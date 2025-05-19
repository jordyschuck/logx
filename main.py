import streamlit as st
from helpers import init_db
from sections import addflight
from sections import viewlogs
from sections import stats

# Initialize the database
init_db()

# Set Streamlit app-wide settings
st.set_page_config(page_title="LogX - Pilot Logbook", layout="wide")

# Sidebar Navigation
st.sidebar.title("LogX Navigation")
PAGES = {
    "➕ Add Flight": addflight,
    "📒 View Logbook": viewlogs,
    "📊 Stats": stats,
}

selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
