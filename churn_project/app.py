import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Telco Churn Predictor", page_icon="📞", layout="centered")


@st.cache_resource
def load_model():
    return joblib.load("best_model.pkl")


model = load_model()

st.title("📞 Telco Customer Churn Predictor")
st.write("Enter the customer's details and click **Predict** to see whether the customer is at risk of leaving.")

# ---------------- Inputs ----------------
st.subheader("Account information")
c1, c2 = st.columns(2)
contract = c1.selectbox("Contract type", ["Month-to-month", "One year", "Two year"])
tenure = c2.slider("Tenure (months)", 0, 72, 12)
monthly = c1.number_input("Monthly charges ($)", 0.0, 200.0, 70.0, step=0.5)
default_total = float(round(monthly * tenure, 2))
total = c2.number_input("Total charges ($)", 0.0, 10000.0, default_total, step=10.0,
                        help="Defaults to monthly charges × tenure; change it if you know the real value.")
paperless = c1.selectbox("Paperless billing", ["Yes", "No"])
payment = c2.selectbox("Payment method", ["Electronic check", "Mailed check",
                                          "Bank transfer (automatic)", "Credit card (automatic)"])

st.subheader("Customer demographics")
c1, c2 = st.columns(2)
gender = c1.selectbox("Gender", ["Female", "Male"])
senior = c2.selectbox("Senior citizen", ["No", "Yes"])
partner = c1.selectbox("Has partner", ["Yes", "No"])
dependents = c2.selectbox("Has dependents", ["No", "Yes"])

st.subheader("Services")
c1, c2 = st.columns(2)
phone = c1.selectbox("Phone service", ["Yes", "No"])
if phone == "Yes":
    multiple = c2.selectbox("Multiple lines", ["No", "Yes"])
else:
    multiple = "No phone service"
    c2.selectbox("Multiple lines", ["No phone service"], disabled=True)

internet = c1.selectbox("Internet service", ["Fiber optic", "DSL", "No"])
if internet == "No":
    online_sec = online_bkp = device = tech = tv = movies = "No internet service"
    st.info("No internet service: the internet add-ons are set to 'No internet service'.")
else:
    d1, d2, d3 = st.columns(3)
    online_sec = d1.selectbox("Online security", ["No", "Yes"])
    online_bkp = d2.selectbox("Online backup", ["No", "Yes"])
    device = d3.selectbox("Device protection", ["No", "Yes"])
    tech = d1.selectbox("Tech support", ["No", "Yes"])
    tv = d2.selectbox("Streaming TV", ["No", "Yes"])
    movies = d3.selectbox("Streaming movies", ["No", "Yes"])

# ---------------- Predict ----------------
if st.button("Predict", type="primary", use_container_width=True):
    row = pd.DataFrame([{
        "gender": gender, "SeniorCitizen": 1 if senior == "Yes" else 0, "Partner": partner,
        "Dependents": dependents, "tenure": tenure, "PhoneService": phone, "MultipleLines": multiple,
        "InternetService": internet, "OnlineSecurity": online_sec, "OnlineBackup": online_bkp,
        "DeviceProtection": device, "TechSupport": tech, "StreamingTV": tv, "StreamingMovies": movies,
        "Contract": contract, "PaperlessBilling": paperless, "PaymentMethod": payment,
        "MonthlyCharges": monthly, "TotalCharges": total,
    }])
    pred = int(model.predict(row)[0])
    prob = float(model.predict_proba(row)[0, 1])

    if pred == 1:
        st.error("This customer is at risk of leaving ⚠️")
    else:
        st.success("This customer is likely to stay ✅")
    st.metric("Churn probability", f"{prob:.1%}")
    st.progress(min(max(prob, 0.0), 1.0))
