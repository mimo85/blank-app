import streamlit as st

def login_page():
    # Create a two-column layout
    col1, col2 = st.columns([3, 2])

    # Left column: Image
    with col1:
        st.image(
            "/workspaces/blank-app/pictures/image.png",  # Replace with actual image path
            use_column_width=True,
            caption="Street Light Management System"
        )

    # Right column: Login form
    with col2:
        st.markdown("<h1 style='text-align: center;'>Hello</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>Street Light Management System</h3>", unsafe_allow_html=True)

        # User credentials (for demonstration purposes)
        valid_users = {"mimo": "123", "admin@example.com": "adminpass"}

        # Email input
        email = st.text_input("Please enter your account name", placeholder="example@example.com")

        # Password input
        password = st.text_input("Please enter your login password", type="password")

        # Remember password checkbox
        st.checkbox("Remember password")

        # Login button
        if st.button("Sign In"):
            if email in valid_users and valid_users[email] == password:
                st.session_state.logged_in = True
                st.session_state.page = "dashboard"  # Set the page to "dashboard"
            else:
                st.error("Invalid email or password.")
