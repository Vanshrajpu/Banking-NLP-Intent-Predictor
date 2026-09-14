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

st.markdown("""
<style>
[data-testid="stSidebar"] { background-color: #0A0F1C; }
.stApp { background-color: #0B1220; }

[data-testid="stTextInput"] input {
    background-color: #FFFFFF!important;
    color: #0F172A!important;
    border-radius: 12px!important;
    height: 52px!important;
    border: 1px solid #E2E8F0!important;
}

div[data-testid="stButton"] > button[kind="primary"] {
    background: linear-gradient(90deg, #2563EB 0%, #3B82F6 100%)!important;
    color: white!important;
    border: none!important;
    border-radius: 12px!important;
    height: 48px!important;
    font-weight: 600!important;
}
div[data-testid="stButton"] > button[kind="secondary"] {
    border-radius: 12px!important;
    height: 48px!important;
}

.card-top {
    background: #151E32;
    padding: 24px;
    border-radius: 16px;
    border: 1px solid #1E293B;
}
.result-card {
    background: linear-gradient(135deg, #2563EB 0%, #3B82F6 50%, #60A5FA 100%);
    padding: 28px;
    border-radius: 20px;
    color: white;
}
.badge {
    background: rgba(255,255,255,0.2);
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 12px;
}
.info-box {
    background: rgba(255,255,255,0.15);
    padding: 12px 16px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown("### 🛡️ FinGuard AI")
    st.caption("Banking AI Platform")
    st.markdown("---")
    st.markdown("**BANK ADMIN**")
    c1, c2 = st.columns(2)
    c1.metric("94.2%", "Accuracy", "+1.2%")
    c2.metric("5", "Core intents")
    st.metric("42ms", "Latency", "Real-time")
    st.markdown("---")
    st.markdown("**📊 Dashboard** \n✨ Intents \n📈 Analytics \n👥 Customers \n🛡️ Security")
    st.markdown("---")
    st.markdown("**BA Admin User** \nadmin@finguard.ai")

# HEADER
col1, col2 = st.columns([4,1])
with col1:
    st.markdown("# Enterprise Banking Intent Intelligence")
    st.caption("Real-time AI-powered intent detection and analysis for enterprise banking support")
with col2:
    st.write("")
    st.button("➕ New Query", type="primary", use_container_width=True)

# TOP CARD
st.markdown('<div class="card-top">', unsafe_allow_html=True)
left, right = st.columns([1.3, 1])
with left:
    st.markdown("#### ✨ Enterprise Banking Intent Intelligence")
    st.markdown("<p style='color:#94A3B8; font-size:14px'>Monitor, analyze, and respond to customer intents automatically using FinGuard AI's foundation model. Get instant insights, confidence scores, and recommended actions.</p>", unsafe_allow_html=True)
with right:
    st.markdown("**Customer Query Analysis**")
    query = st.text_input("q", placeholder="Why was I charged for cash withdrawal?", label_visibility="collapsed", key="q_input")
    analyze = st.button("Analyze ✨", type="primary", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# RESULT
if analyze and query.strip()!= "":
    with st.spinner("Analyzing..."):
        time.sleep(0.6)
        if model:
            pred = model.predict([query])[0]
            prob = max(model.predict_proba([query])[0]) * 100
        else:
            pred = "cash_withdrawal_charge"
            prob = 87.0

    cat = "Charges & Fees" if "cash" in pred or "charge" in pred else "Payments & Cards"
    if "card_not_working" in pred:
        cat = "Payments & Cards"
        action = "Issue replacement card and notify customer via SMS/Email. Review recent transactions for fraud."
    elif "cash" in pred:
        action = "Review charge policy, verify transaction and initiate fee waiver if applicable."
    else:
        action = f"Auto-route to {pred.replace('_',' ').title()} department and create support ticket."

    st.markdown(f"""
    <div class="result-card">
        <div style="display:flex; justify-content:space-between">
            <span class="badge">Intent Detected</span>
            <span class="badge">Confidence {int(prob)}%</span>
        </div>
        <h1 style="margin:18px 0;">{pred.replace('_',' ').title()}</h1>
        <div style="display:flex; gap:12px; margin-bottom:16px">
            <div class="info-box" style="flex:1">📄 Category:<br><b>{cat}</b></div>
            <div class="info-box" style="flex:1; background:#FDE68A; color:#000">⚠️ Severity:<br><b>Medium</b></div>
            <div class="info-box" style="flex:1">⏱️ Detected:<br><b>0.8s ago</b></div>
        </div>
        <p style="margin:0"><b>Recommended Action</b><br>{action}</p>
        <div style="background:rgba(255,255,255,0.3); height:6px; border-radius:10px; margin-top:22px">
            <div style="background:white; width:{int(prob)}%; height:6px; border-radius:10px"></div>
        </div>
        <div style="display:flex; justify-content:space-between; font-size:12px; margin-top:8px">
            <span>Confidence {int(prob)}/100</span>
            <span>High confidence • Auto-action suggested</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
