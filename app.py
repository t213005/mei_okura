import streamlit as st
from scipy.optimize import minimize

def main():
    st.title("Function Optimizer")
    st.write("This app helps you find the minimum value of a function.")

    # Get function from user
    func_str = st.text_input("Enter a function in terms of x:")

    # Define the optimization function
    def func(x):
        return eval(func_str)

    # Get initial guess from user
    x0 = st.number_input("Enter an initial guess for x:")

    # Find the minimum value
    res = minimize(func, x0)

    # Show results
    st.write(f"Minimum value: {res.fun}")
    st.write(f"Minimum occurs at x = {res.x}")

if __name__ == "__main__":
    main()