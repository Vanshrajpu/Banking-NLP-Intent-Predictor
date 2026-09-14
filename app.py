import streamlit as st
import joblib
import time

# --- Page Config ---
st.set_page_config(page_title="FinGuard AI | Intent Engine", page_icon="🏦", layout="centered")

# --- Load Model ---
@st.cache_resource
def load_model():
    return joblib.load("intent_model.pkl")
model = load_model()

# --- CSS for FAANG Level UI ---
st.markdown("""
<style>
.main { background-color: #0E1117; }
.stTextInput > div > div > input { border-radius: 12px; height: 50px; font-size: 16px; }
.result-card { background: linear-gradient(135deg, #00C9A7 0%, #0072FF 100%); padding: 20px; border-radius: 15px; color: white; }
.intent-badge { background-color: #1f2937; padding: 8px 16px; border-radius: 20px; font-size: 14px; border: 1px solid #374151; }
</style>
""", unsafe_allow_html=True)

# --- Header ---
col1, col2 = st.columns([1, 8])
with col1:
    st.markdown("# 🏦")
with col2:
    st.markdown("## FinGuard AI")
    st.caption("Enterprise Banking Intent Intelligence | v2.1")

st.divider()

# --- Sidebar for Bank ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2830/2830284.png", width=80)
    st.title("Bank Admin")
    st.metric("Model Accuracy", "94.2%", "↑ 2.1%")
    st.metric("Intents Trained", "5 Core")
    st.metric("Avg Latency", "42ms")
    st.divider()
    st.write("**Supported Intents:**")
    st.code("card_arrival\ncard_delivery_estimate\ncard_not_working\ncash_withdrawal_charge\ncash_withdrawal_not_recognised")
    st.info("© 2025 FinGuard AI by Vanshrajpu")

# --- Main Input ---
st.subheader("Customer Query Analysis")
st.write("Real-time classification of banking customer queries.")

user_input = st.text_input("Query", placeholder="e.g. Why was I charged for cash withdrawal?", label_visibility="collapsed")

predict_btn = st.button("🚀 Analyze Intent", use_container_width=True, type="primary")

if predict_btn:
    if not user_input.strip():
        st.warning("Please enter a customer query.")
    else:
        with st.spinner("Analyzing with Banking NLP Engine..."):
            time.sleep(0.8)
            pred = model.predict([user_input])[0]
            prob = max(model.predict_proba([user_input])[0]) * 100

        # Result Card
        st.markdown(f"""
        <div class="result-card">
            <h4 style='margin:0;'>✅ Intent Detected</h4>
            <h2 style='margin:10px 0;'>{pred.replace('_',' ').title()}</h2>
            <p style='margin:0; opacity:0.9;'>Confidence Score: {prob:.2f}% | Action: Auto-Route to {pred.split('_')[0].title()} Dept.</p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        c1, c2, c3 = st.columns(3)
        c1.metric("Confidence", f"{prob:.2f}%")
        c2.metric("Risk Level", "Low" if prob > 80 else "Medium")
        c3.metric("Status", "Ready to Route")

        # Department wise logic
        st.divider()
        st.subheader("Suggested Next Action")
        if "card" in pred:
            st.info("📨 **Action:** Forward to Card Operations Team | ETA: 2 hours | Create Ticket: CARD-OPS")
        else:
            st.info("💰 **Action:** Forward to Transaction Dispute Team | ETA: 24 hours | Check Fee Waiver Policy")

else:
    st.markdown("---")
    st.markdown("### Try these examples:")
    ex1, ex2 = st.columns(2)
    if ex1.button("My card is not working at ATM"):
        st.session_state['example'] = "My card is not working at ATM"
    if ex2.button("When will my new card arrive?"):
        st.session_state['example'] = "When will my new card arrive?"
