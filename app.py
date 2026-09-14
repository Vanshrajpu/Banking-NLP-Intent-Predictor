import streamlit as st
import joblib

# model load
model = joblib.load("intent_model.pkl")

st.set_page_config(page_title="Banking Intent Classifier", page_icon="🏦")
st.title("🏦 Banking Intent Classifier")
st.caption("powered by Vanshrajpu | 94% Accuracy")

st.divider()

user_input = st.text_input("Apna banking query likho:", placeholder="e.g. My card is not working")

if st.button("Predict Intent"):
    if user_input.strip() == "":
        st.warning("Pehle kuch likh to sahi!")
    else:
        prediction = model.predict([user_input])[0]
        proba = max(model.predict_proba([user_input])[0]) * 100

        st.success(f"**Intent:** {prediction}")
        st.progress(int(proba))
        st.write(f"Confidence: {proba:.2f}%")

        # Intent ke hisab se colour
        if prediction == "card_not_working":
            st.error("Lagta hai card issue hai - Support se contact karo")
        elif prediction == "card_arrival":
            st.info("Card arrival ka status check ho raha hai...")

st.divider()
st.markdown("**Model trained on Banking77 dataset - 5 intents**")
