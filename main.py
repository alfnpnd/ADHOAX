import streamlit as st
import pickle
import pandas as pd
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer

load_clf = pickle.load(open('DTModel.pkl', 'rb'))
load_vectorizer = pickle.load(open("vectorization.pkl", "rb"))


st.title('ADHOAX')
st.info('Aplikasi Deteksi Berita Hoax')

def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text



def output_lable(n):
    if n == 'HOAX':
        return "BERITA HOAX!!!"
    elif n == 'FAKTA':
        return "BUKAN HOAX :)"


def manual_testing(news):
    if news == '':
        st.error('masukkan berita')
    else:
        testing_news = {"text": [news]}
        new_def_test = pd.DataFrame(testing_news)
        new_def_test["text"] = new_def_test["text"].apply(wordopt)
        new_x_test = new_def_test["text"]
        new_xv_test = load_vectorizer.transform(new_x_test)
        pred_DT = load_clf.predict(new_xv_test)

        return f"\n\nPrediksi : {output_lable(pred_DT[0])}"

news_text = st.text_area('masukan teks','type here')
news = (news_text)

if st.button('Classify'):
    st.success(manual_testing(news))
