import streamlit as st
from janome.tokenizer import Tokenizer

def generate_sentence(word):
    t = Tokenizer()
    tokens = t.tokenize(word)
    sentence = "入力した単語は"
    for token in tokens:
        sentence += token.surface
    sentence += "です。"
    return sentence

st.title("単語から文章生成アプリ(Japanese)")

word = st.text_input("単語を入力:")

if st.button("生成"):
    sentence = generate_sentence(word)
    st.success(sentence)