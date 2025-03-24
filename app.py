import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Customer Price Reaction Simulator")
st.write("Set initial conditions and see how customers react to Company A's price changes.")

# User inputs for initial settings
st.header("Initial Settings")

price_a = st.number_input("Company A Price ($)", min_value=1.0, value=100.0)
unit_cost_a = st.number_input("Company A Unit Cost ($)", min_value=0.0, value=50.0)
base_sales_a = st.number_input("Base Sales Volume (customers at price $100)", min_value=1, value=1000)

# Ensure the base sales value is not zero or negative
if base_sales_a <= 0:
    st.error("Base sales volume must be a positive value.")
    base_sales_a = 1000  # Set default value to avoid further issues

# Number of customers
num_customers = 10

# Simulate customer reactions based on price
def calculate_customer_sales(price_a, base_sales_a, num_customers):
    # Elasticity factor (simple model: 1% price increase -> 2% decrease in demand)
    elasticity_factor = 0.02
    sales = []
    
    for i in range(num_customers):
        # Customer demand decreases with price increase (elasticity model)
        customer_demand = base_sales_a * (1 - elasticity_factor * (price_a - 100) / 100)
        sales.append(max(0, customer_demand))  # Prevent negative sales

    return sales

# Calculate customer sales at the current price point
sales_a = calculate_customer_sales(price_a, base_sales_a, num_customers)

# Total sales volume for Company A
