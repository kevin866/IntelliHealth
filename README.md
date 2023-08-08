# IntelliHealth
Introducing a DFW IT competition project: an advanced healthcare AI recommendation system. Enhance patient outcomes with personalized recommendations, clinical decision support, risk stratification, and continuous learning.
notion notebook
https://mud-virgo-611.notion.site/DFW-IT-competition-40fe04113aca46d382e5e144644190eb?pvs=4

# Creating local IntelliHealth System
## Download local copy from Git repository 
  * Git clone https://github.com/kevin866/IntelliHealth.git

## Create Pinecone index
  * [Registering account of Pinecone] (https://www.pinecone.io/)
  * [Following Jupyter Notebook](https://github.com/kevin866/IntelliHealth/blob/justin/chatbot/diabetes_KB/pinecone_index_cdc_diabetes.ipynb)
  * Adding OpenAI API key and Pinecone API key at file utils/.env as following
    * apikey=sk-**
    * model_path=model_kaggle_6.pkl
    * preprocessed_data_path=diabetes_prediction_dataset.csv
    * OPENAI_API_KEY=sk-****
    * PINECONE_KEY=***
    * PINECONE_ENVIRON=asia-southeast1-gcp-free


## Start local web app 
  1. start back end Flask app
    * cd IntelliHealthApp/IntelliHealthFlask
    * <python app.py>
      * display OrderedDict([('apikey', 'sk-*****'), ('model_path', 'model_kaggle_6.pkl'), ('preprocessed_data_path', 'diabetes_prediction_dataset.csv'), ('OPENAI_API_KEY', 'sk-****'), ('PINECONE_KEY', '6238f957-bdfe-4b52-8f3f-b85b1fd8183a'), ('PINECONE_ENVIRON', 'asia-southeast1-gcp-free')])
     * Serving Flask app 'app'
     * Debug mode: off
     WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:5000
  2. start front end React app
    * cd IntelliHealthReact/intellihealthfrontend
    * npm start 
      * Compiled successfully!

      * You can now view intellihealthfrontend in the browser.

      * Local:            http://localhost:3000
      * On Your Network:  http://10.0.0.39:3000

      * Note that the development build is not optimized.
      * To create a production build, use npm run build.

      * webpack compiled successfully

    


