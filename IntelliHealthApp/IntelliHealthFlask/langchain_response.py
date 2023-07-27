from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv, find_dotenv
import pdb
import os
import openai
import pinecone
from dotenv import dotenv_values
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import TextLoader
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chains import RetrievalQA
from langchain.agents import Tool
from langchain.agents import initialize_agent
from langchain import OpenAI
from langchain.chains.question_answering import load_qa_chain


#load_dotenv()  # Load environment variables from .env file
# Set your OpenAI API key
env_vars = dotenv_values('utils/.env')
print(env_vars)
PINECONE_API_KEY = env_vars['PINECONE_KEY']
PINECONE_ENV = env_vars['PINECONE_ENVIRON']
openai_api_key = env_vars["apikey"]
openai.api_key = openai_api_key

#PINECONE_API_KEY = getpass.getpass("Pinecone API Key:")
# initialize pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_ENV,  # next to api key in console
)
# chat completion llm
llm = ChatOpenAI(
    openai_api_key=openai_api_key,
    model_name='gpt-3.5-turbo',
    temperature=0.0
)
# conversational memory
conversational_memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=5,
    return_messages=True
)

text_field = "text"
index_name = "diabetes"
# switch back to normal index for langchain
index = pinecone.Index(index_name)
embed = OpenAIEmbeddings(openai_api_key=openai_api_key)

vectorstore = Pinecone(
    index, embed.embed_query, text_field
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

app = Flask(__name__)
conversation_history = []

def home():
    return render_template('index.html')

def chatbot(message):
    #conversation_history = []
    # Append user message to conversation history
    #conversation_history.append({'role': 'user', 'content': message})

    # Get response from language model
    response = generate_response(message)

    # Append model response to conversation history
    conversation_history.append({'role': 'model', 'content': response})

    return response

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
    embeddings = embed
    docsearch = Pinecone.from_existing_index(index_name, embeddings)
    
    #defining LLM
    llm = OpenAI(temperature=0.0)
    #llm = ChatOpenAI(temperature = 0.0, model="gpt-3.5-turbo")

    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever(search_kwargs={"k": 2}))
    #query = "What is DesignOps support model?"
    return qa.run(input_text)

def response_from_pinecone_index(input_text):
    #input_file = "cdc_diabetes_text_2.txt"
    embeddings = embed
    index_name = "diabetes"
    docsearch = Pinecone.from_existing_index(index_name, embeddings)
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

def query_cdc_embedding(input_text, index_name):

    #https://blog.baeke.info/2023/03/16/pinecone-and-openai-magic-a-guide-to-finding-your-long-lost-blog-posts-with-vectorized-search-and-chatgpt/
 
    # set index; must exist
    #index = pinecone.Index('diabetes')
    #env_vars = dotenv_values('utils/.env')
    #PINECONE_API_KEY = env_vars['PINECONE_KEY_cdc']
    #PINECONE_ENV = env_vars['PINECONE_ENVIRON_cdc']

    env_vars = dotenv_values('utils/.env')
    print(env_vars)
    PINECONE_API_KEY = env_vars['PINECONE_KEY']
    PINECONE_ENV = env_vars['PINECONE_ENVIRON']
    openai_api_key = env_vars["apikey"]
    openai.api_key = openai_api_key

    #PINECONE_API_KEY = getpass.getpass("Pinecone API Key:")
    # initialize pinecone
    pinecone.init(
        api_key=PINECONE_API_KEY,  # find at app.pinecone.io
        environment=PINECONE_ENV,  # next to api key in console
    )
    # chat completion llm
    llm = ChatOpenAI(
        openai_api_key=openai_api_key,
        model_name='gpt-3.5-turbo',
        temperature=0.0
    )
    # conversational memory
    conversational_memory = ConversationBufferWindowMemory(
        memory_key='chat_history',
        k=5,
        return_messages=True
    )

    text_field = "text"
    index_name = "diabetes"
    # switch back to normal index for langchain
    index = pinecone.Index(index_name)
    embed = OpenAIEmbeddings(openai_api_key=openai_api_key)

    #if(PINECONE_API_KEY != ""):
    #    pinecone.init(
    #        api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    #        environment=PINECONE_ENV,  # next to api key in console
    #    )

    vectorstore = Pinecone(
        index, embed.embed_query, text_field
    )

    #index = pinecone.Index(index)

    #query = "what is diabetets?"
    # vectorize with OpenAI text-emebdding-ada-002 
    input_text = 'user: ' + input_text
    embedding = openai.Embedding.create(
        input=input_text,
        model="text-embedding-ada-002"
    )
    # print the embedding (length = 1536)
    vector = embedding["data"][0]["embedding"]
    
    search_response = index.query(top_k=5,vector=vector,include_metadata=True)

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

def generate_response(message):
    # Combine conversation history and current message
    #conversation = [{'role': item['role'], 'content': item['content']} for item in conversation_history]
    #conversation.append({'role': 'user', 'content': message})

    # Convert conversation to OpenAI GPT-3 input format
    #input_text = '\n'.join([f"{item['role']}: {item['content']}" for item in conversation])

    #reply2 = response_from_pinecone_index(message,)
    #if not reply2.startswith("From Diabetes Content"):
    #   reply2 = "From Diabetes Content: " + reply2
    #print(response)
    #return reply2
    input_text = message
    reply = query_cdc_embedding(input_text, "diabetes")
    if not reply.startswith("Answer from cdc.gov/diabetes: "):
        reply = "Answer from cdc.gov/diabetes: " + reply
    return reply
