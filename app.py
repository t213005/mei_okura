import streamlit as st
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

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

    # Get optimization method
    method = st.selectbox("Select an optimization method:", ["BFGS", "CG", "L-BFGS-B", "SLSQP"])

    # Find the minimum value
    res = minimize(func, x0, method=method)

    # Show results
    st.write(f"Minimum value: {res.fun}")
    st.write(f"Minimum occurs at x = {res.x}")

    # Plot the function and optimization result
    x = np.linspace(-10, 10, 100)
    y = func(x)
    plt.plot(x, y, label="Function")
    plt.scatter(res.x, res.fun, c='r', label="Minimum")
    plt.legend()
    st.pyplot()

if __name__ == "__main__":
    main()