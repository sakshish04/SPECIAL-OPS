import streamlit as st

st.title("Reformers's Fintech Agent 🛡️")
st.write("If you see this, your dashboard is working!")

if st.button("Click to Simulate a Payment"):
    st.balloons()
    st.success("Payment Processed!")