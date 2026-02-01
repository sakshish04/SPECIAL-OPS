import streamlit as st
import time
from simulator import generate_payment_data
from brain import analyze_payment_failures

st.set_page_config(page_title="NEURAL COMMAND", layout="wide")

# Futuristic Header Styling
st.markdown("<h1 style='text-align: center; color: #00ff41;'>🛰️ NEURAL COMMAND: OPS CENTER</h1>", unsafe_allow_html=True)

if st.button("⚡ INITIALIZE LIVE INTERCEPTION"):
    # 1. OBSERVE
    with st.status("📡 Intercepting 75 Live Data Packets...", expanded=True) as status:
        df = generate_payment_data(n=75)
        st.dataframe(df, width="stretch", height=400)
        
        # 2. REASON
        status.update(label="🧠 Agent Analyzing Failure Diversification...", state="running")
        reasoning = analyze_payment_failures(df)
        
        time.sleep(1.5) # Simulated "Cognitive Processing" time
        st.subheader("🤖 Agent Reasoning & Hypothesis")
        st.info(reasoning)
        status.update(label="✅ Analysis Complete. Intervention Logic Primed.", state="complete")

    # 3. ACT
    st.divider()
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.metric("TOTAL ALERTS", "20", "CRITICAL")
        if "504" in reasoning:
            st.error("ACTION: REROUTING HDFC UPI → ICICI")
            
    with c2:
        st.metric("LATENCY AVG", f"{int(df['Latency_ms'].mean())}ms", "HIGH")
        if "Guardrail Triggered" in reasoning:
            st.warning("GUARDRAIL: MANUAL AUDIT REQUIRED")
            
    with c3:
        st.metric("SUCCESS RATE", f"{len(df[df['Status']=='Success'])}/75", "-26%")
        st.success("SYSTEM STATE: INTERVENED")

else:
    st.info("System Standby. Awaiting Signal.")