import streamlit as st
import pickle
model = pickle.load(open("anomaly_model.pkl", "rb"))
def extract_features(text):
    if len(text) > 5:
        speed = len(text) / (len(text) * 0.25)  
        pressure = 0.8 if "a" in text else 0.3  
        return [speed, pressure]
    return None
st.title("💡 B-SAFE: Behavior-Based Banking Security")

st.markdown("### Step 1: Type the phrase to simulate behavior")
typed = st.text_input("Type exactly this phrase: `secure banking`")

if typed:
    features = extract_features(typed)
    if features:
        prediction = model.predict([features])[0]

        if prediction == 0:
            st.success("✅ Behavior Detected: Genuine User")

            if st.button("Transfer ₹1000"):
                st.success("💰 Transaction Successful!")
        else:
            st.error("🚨 Suspicious Behavior Detected!")
            st.warning("🔐 Transaction Blocked. Please re-authenticate.")
    else:
        st.info("ℹ️ Keep typing to capture your behavior.")
