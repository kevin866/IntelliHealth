"""from service.get_gpt_service import GptService
cur_service = GptService()
response_content = cur_service.get_gpt_response(question)
print(type(response_content))
print(response_content["choices"])"""
import os
import openai
from dotenv import dotenv_values
env_vars = dotenv_values('utils/.env')
openai.api_key = env_vars["apikey"]
query = "Give recommendation for preventing diabetes to a male 29 years old with a Hypertension of 3, Heart Disease of 3, Smoking history, a BMI of 76, HbA1c Level of 87, and blood glucose level of 35. "
question = [
    {"role": "system", "content": "You are a health consultant specialized in diabetes."},
    {"role": "user", "content": query}
]
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=question,
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

