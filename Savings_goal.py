import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set Streamlit app title
st.title("💰 Savings Goal Planner 🎯")
st.sidebar.header("Set Your Savings Goal")

# User Input Widgets
target_savings = st.sidebar.number_input("Target Savings Amount ($)", min_value=100, step=100, value=5000)
monthly_income = st.sidebar.number_input("Monthly Income ($)", min_value=0, step=100, value=3000)
monthly_expenses = st.sidebar.number_input("Monthly Expenses ($)", min_value=0, step=100, value=2000)
savings_period = st.sidebar.slider("Savings Period (Months)", 1, 60, 12)

# Compute Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Validate input and calculate savings
if monthly_savings <= 0:
    st.error("⚠️ Your expenses are greater than or equal to your income! Reduce expenses or increase income to save.")
else:
    total_savings = [monthly_savings * i for i in range(1, savings_period + 1)]
    months = list(range(1, savings_period + 1))

    # Display Savings Overview
    st.subheader("📊 Savings Plan Overview")
    st.write(f"**💵 Monthly Savings:** ${monthly_savings}")
    st.write(f"**📅 Total Savings After {savings_period} Months:** ${total_savings[-1]}")

    # Check if target savings is met
    if total_savings[-1] >= target_savings:
        st.success("🎉 Congratulations! You will reach your savings goal on time! 🚀")
    else:
        st.warning("⚠️ Your savings are insufficient to meet your target. Consider increasing savings or extending the period.")

    # 📈 Line Chart: Savings Growth Over Time
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(months, total_savings, marker='o', linestyle='-', color='b', label='Total Savings')
    ax.axhline(y=target_savings, color='r', linestyle='--', label='Target Savings')
    ax.set_xlabel("Months")
    ax.set_ylabel("Savings ($)")
    ax.set_title("📈 Savings Growth Over Time")
    ax.legend()
    st.pyplot(fig)  # Display the chart in Streamlit

    # 🍰 Pie Chart: Income vs. Expenses vs. Savings
    labels = ['Expenses', 'Savings']
    values = [monthly_expenses, monthly_savings]
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'green'])
    ax.set_title("💰 Income Distribution")
    st.pyplot(fig)

st.sidebar.text("🔧 Adjust values to optimize your savings goal!")
