import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from preprocessing import preprocessor
import streamlit as st

model = pickle.load(open("SAVED_MODEL/model_02-01-2022.sav", 'rb'))

st.image("Image/phishing.jpg")
st.title("URL Spam Classifier")

input_url = st.text_input("Enter the URL")

if st.button("Predict"):
    input_df = pd.DataFrame({"url": [input_url], "is_spam": [False]})
    input_df = preprocessor(input_df)
    features = [feature for feature in input_df.columns if feature not in ["url", "is_spam"]]
    X = input_df[features]

    result = model.predict(X)[0]
    if result == 1:
        st.header("This is a spam URL !!! Don't click on it.")
    else:
        st.header("This URL is safe.")
        #print("This is a spam URL !!! Don't click on it.")

#url = ["https://briefingday.us8.list-manage.com/unsubscribe"]
#loaded_model = pickle.load(open("SAVED_MODEL/model_02-01-2022.sav", 'rb'))




