import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

ps=PorterStemmer()

model = pickle.load(open('model.pkl','rb'))
tfidf = pickle.load(open('vectorizer.pkl','rb'))

st.title("SMS/Email Spam Classifier")
input_sms = st.text_area("Enter your text")
if st.button("Predict"):

    #preprocessing
    def preprocess(text):
        review = re.sub('[^a-zA-Z]', ' ', text)
        review = review.lower()
        words = word_tokenize(review)
        review = [ps.stem(word) for word in words if word not in stopwords.words('english')]

        return " ".join(review)

    preprocessed = preprocess(input_sms)
    #vectorize
    vector = tfidf.transform([preprocessed])
    #predict
    output = model.predict(vector)[0]
    #show
    if output==1:
        st.header("Spam")
    else:
        st.header("Ham")