import streamlit as st

st.title("Competitive Pricing Reaction Simulator")
st.write("Adjust Company A's price and see how competitors react!")

# User input for Company A's price
company_a_price = st.slider("Set Company A's Price", min_value=50, max_value=500, value=100)

# Simple competitive reactions
company_b_price = company_a_price * 0.95  # 5% lower price
company_c_price = company_a_price * 1.05  # 5% higher price

st.write(f"Company B's response price: ${company_b_price:.2f}")
st.write(f"Company C's response price: ${company_c_price:.2f}")
