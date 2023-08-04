import os

import numpy as np
from flask import Flask, request, json, send_from_directory
from flask_cors import CORS, cross_origin
from service.get_gpt_service import GptService
from service.get_model_service import ModelService
import langchain_response
import openai
import pdb
app = Flask(__name__, static_folder='client/build', static_url_path='')

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/v1/health')
@cross_origin()
def health():  # put application's code here
    return 'Status: Healthy, Version: 1.0'

@app.route('/api/v1/chat/<chat_content>')
@cross_origin()
def chat(chat_content):
    response = langchain_response.chatbot(chat_content)
    return {"text":response}


"""
def chat(chat_content):
    pdb.set_trace()
    response = langchain_response.chatbot(chat_content)
    #return {"text":response}
    print("Response:", response)
    return jsonify({'message': response}) #, 'additionalText': additional_text

    cur_service = GptService()
    response_content = cur_service.get_gpt_response(chat_content)
    print(type(response_content))
    print(response_content["choices"][0])
    return response_content["choices"][0]
"""   
def recommendation_generator(data):
    "Give recommendation for preventing diabetes to a male 29 years old with a Hypertension of 3, Heart Disease of 3, Smoking history, a BMI of 76, HbA1c Level of 87, and blood glucose level of 35. "
    query = "Give a very concise recommendations to a {age}-year-old {gender} with {hypertension}, {heart_disease}, {smoking_history}, a BMI of {BMI}, HbA1c level of {HbA1c}, and a blood glucose level of {glucose}. Make you repsonse in second person pronoun.'".format(age = data[1],
                                                                                                                                                                                                            gender = "male" if data[0] == 1.0 else "female", 
                                                                                                                                                                                                            hypertension = "hypertension" if data[2] == 1.0 else "no hypertension", 
                                                                                                                                                                                                            heart_disease = "heart diease" if data[3] == 1.0 else "no heart diease", 
                                                                                                                                                                                                            smoking_history = "smoking history" if data[4] == 1.0 else "no smoking history",
                                                                                                                                                                                                            BMI = int(data[5]), HbA1c = data[6], glucose = data[7])

    question = [
        {"role": "system", "content": "You are a health consultant specialized in diabetes."},
        {"role": "user", "content": query}
        ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=question,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    return response['choices'][0]['message']['content']

@app.route('/api/v1/model/prediction', methods=['POST'])
@cross_origin()
def predict():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json_input = request.json
        #print("model request inputs: ", json_input)
        cur_model = ModelService()
        #print(type(json_input))
        body = json.loads(json_input['body'])
        #print(type(body))
        matrix = body["data"]
        #print(matrix)
        input_data = np.array(matrix)
        print(input_data)
        print(input_data.shape)
        prediction = cur_model.predict(input_data)
        data = np.ravel(input_data)
        recom = recommendation_generator(np.ravel(input_data))
        if prediction == 1.0:
            prediction = "You have a high chances of developing diabetes. \n"
        else:
            prediction = "You have a low chances of developing diabetes. \n"
        #print("prediction: ", prediction)

    else:
        return 'Content-Type not supported!', 400
    #print(recom)
    prediction = prediction+ recom.replace('\n\n', "\n  ")
    response = json.dumps({"prediction": prediction})
    print(response)
    return response

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
