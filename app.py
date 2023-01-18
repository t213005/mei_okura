import streamlit as st
import random

def main():
    st.title("Omikuji App")
    st.write("This app helps you draw a fortune.")

    # Draw a fortune
    fortunes = ["大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶"]
    fortune = random.choice(fortunes)

    # Show the fortune
    st.write("Your fortune is : " + fortune)
    # Show the fortune image
    img_path = "img/" + fortune + ".png"
    st.image(img_path, width=300)

if __name__ == "__main__":
    main()