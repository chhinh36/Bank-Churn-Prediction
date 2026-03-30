import streamlit as st
import pandas as pd
import joblib
import os
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Bank Churn Prediction",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# LOAD FILES
# =========================
app_dir = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(app_dir, 'model.pkl'))
features = joblib.load(os.path.join(app_dir, 'features.pkl'))
threshold = joblib.load(os.path.join(app_dir, 'threshold.pkl'))

# =========================
# HEADER
# =========================
st.title("🏦 Bank Customer Churn Prediction")
st.markdown("Predict whether a customer will leave the bank based on key attributes.")
st.divider()

# =========================
# SIDEBAR (OPTIONAL CLEAN INFO)
# =========================
st.sidebar.title("ℹ About App")
st.sidebar.info("This app uses Machine Learning to predict customer churn probability.")

# =========================
# INPUT SECTION
# =========================
st.subheader("🧾 Customer Information")

col1, col2, col3 = st.columns(3)

with col1:
    CreditScore = st.number_input("Credit Score", 300, 900, 600)
    Age = st.number_input("Age", 18, 100, 35)
    Tenure = st.number_input("Tenure", 0, 10, 5)

with col2:
    Balance = st.number_input("Balance", 0.0, 300000.0, 50000.0)
    NumOfProducts = st.number_input("Num Of Products", 1, 4, 1)
    EstimatedSalary = st.number_input("Estimated Salary", 0.0, 200000.0, 50000.0)

with col3:
    HasCrCard = st.selectbox("Has Credit Card", [0, 1])
    IsActiveMember = st.selectbox("Is Active Member", [0, 1])
    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", ["Male", "Female"])

st.divider()

# =========================
# PREDICT BUTTON
# =========================
if st.button("🚀 Predict Churn"):

    # ------------------------
    # CREATE INPUT DATA
    # ------------------------
    data = pd.DataFrame([{
        'CreditScore': CreditScore,
        'Age': Age,
        'Tenure': Tenure,
        'Balance': Balance,
        'NumOfProducts': NumOfProducts,
        'HasCrCard': HasCrCard,
        'IsActiveMember': IsActiveMember,
        'EstimatedSalary': EstimatedSalary,
        'Geography': geography,
        'Gender': gender
    }])

    # ------------------------
    # ONE HOT ENCODING
    # ------------------------
    data = pd.get_dummies(data, columns=['Geography', 'Gender'], drop_first=False)

    # ------------------------
    # ALIGN FEATURES
    # ------------------------
    data = data.reindex(columns=features, fill_value=0)

    # ------------------------
    # PREDICTION
    # ------------------------
    prob = float(model.predict_proba(data)[:, 1][0])
    pred = int(prob > threshold)

    # =========================
    # RESULT UI (IMPROVED)
    # =========================
    st.subheader("📊 Prediction Result")

    # Display metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Churn Probability", f"{prob:.2%}")

    with col2:
        st.metric("Threshold", f"{threshold:.2f}")
    
    with col3:
        risk_level = "HIGH RISK" if pred == 1 else "LOW RISK"
        st.metric("Risk Level", risk_level)

    st.divider()

    # Visualization: Gauge Chart and Pie Chart
    st.write("---")
    st.subheader("📈 Visualizations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Churn Probability Gauge**")
        try:
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=prob * 100,
                title={'text': "Churn Risk %"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "#ef553b" if pred == 1 else "#00cc96"},
                    'steps': [
                        {'range': [0, 25], 'color': "#e8f5e9"},
                        {'range': [25, 50], 'color': "#fff9c4"},
                        {'range': [50, 75], 'color': "#ffe0b2"},
                        {'range': [75, 100], 'color': "#ffcdd2"}
                    ]
                }
            ))
            fig_gauge.update_layout(height=350, margin=dict(l=10, r=10, t=30, b=10))
            st.plotly_chart(fig_gauge, use_container_width=True)
        except Exception as e:
            st.error(f"Error displaying gauge: {e}")
    
    with col2:
        st.write("**Risk Distribution**")
        try:
            fig_pie = go.Figure(data=[go.Pie(
                labels=['Churn Risk', 'Retention Risk'],
                values=[prob * 100, (1 - prob) * 100],
                marker=dict(colors=['#ef553b', '#00cc96']),
                textinfo='label+percent',
                hoverinfo='label+percent'
            )])
            fig_pie.update_layout(height=350, margin=dict(l=10, r=10, t=30, b=10))
            st.plotly_chart(fig_pie, use_container_width=True)
        except Exception as e:
            st.error(f"Error displaying pie chart: {e}")

    st.divider()

    # Status Message
    if pred == 1:
        st.error("⚠ Customer is HIGH RISK of Churn")
        st.warning("Recommended action: Offer retention strategy")
    else:
        st.success("✔ Customer is LOW RISK of Churn")
        st.info("Customer is likely to stay")

    # Progress bar
    st.write("**Churn Probability Meter**")
    st.progress(min(prob, 1.0))
    
    # Customer Profile Summary
    st.write("**Customer Profile Summary**")
    summary_df = pd.DataFrame({
        'Attribute': ['Credit Score', 'Age', 'Tenure', 'Balance', 'Num Products', 'Active Member', 'Has Credit Card'],
        'Value': [CreditScore, Age, Tenure, f"${Balance:,.0f}", NumOfProducts, "Yes" if IsActiveMember else "No", "Yes" if HasCrCard else "No"]
    })
    st.dataframe(summary_df, use_container_width=True, hide_index=True)