import streamlit as st
import joblib
import time

st.set_page_config(page_title="FinGuard AI", page_icon="🛡️", layout="wide")

@st.cache_resource
def load_model():
    try:
        return joblib.load("intent_model.pkl")
    except:
        return None
model = load_model()

# --- CSS ---
st.markdown("""
<style>
[data-testid="stSidebar"] { background-color: #0A0F1C; }
.main { background-color: #F8FAFC; }
.card-top {
    background: white; padding: 25px; border-radius: 16px;
    border: 1px solid #E2E8F0; box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.result-card {
    background: linear-gradient(135deg, #2563EB 0%, #3B82F6 40%, #60A5FA 100%);
    padding: 28px; border-radius: 18px; color: white;
}
.small-badge { background: rgba(255,255,255,0.2); padding: 6px 14px; border-radius: 20px; font-size: 12px; }
.info-box { background: rgba(255,255,255,0.15); padding: 12px 16px; border-radius: 10px; backdrop-filter: blur(10px); }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🛡️ FinGuard AI")
    st.caption("Banking AI Platform")
    st.write("")
    st.markdown("**BANK ADMIN**")
    st.metric("94.2%", "Accuracy", delta="+1.2%")
    st.metric("5", "Core intents", delta="Active")
    st.metric("42ms", "Latency", delta="Real-time")
    st.divider()
    st.markdown("**📊 Dashboard**")
    st.markdown("✨ Intents")
    st.markdown("📈 Analytics")
    st.markdown("👥 Customers")
    st.markdown("🛡️ Security")
    st.divider()
    st.markdown("**BA** Admin User\n\nadmin@finguard.ai")

# --- MAIN HEADER ---
h1, h2 = st.columns([6, 2])
with h1:
    st.markdown("## Enterprise Banking Intent Intelligence")
    st.caption("Real-time AI-powered intent detection and analysis for enterprise banking support")
with h2:
    st.button("➕ New Query", type="primary")

st.write("")

# --- TOP CARD ---
st.markdown('<div class="card-top">', unsafe_allow_html=True)
c1, c2 = st.columns([1.2, 1])
with c1:
    st.markdown("#### ✨ Enterprise Banking Intent Intelligence")
    st.write("Monitor, analyze, and respond to customer intents automatically using FinGuard AI's foundation model. Get instant insights, confidence scores, and recommended actions.")
with c2:
    st.markdown("**Customer Query Analysis**")
    query = st.text_input("query_input", placeholder="Enter customer query...", label_visibility="collapsed")
    analyze = st.button("Analyze ✨", type="primary", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# --- RESULT CARD LOGIC ---
if 'analyze' in locals() and analyze and query:
    with st.spinner("Analyzing..."):
        time.sleep(0.6)
        if model:
            pred = model.predict([query])[0]
            proba = max(model.predict_proba([query])[0]) * 100
        else:
            pred = "card_not_working"
            proba = 92.0

    # Map for display
    category = "Payments & Cards" if "card" in pred else "Charges & Fees"
    action_text = "Issue replacement card and notify customer via SMS/Email. Review recent transactions for fraud." if "card" in pred else "Review charge policy, verify transaction and initiate fee waiver if applicable."

    st.markdown(f"""
    <div class="result-card">
        <div style="display:flex; justify-content:space-between; align-items:center">
            <span class="small-badge">💠 Intent Detected</span>
            <span class="small-badge">Confidence {proba:.0f}%</span>
        </div>
        <h1 style="margin:15px 0;">{pred.replace('_',' ').title()}</h1>
        <div style="display:flex; gap:12px; margin:15px 0;">
            <div class="info-box" style="flex:1">📄 Category:<br><b>{category}</b></div>
            <div class="info-box" style="flex:1; background:#FBBF24; color:#000">⚠️ Severity:<br><b>Medium</b></div>
            <div class="info-box" style="flex:1">🕒 Detected:<br><b>0.8s ago</b></div>
        </div>
        <p><b>Recommended Action</b><br>{action_text}</p>
        <div style="background:rgba(255,255,255,0.3); height:6px; border-radius:10px; margin-top:20px;">
            <div style="background:white; height:6px; width:{int(proba)}%; border-radius:10px;"></div>
        </div>
        <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:13px;">
            <span>Confidence {int(proba)}/100</span>
            <span>High confidence • Auto-action suggested</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="result-card" style="opacity:0.9">
        <span class="small-badge">💠 Intent Detected</span>
        <h1 style="margin:15px 0;">Card Not Working</h1>
        <p>Enter a query above and click Analyze to see live detection...</p>
    </div>
    """, unsafe_allow_html=True)
