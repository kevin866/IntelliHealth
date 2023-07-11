import pickle
import pandas as pd

modelFile = open('model_kaggle_6.pkl', 'rb')

model6 = pickle.load(modelFile)

df = pd.read_csv('Data6/diabetes_prediction_dataset.csv')

# gender: 0- female, 1-male
# smoking history: 4-never, 0-no info, 1-current, 3-former, 2-ever, 5-not current
data = {'gender': [0],
        'age': [80],
        'hypertension': [0],
        'heart_disease': [0],
        'smoking_history': [4],
        'bmi': [25.19],
        'HbA1c_level': [6.6],
        'blood_glucose_level': [140]
        }
df = pd.DataFrame(data)
pred = model6.predict(df)
# expected 0 - no diabetes
print(pred)