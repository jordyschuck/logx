import streamlit as st
import pandas as pd
from helpers import getAllFlights
import matplotlib.pyplot as plt

def app():
    st.title("Your stats")
    df = getAllFlights()

    if df.empty:
        st.warning("No Flights in the System Found")
        return
    
    st.subheader("Summary")
    totals = {
        "Total Hours": df["totaltime"].sum(),
        "PIC": df["pic"].sum(),
        "SIC": df["sic"].sum(),
        "Night": df["night"].sum(),
        "IMC (Real + Sim)": df["hoodsim"].sum() + df["hardimc"].sum(),
        "Approaches": df["approaches"].sum(),
        "Landings": df["alllandings"].sum(),
        "Tails Flown": df["tail"].nunique()
    }
    st.json(totals)

    if st.button("Export as CSV"):
        pd.DataFrame([totals]).to_csv("data/summary.csv")

    df['date'] = pd.to_datetime(df['date'])
    timeByMonth = df.groupby(df['date'].dt.to_period("M"))['totaltime'].sum()

    st.subheader("Hours Per Month")
    st.line_chart(timeByMonth)

    timePerReg = df.groupby('tail')['totaltime'].sum().sort_values(ascending=False)
    st.subheader("Hours by Registration")
    st.bar_chart(timePerReg)