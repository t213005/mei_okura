import streamlit as st

st.title("Word to Sentence Generator")

word = st.text_input("Enter a word:")

if st.button("Generate"):
    # Insert code here to generate a sentence using the input word
    sentence = "The " + word + " jumped over the moon."
    st.success(sentence)