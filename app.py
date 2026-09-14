import streamlit as st
import joblib, time

st.set_page_config(page_title="FinGuard AI", page_icon="🏦", layout="wide")
model = joblib.load("intent_model.pkl")

st.markdown("""
<style>
[data-testid="stSidebar"] { background-color: #0f172a; }
.stTextInput input { background-color: #1e293b!important; color: white!important; border: 1px solid #334155!important; border-radius: 10px!important;}
.result-card { background: linear-gradient(90deg, #06b6d4 0%, #3b82f6 100%); padding: 22px; border-radius: 16px; color: white; box-shadow: 0 10px 30px rgba(59,130,246,0.3); }
.metric-card { background: #1e293b; padding: 15px; border-radius: 12px; border: 1px solid #334155; }
</style>
""", unsafe_allow_html=True)

# Sidebar - same as yours is perfect
with st.sidebar:
    st.markdown("### 🏛️ Bank Admin")
    st.metric("Model Accuracy", "94.2%", "2.1%")
    st.metric("Intents Trained", "5 Core")
    st.metric("Avg Latency", "42ms", "-5ms")
    st.divider()
    st.caption("Supported Intents")
    st.code("card_arrival\ncard_delivery_estimate\ncard_not_working\ncash_withdrawal_charge\ncash_withdrawal_not_recognised", language="text")
    st.success("System: Online")

# Main
c1, c2 = st.columns([3,1])
with c1:
    st.title("FinGuard AI")
    st.caption("Enterprise Banking Intent Intelligence v2.1 | Built by Vanshrajpu")
with c2:
    st.write("")
    st.write("🟢 Live Engine")

st.divider()
st.subheader("Customer Query Analysis")
q = st.text_input("", placeholder="Type customer query here... e.g. My card is not working", key="q")

if st.button("Analyze Intent", type="primary", use_container_width=True):
    if q:
        with st.spinner("Running NLP engine..."):
            time.sleep(0.6)
            pred = model.predict([q])[0]
            prob = max(model.predict_proba([q])[0])*100

        st.markdown(f'<div class="result-card"><h4>✓ Intent Detected</h4><h1>{pred.replace("_"," ").title()}</h1><p>Confidence {prob:.2f}% | Auto-Route to {pred.split("_")[0].upper()} Dept</p></div>', unsafe_allow_html=True)

        st.write("")
        m1,m2,m3 = st.columns(3)
        m1.markdown(f'<div class="metric-card"><small>Confidence</small><h3>{prob:.2f}%</h3></div>', unsafe_allow_html=True)
        m2.markdown(f'<div class="metric-card"><small>Risk Level</small><h3>{"Low" if prob>75 else "Medium"}</h3></div>', unsafe_allow_html=True)
        m3.markdown(f'<div class="metric-card"><small>Status</small><h3>Ready to Route</h3></div>', unsafe_allow_html=True)

        st.write("")
        st.info(f"**Suggested Next Action:** Forward to {'Card Operations' if 'card' in pred else 'Transaction Dispute'} Team | ETA 2 Hours | Create Ticket: {pred.upper()}-OPS-2025")
        st.progress(int(prob))
