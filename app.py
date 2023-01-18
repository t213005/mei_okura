import streamlit as st
from transformers import AutoModelWithLMHead, AutoTokenizer

# Load the pre-trained model and tokenizer
model = AutoModelWithLMHead.from_pretrained("text-davinci-002")
tokenizer = AutoTokenizer.from_pretrained("text-davinci-002")

st.title("Text Generation App")

# Get the user's input
prompt = st.text_input("Enter your prompt:")

# Generate text
if st.button("Generate text"):
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to('cuda')
    output = model.generate(input_ids, max_length=100, do_sample=True, top_p=0.95, top_k=50)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    st.write("Generated text:")
    st.write(generated_text)