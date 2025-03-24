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
base_sales_a
