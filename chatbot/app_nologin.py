from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import pdb
import os
import openai
import pinecone
from dotenv import dotenv_values
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chains import RetrievalQA
import newspaper


load_dotenv()  # Load environment variables from .env file

# conversational memory
conversational_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True
)

text_field = "text"
index_name = "complication"
# switch back to normal index for langchain
index = pinecone.Index(index_name)
embed = OpenAIEmbeddings()

vectorstore = Pinecone(
    index, embed.embed_query, text_field
)

app = Flask(__name__)
conversation_history = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/extract')

def extract_text():
    url = request.args.get('url')
    article = newspaper.Article(url)
    article.download()
    article.parse()
    return article.text

@app.route('/chat', methods=['POST'])
def chat():
    #pdb.set_trace()
    message = request.form['message']
    #print(request.form)  # Add this line to print the form data
    option = request.form.get('select-option') #get
    additional_text = request.form['additional-text']

    print("Received message:", message)
    print("Selected option:", option)
    print("Additional text:", additional_text)
    
    #pdb.set_trace()
    env_vars = dotenv_values('.env')
    # Set your OpenAI API key
    
    #openai_api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = env_vars['OPENAI_API_KEY']
    openai_api_key = openai.api_key
    os.environ['OPENAI_API_KEY'] = openai_api_key
    # chat completion llm
    llm = ChatOpenAI(
        openai_api_key=openai_api_key,
        model_name='gpt-3.5-turbo',
        temperature=0.0
    )
    if(option == "cdc_diabetes"):
        PINECONE_API_KEY = env_vars['PINECONE_KEY_cdc']
        PINECONE_ENV = env_vars['PINECONE_ENVIRON_cdc']
    else:
        PINECONE_API_KEY = env_vars['PINECONE_KEY']
        PINECONE_ENV = env_vars['PINECONE_ENVIRON']
    #PINECONE_API_KEY = getpass.getpass("Pinecone API Key:")
    # initialize pinecone
    pinecone.init(
        api_key=PINECONE_API_KEY,  # find at app.pinecone.io
        environment=PINECONE_ENV,  # next to api key in console
    )
    # retrieval qa chain
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )


    tools = [
        Tool(
            name='Knowledge Base',
            func=qa.run,
            description=(
                'use this tool when answering general knowledge queries to get '
                'more information about the topic'
            )
        )
    ]
    agent = initialize_agent(
        agent='chat-conversational-react-description',
        tools=tools,
        llm=llm,
        verbose=True,
        max_iterations=3,
        early_stopping_method='generate',
        memory=conversational_memory
    )

    
    conversation_history = []
    # Append user message to conversation history
    conversation_history.append({'role': 'user', 'content': message})

    # Get response from language model
    response = generate_response(message, option,additional_text)

    # Append model response to conversation history
    conversation_history.append({'role': 'model', 'content': response})
    print("Response:", response)
    return jsonify({'message': response}) #, 'additionalText': additional_text

def answer_by_context(question, context):
    response_a = openai.Completion.create(
            prompt=f"Answer the question based on the context below, \
                  and if the question can't be answered based on the context, \
                      say \"I don't know\"\n\nContext: \
                          {context}\n\n---\n\nQuestion: {question}\nAnswer:",
            temperature=0,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            model="text-davinci-003" # "gpt-3.5-turbo"# 
        )
    return response_a["choices"][0]["text"].strip()

def search_pinecone_index(index_name, input_text):
    embeddings = OpenAIEmbeddings()
    docsearch = Pinecone.from_existing_index(index_name, embeddings)
    
    #defining LLM
    llm = OpenAI(temperature=0.0)
    #llm = ChatOpenAI(temperature = 0.0, model="gpt-3.5-turbo")

    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever(search_kwargs={"k": 2}))
    #query = "What is DesignOps support model?"
    return qa.run(input_text)

