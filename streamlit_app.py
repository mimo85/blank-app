import streamlit as st
from Project.login import login_page
from Project.dashboard import dashboard_page

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"  # Default page is "login"

# Rerun logic for navigation
if st.session_state.page == "dashboard" and st.session_state.logged_in:
    dashboard_page()
elif st.session_state.page == "login":
    login_page()
