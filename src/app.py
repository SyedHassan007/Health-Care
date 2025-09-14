import streamlit as st
import pandas as pd
import plotly.express as px
from kpis import calculate_business_kpis, calculate_patient_kpis

# Page configuration
st.set_page_config(
    page_title="Healthcare Analytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏥 Healthcare Analytics Dashboard")
st.markdown("### An interactive tool for analyzing hospital performance and patient experience.")

# Load processed data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/processed/healthcare_processed_data.csv", parse_dates=['date'])
        return df
    except FileNotFoundError:
        st.error("Processed data file not found. Please run the ETL script first.")
        return pd.DataFrame()

df_raw = load_data()

if not df_raw.empty:
    # Create tabs
    tab1, tab2 = st.tabs(["📊 Hospital Insights", "🫂 Patient Insights"])

    with tab1:
        st.header("Hospital Insights")
        st.markdown("Metrics for healthcare administrators and policymakers.")

        biz_kpis = calculate_business_kpis(df_raw)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Bed Occupancy Rate", f"{biz_kpis['avg_occupancy']:.2f}%")
        with col2:
            st.metric("Avg. Length of Stay", f"{biz_kpis['avg_alos']:.2f} days")
        with col3:
            st.metric("Readmission Rate", f"{biz_kpis['readmission_rate']:.2f}%")
        with col4:
            st.metric("Avg. ER Wait Time", f"{biz_kpis['avg_er_wait_time']:.2f} hours")
        
        st.subheader("Monthly Admissions Trend")
        fig_admissions = px.line(
            biz_kpis['monthly_admissions'],
            x='date',
            y='Admissions',
            title='Monthly Patient Admissions'
        )
        st.plotly_chart(fig_admissions, use_container_width=True)
        
        st.subheader("Departmental Performance")
        fig_dept_rev = px.bar(
            biz_kpis['dept_performance'],
            x='department',
            y='total_revenue',
            title='Total Revenue by Department'
        )
        st.plotly_chart(fig_dept_rev, use_container_width=True)

    with tab2:
        st.header("Patient Insights")
        st.markdown("Metrics for patients and their families to make informed decisions.")

        patient_kpis = calculate_patient_kpis(df_raw)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Avg. Satisfaction Score", f"{patient_kpis['avg_satisfaction_score']:.2f} / 5.0")
        with col2:
            st.metric("Avg. Out-of-Pocket Cost", f"${patient_kpis['avg_out_of_pocket']:.2f}")
        with col3:
            st.metric("Insurance Coverage", f"{patient_kpis['avg_insurance_coverage']:.2f}%")

        st.subheader("Average Treatment Cost per Condition")
        fig_cost_condition = px.bar(
            patient_kpis['avg_cost_per_condition'],
            x='Condition',
            y='Average Revenue',
            title='Average Cost per Condition'
        )
        st.plotly_chart(fig_cost_condition, use_container_width=True)