import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Competitive Pricing Reaction Simulator")
st.write("Set initial conditions and see how Company A's revenue and profit change along with competitive reactions.")

# User inputs for initial settings
st.header("Initial Settings")

col1, col2, col3 = st.columns(3)

with col1:
    price_a = st.number_input("Company A Price ($)", min_value=1.0, value=100.0)
    unit_cost_a = st.number_input("Company A Unit Cost ($)", min_value=0.0, value=50.0)

with col2:
    price_b_discount = st.number_input("Company B Price Discount (%)", min_value=0.0, max_value=100.0, value=5.0)
    sales_b = st.number_input("Company B Sales Volume", min_value=0, value=900)

with col3:
    price_c_markup = st.number_input("Company C Price Markup (%)", min_value=0.0, max_value=100.0, value=5.0)
    sales_c = st.number_input("Company C Sales Volume", min_value=0, value=800)

# Sales volume for Company A
sales_a = st.number_input("Company A Sales Volume", min_value=0, value=1000)

# Simulate competitive reactions and adjust sales volumes
# Reaction function for sales volume based on price difference
def calculate_sales_volume(price_a, price_b, price_c, base_sales_a, base_sales_b, base_sales_c):
    # Sales volume changes based on price differences (simplified model)
    sales_a_new = base_sales_a * (1 - 0.01 * (price_a - 100))  # Adjust based on price
    sales_b_new = base_sales_b * (1 - 0.01 * (price_b - 100))  # Adjust based on price
    sales_c_new = base_sales_c * (1 - 0.01 * (price_c - 100))  # Adjust based on price
    return sales_a_new, sales_b_new, sales_c_new

# Calculate initial sales volumes and prices
price_b = price_a * (1 - price_b_discount / 100)  # Company B adjusts based on a discount from Company A's price
price_c = price_a * (1 + price_c_markup / 100)  # Company C adjusts based on a markup from Company A's price

# Calculate sales volumes
sales_a_new, sales_b_new, sales_c_new = calculate_sales_volume(price_a, price_b, price_c, sales_a, sales_b, sales_c)

# Calculate revenue and profit for Company A
revenue_a = price_a * sales_a_new
profit_a = (price_a - unit_cost_a) * sales_a_new

st.write(f"### Company A Revenue: ${revenue_a:,.2f}")
st.write(f"### Company A Profit: ${profit_a:,.2f}")
st.write(f"### Company A Sales Volume: {sales_a_new:,.0f}")
st.write(f"### Company B Price: ${price_b:,.2f}, Sales Volume: {sales_b_new:,.0f}")
st.write(f"### Company C Price: ${price_c:,.2f}, Sales Volume: {sales_c_new:,.0f}")

# Simulate different price points for Company A
st.header("Revenue and Profit at Different Price Points")

price_range = range(int(price_a * 0.5), int(price_a * 1.5), 5)
revenues = []
profits = []
sales_a_prices = []
sales_b_prices = []
sales_c_prices = []

for p in price_range:
    # Update prices for Companies B and C dynamically
    price_b_new = p * (1 - price_b_discount / 100)  # Company B price adjustment
    price_c_new = p * (1 + price_c_markup / 100)  # Company C price adjustment

    # Get new sales volumes
    sales_a_new, sales_b_new, sales_c_new = calculate_sales_volume(p, price_b_new, price_c_new, sales_a, sales_b, sales_c)

    # Revenue and profit for Company A
    rev = p * sales_a_new
    prof = (p - unit_cost_a) * sales_a_new

    revenues.append(rev)
    profits.append(prof)
    sales_a_prices.append(sales_a_new)
    sales_b_prices.append(sales_b_new)
    sales_c_prices.append(sales_c_new)

# Create a dataframe
df = pd.DataFrame({
    "Price": price_range,
    "Revenue": revenues,
    "Profit": profits,
    "Sales A": sales_a_prices,
    "Sales B": sales_b_prices,
    "Sales C": sales_c_prices
})

# Plot revenue, profit, and sales for all companies
fig, ax1 = plt.subplots()

# Plot revenue and profit for Company A
ax1.plot(df["Price"], df["Revenue"], label="Revenue ($)", color="blue")
ax1.plot(df["Price"], df["Profit"], label="Profit ($)", color="green")
ax1.set_xlabel("Company A Price ($)")
ax1.set_ylabel("Revenue / Profit ($)", color="black")
ax1.tick_params(axis='y', labelcolor="black")

# Plot sales volumes for all companies
ax2 = ax1.twinx()  # Instantiate another y-axis
ax2.plot(df["Price"], df["Sales A"], label="Sales A", color="red", linestyle="--")
ax2.plot(df["Price"], df["Sales B"], label="Sales B", color="orange", linestyle="--")
ax2.plot(df["Price"], df["Sales C"], label="Sales C", color="purple", linestyle="--")
ax2.set_ylabel("Sales Volume", color="black")
ax2.tick_params(axis='y', labelcolor="black")

# Legends
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

ax1.grid()

st.pyplot(fig)
