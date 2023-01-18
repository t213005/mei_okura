import streamlit as st
import openai_secret_manager

# Get API Key
secrets = openai_secret_manager.get_secret("openai")
api_key = secrets["api_key"]

# Use the OpenAI API to generate text
import openai
openai.api_key = api_key

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

def main():
    st.title("Text Generator")
    st.write("This app helps you generate text based on your input.")

    # Get keywords from user
    keywords = st.text_input("Enter keywords:")

    # Generate text
    generated_text = generate_text(f"Write a short story based on the following keywords: {keywords}")

    # Show the generated text
    st.write("Generated text:")
    st.write(generated_text)

if __name__ == "__main__":
    main()