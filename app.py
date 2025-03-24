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
total_sales_a = sum(sales_a)

# Calculate revenue and profit for Company A
revenue_a = price_a * total_sales_a
profit_a = (price_a - unit_cost_a) * total_sales_a

# Display results
st.write(f"### Company A Revenue: ${revenue_a:,.2f}")
st.write(f"### Company A Profit: ${profit_a:,.2f}")
st.write(f"### Company A Total Sales Volume: {total_sales_a:,.0f}")

# Simulate different price points for Company A and customer reactions
st.header("Customer Reaction at Different Price Points")

price_range = range(int(price_a * 0.5), int(price_a * 1.5), 5)
revenues = []
profits = []
sales_a_prices = []

for p in price_range:
    # Get new customer sales at different price points
    sales_a_new = calculate_customer_sales(p, base_sales_a, num_customers)
    total_sales_a_new = sum(sales_a_new)
    
    # Calculate revenue and profit for Company A at this price point
    rev = p * total_sales_a_new
    prof = (p - unit_cost_a) * total_sales_a_new
    
    revenues.append(rev)
    profits.append(prof)
    sales_a_prices.append(total_sales_a_new)

# Create a dataframe
df = pd.DataFrame({
    "Price": price_range,
    "Revenue": revenues,
    "Profit": profits,
    "Total Sales": sales_a_prices
})

# Plot revenue, profit, and total sales for Company A
fig, ax1 = plt.subplots()

# Plot revenue and profit for Company A
ax1.plot(df["Price"], df["Revenue"], label="Revenue ($)", color="blue")
ax1.plot(df["Price"], df["Profit"], label="Profit ($)", color="green")
ax1.set_xlabel("Company A Price ($)")
ax1.set_ylabel("Revenue / Profit ($)", color="black")
ax1.tick_params(axis='y', labelcolor="black")

# Plot total sales volume for Company A
ax2 = ax1.twinx()  # Instantiate another y-axis
ax2.plot(df["Price"], df["Total Sales"], label="Total Sales Volume", color="red", linestyle="--")
ax2.set_ylabel("Total Sales Volume", color="black")
ax2.tick_params(axis='y', labelcolor="black")

# Legends
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

ax1.grid()

st.pyplot(fig)
