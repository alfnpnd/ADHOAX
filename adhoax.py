import streamlit as st
import pickle
import pandas as pd
import re
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

hide_menu = """
<style>
#MainMenu {
    visibility:hidden;
}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

load_clf = pickle.load(open('model10k75.pkl', 'rb'))
load_vectorizer = pickle.load(open("vectorizer10k.pkl", "rb"))


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
def text_preprocessing(text):
    tokenizer_reg = nltk.tokenize.RegexpTokenizer(r'\w+')
    
    nopunc = wordopt(text)
    tokenized_text = tokenizer_reg.tokenize(nopunc)
    remove_stopwords = [w for w in tokenized_text if w not in stopwords.words('indonesian')]
    combined_text = ' '.join(remove_stopwords)
    return combined_text



def output_lable(n):
    if n == 'HOAX':
        return "BERITA HOAX!!!"
    elif n == 'FAKTA':
        return "BUKAN HOAX :)"


def manual_testing(news):
    if news == '':
        st.error('masukkan berita')
    elif news == 'type here':
        st.error('masukkan berita')
    else:
        testing_news = {"text": [news]}
        new_def_test = pd.DataFrame(testing_news)
        new_def_test["text"] = new_def_test["text"].apply(wordopt).apply(text_preprocessing)
        new_x_test = new_def_test["text"]
        new_xv_test = load_vectorizer.transform(new_x_test)
        pred_DT = load_clf.predict(new_xv_test)

        return f"\n\nPrediksi : {output_lable(pred_DT[0])}"

news_text = st.text_area('Masukan Teks Berita','type here')
news = (news_text)

if st.button('Enter'):
    st.success(manual_testing(news))
    
my_expander = st.expander(label='Panduan')
with my_expander:
    'Adhoax adalah sebuah aplikasi pendeteksi berita hoax yang dibuat menggunakan metode C4.5'
    'terdiri dari 10rb dataset untuk memprediksi hasil deteksi dengan akurasi 75%'
    'panduan'
    '1. masukkan teks berita yang akan di deteksi pada kolom. boleh judul, isi, maupun paragraf.'
    '2. Tekan Enter lalu tunggu sampai hasil deteksi keluar'
