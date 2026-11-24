import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Hospital Analytics Dashboard",
    page_icon="🏥",
    layout="wide"
)
st.title("🏥 Hospital Patient Analytics Dashboard")
st.write("Welcome to Hospital Data Analysis")
# Load Dataset
df = pd.read_csv("hospital_data.csv")
# Sidebar Filters
st.sidebar.title("Dashboard Filters")
department = st.sidebar.multiselect(
    "Select Department",
    options=df["Department"].unique(),
    default=df["Department"].unique()
)
gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)
# Filter Data
filtered_df = df[
    (df["Department"].isin(department)) &
    (df["Gender"].isin(gender))
]
# Key Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Patients", len(filtered_df))
col2.metric("Average Age", round(filtered_df["Age"].mean(), 1))
col3.metric("Treatment Cost", 
            f"₹{filtered_df['Treatment_Cost'].sum():,.0f}")
col4.metric("Recovery Rate",
            f"{filtered_df['Recovery_Rate'].mean():.1f}%")
st.divider()
# Department Analysis
st.subheader("Department-wise Patient Analysis")
fig1 = px.bar(
    filtered_df["Department"].value_counts().reset_index(),
    x="Department",
    y="count",
    color="Department",
    title="Patients by Department"
)
st.plotly_chart(fig1, use_container_width=True)
# Disease Distribution
st.subheader("Disease Distribution")
fig2 = px.pie(
    filtered_df,
    names="Disease",
    title="Patient Disease Distribution"
)
st.plotly_chart(fig2, use_container_width=True)
# Gender Distribution
st.subheader("Gender Distribution")
fig3 = px.histogram(
    filtered_df,
    x="Gender",
    color="Gender",
    title="Male vs Female Patients"
)
st.plotly_chart(fig3, use_container_width=True)
# Data Table
st.subheader("Hospital Patient Records")
st.dataframe(filtered_df, use_container_width=True)
