import streamlit as st
import random

def main():
    st.title("Omikuji App")
    st.write("This app helps you draw a fortune.")

    # Draw a fortune
    fortunes = ["大吉", "中吉", "小吉", "吉", "半吉", "末吉", "末小吉", "凶", "小凶", "半凶", "末凶", "大凶"]
    fortune = random.choice(fortunes)

    # Show the fortune
    st.write("Your fortune is: " + fortune)

if __name__ == "__main__":
    main()