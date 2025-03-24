import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Competitive Pricing Reaction Simulator")
st.write("Set initial conditions and see how Company A's revenue and profit change.")

# User inputs for initial settings
st.header("Initial Settings")

col1, col2, col3 = st.columns(3)

with col1:
    price_a = st.number_input("Company A Price ($)", min_value=1.0, value=100.0)
    unit_cost_a = st.number_input("Company A Unit Cost ($)", min_value=0.0, value=50.0)

with col2:
    price_b = st.number_input("Company B Price ($)", min_value=1.0, value=95.0)
    sales_b = st.number_input("Company B Sales Volume", min_value=0, value=900)

with col3:
    price_c = st.number_input("Company C Price ($)", min_value=1.0, value=105.0)
    sales_c = st.number_input("Company C Sales Volume", min_value=0, value=800)

# Sales volume for Company A
sales_a = st.number_input("Company A Sales Volume", min_value=0, value=1000)

# Compute revenue and profit for Company A
revenue_a = price_a * sales_a
profit_a = (price_a - unit_cost_a) * sales_a

st.write(f"### Company A Revenue: ${revenue_a:,.2f}")
st.write(f"### Company A Profit: ${profit_a:,.2f}")

# Simulate different price points for Company A
st.header("Revenue and Profit at Different Price Points")

price_range = range(int(price_a * 0.5), int(price_a * 1.5), 5)
revenues = []
profits = []

for p in price_range:
    rev = p * sales_a  # Keep sales volume fixed for simplicity
    prof = (p - unit_cost_a) * sales_a
    revenues.append(rev)
    profits.append(prof)

# Create a dataframe
df = pd.DataFrame({"Price": price_range, "Revenue": revenues, "Profit": profits})

# Plot revenue and profit curves
fig, ax = plt.subplots()
ax.plot(df["Price"], df["Revenue"], label="Revenue ($)", color="blue")
ax.plot(df["Price"], df["Profit"], label="Profit ($)", color="green")
ax.set_xlabel("Company A Price ($)")
ax.set_ylabel("Amount ($)")
ax.legend()
ax.grid()

st.pyplot(fig)