def response_from_pinecone_index(input_text):
    #input_file = "cdc_diabetes_text_2.txt"
    embeddings = OpenAIEmbeddings()
    index_name = "complication"
    #docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)
    # if you already have an index, you can load it like this
    docsearch = Pinecone.from_existing_index(index_name, embeddings)
    #question = "What is the symptoms of diabetes?"
    docs = docsearch.similarity_search(input_text, k=3)
    print(docs[0].page_content)
    context = docs[0].page_content
    answer = answer_by_context(input_text,context)
    return answer

def get_highest_score(items):
    highest_score_item = max(items, key=lambda item: item["score"])
 
    if highest_score_item["score"] > 0.8:
        return highest_score_item["metadata"]['text'], highest_score_item["metadata"]['url']
    else:
        return ""

def query_cdc_embedding(input_text, index):

    #https://blog.baeke.info/2023/03/16/pinecone-and-openai-magic-a-guide-to-finding-your-long-lost-blog-posts-with-vectorized-search-and-chatgpt/
 
    # set index; must exist
    #index = pinecone.Index('diabetes')
    index = pinecone.Index(index)

    #query = "what is diabetets?"
    # vectorize with OpenAI text-emebdding-ada-002
    embedding = openai.Embedding.create(
        input=input_text,
        model="text-embedding-ada-002"
    )
    # print the embedding (length = 1536)
    vector = embedding["data"][0]["embedding"]
    
    search_response = index.query(
        top_k=5,
        vector=vector,
        include_metadata=True
    )

    context, url = get_highest_score(search_response['matches'])

    prompt = f"Answer the question based on the context below:\n\n{context}\n\nQuestion: {input_text}\nAnswer:"

    response = openai.Completion.create(
        prompt=prompt,
        model="text-davinci-003",
        temperature=0,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    answer = response.choices[0].text.strip()
    answer_with_url = answer + ' URL: ' + url  # Append the answer with the URL
    return answer_with_url




def generate_response(message, option,additional_text):
    # Combine conversation history and current message
    conversation = [{'role': item['role'], 'content': item['content']} for item in conversation_history]
    conversation.append({'role': 'user', 'content': message})

    # Convert conversation to OpenAI GPT-3 input format
    input_text = '\n'.join([f"{item['role']}: {item['content']}" for item in conversation])

    # Call the language model API
    # Debug: Print the input text
    #print("Input Text:", input_text)
    # Start the debugger
    #pdb.set_trace()
    if option == "input_text":
        if(additional_text == "Enter or paste text here..." or additional_text == ""):
            reply = "From input text: no text was entered"
        else:
            reply = answer_by_context(input_text,additional_text)
            if not reply.startswith("Answer from input text"):
                reply = "Answer from input text: " + reply
        return reply
    elif option == "chatgpt":
        #response_b = openai.Completion.create(
        #    model='gpt-3.5-turbo',#engine='text-davinci-003',
        #    prompt=input_text,
        #    max_tokens=50
        #)

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": input_text}
                ]
        )
        #pdb.set_trace()
        #print(completion)
        reply = completion.choices[0].message['content']
        # Extract the model's reply from the response
        #reply = response_b.choices[0].text.strip()
        if not reply.startswith("From ChatGPT"):
            reply = "From ChatGPT: " + reply
        return reply
    elif option == "cdc_diabetes":
        #pdb.set_trace()
        #queries = [
        #    {'query': input_text}
        #]
        #endpoint_url = 'http://localhost:8000'
        #reply = query_cdc_2(endpoint_url, input_text)
        reply = query_cdc_embedding(input_text, "diabetes")
        if not reply.startswith("Answer from cdc.gov/diabetes: "):
                reply = "Answer from cdc.gov/diabetes: " + reply
        return reply
    else:
        #pdb.set_trace()
        #result = search_pinecone_index(index_name, input_text)
        #print(result)
        #result = agent(input_text)
        #reply2 = result
        reply2 = response_from_pinecone_index(input_text)
        if not reply2.startswith("Answer from diabetes.org"):
            reply2 = "Answer from diabetes.org: " + reply2
        #print(response)
        return reply2
    #return response

if __name__ == '__main__':
    print("abc")
    app.run(debug=True)
