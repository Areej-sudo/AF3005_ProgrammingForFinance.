import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set app title
st.title("Investment Portfolio Risk Analyzer")
st.sidebar.header("Portfolio Allocation")

# Define asset classes and default allocations
assets = ["Stocks", "Bonds", "Crypto", "Real Estate", "Gold"]
default_allocations = [40, 30, 10, 10, 10]

# User inputs: Sliders for asset allocation
allocations = []
for asset, default in zip(assets, default_allocations):
    allocation = st.sidebar.slider(f"{asset} Allocation (%)", 0, 100, default)
    allocations.append(allocation)

# Ensure total allocation is 100%
total_allocation = sum(allocations)
if total_allocation != 100:
    st.sidebar.warning("Total allocation must be 100%!")

# Simulated historical data (expected return and volatility)
np.random.seed(42)
expected_returns = np.random.uniform(5, 15, len(assets)) 
volatilities = np.random.uniform(10, 30, len(assets)) 

# Convert to DataFrame
df = pd.DataFrame({"Asset": assets, "Allocation": allocations, "Expected Return (%)": expected_returns, "Volatility (%)": volatilities})

# Portfolio metrics calculation
portfolio_return = np.dot(df["Allocation"], df["Expected Return (%)"]) / 100
portfolio_volatility = np.sqrt(np.dot(df["Allocation"] ** 2, df["Volatility (%)"] ** 2)) / 100
sharpe_ratio = portfolio_return / portfolio_volatility if portfolio_volatility > 0 else 0

# Display metrics
st.subheader("Portfolio Analysis")
st.write(df)
st.metric("Expected Portfolio Return", f"{portfolio_return:.2f}%")
st.metric("Portfolio Volatility", f"{portfolio_volatility:.2f}%")
st.metric("Sharpe Ratio", f"{sharpe_ratio:.2f}")

# Portfolio Allocation Pie Chart
fig, ax = plt.subplots()
ax.pie(df["Allocation"], labels=df["Asset"], autopct='%1.1f%%', startangle=90)
ax.set_title("Portfolio Allocation")
st.pyplot(fig)

# Risk vs. Return Scatter Plot
fig, ax = plt.subplots()
ax.scatter(volatilities, expected_returns, c='blue', label="Asset Classes")
ax.scatter(portfolio_volatility * 100, portfolio_return, c='red', marker='x', s=100, label="Portfolio")
ax.set_xlabel("Volatility (%)")
ax.set_ylabel("Expected Return (%)")
ax.set_title("Risk vs. Return")
ax.legend()
st.pyplot(fig)

st.sidebar.text("Adjust allocations to optimize your risk-return balance!")
