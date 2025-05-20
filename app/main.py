import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data  

st.set_page_config(page_title="Solar Farm Analysis Dashboard", layout="wide")

st.title("Solar Farm Analysis Dashboard")


st.sidebar.header("Filters")
country = st.sidebar.selectbox("Select Country", ["Benin", "Sierraleone", "Togo"])
metric = st.sidebar.selectbox("Select Metric", ["GHI", "DNI", "DHI", "Tamb"])  
date_range = st.sidebar.slider(
    "Select Date Range",
    min_value=pd.to_datetime("2023-01-01"),  
    max_value=pd.to_datetime("2023-12-31"),
    value=(pd.to_datetime("2023-01-01"), pd.to_datetime("2023-12-31")),
    format="YYYY-MM-DD"
)

df = load_data(country)

df["Timestamp"] = pd.to_datetime(df["Timestamp"])  # Ensure Timestamp is datetime
df_filtered = df[(df["Timestamp"] >= date_range[0]) & (df["Timestamp"] <= date_range[1])]

col1, col2 = st.columns(2)


with col1:
    st.subheader(f"{metric} Boxplot")
    fig, ax = plt.subplots()
    sns.boxplot(x="Country", y=metric, data=df_filtered)
    plt.title(f"{metric} Distribution for {country}")
    st.pyplot(fig)


with col2:
    st.subheader(f"Mean {metric} by Country")
    mean_data = df_filtered.groupby("Country")[metric].mean().reset_index()
    st.dataframe(mean_data.style.format({metric: "{:.2f}"}))


st.subheader(f"{metric} Time Series")
fig, ax = plt.subplots()
sns.lineplot(x="Timestamp", y=metric, data=df_filtered, ax=ax)
plt.xticks(rotation=45)
plt.title(f"{metric} Over Time in {country}")
st.pyplot(fig)


if st.checkbox("Show Raw Data"):
    st.subheader("Filtered Data")
    st.dataframe(df_filtered)