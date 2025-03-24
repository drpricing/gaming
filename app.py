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
