import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("Global Economic Intelligence Dashboard")

# Load data
df = pd.read_csv("../data/cleaned_data.csv")

# Sidebar country selector
country = st.sidebar.selectbox(
    "Select Country",
    df["Country"].unique()
)

# Filter data
data = df[df["Country"] == country]
data = data.sort_values("Year")

# -------------------------------
# 1️⃣ Unemployment Trend
# -------------------------------
st.header("Unemployment Trend")

fig1, ax1 = plt.subplots()

ax1.plot(data["Year"], data["Unemployment_Rate_%"], marker="o")

ax1.set_title("Unemployment Trend - " + country)
ax1.set_xlabel("Year")
ax1.set_ylabel("Unemployment Rate (%)")

st.pyplot(fig1)

# -------------------------------
# 2️⃣ CO2 vs GDP
# -------------------------------
st.header("CO2 Emissions vs GDP")

fig2, ax2 = plt.subplots()

ax2.scatter(
    data["GDP_USD"] / 1e12,
    data["CO2_Emissions_metric_tons_per_capita"]
)

ax2.set_xlabel("GDP (Trillion USD)")
ax2.set_ylabel("CO2 Emissions (metric tons per capita)")
ax2.set_title("CO2 Emissions vs GDP - " + country)

st.pyplot(fig2)

# -------------------------------
# 3️⃣ Life Expectancy vs GDP
# -------------------------------
st.header("Life Expectancy vs GDP")

fig3, ax3 = plt.subplots()

ax3.scatter(
    data["GDP_USD"] / 1e12,
    data["Life_Expectancy"]
)

ax3.set_xlabel("GDP (Trillion USD)")
ax3.set_ylabel("Life Expectancy")
ax3.set_title("Life Expectancy vs GDP - " + country)

st.pyplot(fig3)