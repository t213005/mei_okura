import streamlit as st
import random

# おみくじの結果を格納したリスト
omikuji_list = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]

def main():
    st.title("おみくじアプリ")

    # おみくじを引くボタン
    if st.button("おみくじを引く"):
        result = random.choice(omikuji_list)
        st.success(result)

if __name__ == "__main__":
    main()