import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function for the dashboard page
def dashboard_page():
    # Sidebar Navigation
    with st.sidebar:
        st.markdown("<h2 style='text-align: center;'>👤 Johanna Doe</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>johanna@company.com</p>", unsafe_allow_html=True)
        st.image("/workspaces/blank-app/pictures/profile.png", width=150)  # Add user image path

        # Sidebar Navigation Items
        st.markdown("---")  # Separator line
        page = st.radio("Navigation", ["🏠 Home", "📊 Analytics", "💡 Lights", "⚙️ Settings"])

    # Display Header
    st.title("Energy Analytics Dashboard")

    # Main Dashboard Content
    if page == "🏠 Home":
        st.subheader("Welcome to the Home Page")
        st.write("Use the navigation menu to explore different sections.")
    elif page == "📊 Analytics":
        st.subheader("Energy Savings")

        # Circular progress data
        progress_data = [
            {"name": "Current Week", "value": 64, "color": "#66D1A6"},
            {"name": "Last Week", "value": 40, "color": "#FF6B6B"},
            {"name": "Last Month", "value": 90, "color": "#4A90E2"},
        ]

        # Columns layout for progress circles
        cols = st.columns(3)
        for i, col in enumerate(cols):
            with col:
                st.markdown(f"<h4 style='text-align: center;'>{progress_data[i]['name']}</h4>", unsafe_allow_html=True)
                option = {
                    "series": [
                        {
                            "type": "pie",
                            "radius": ["70%", "90%"],
                            "data": [
                                {
                                    "value": progress_data[i]['value'],
                                    "name": f"{progress_data[i]['value']}%",
                                    "itemStyle": {"color": progress_data[i]['color']},
                                },
                                {
                                    "value": 100 - progress_data[i]['value'],
                                    "name": "",
                                    "itemStyle": {"color": "#EDEDED"},
                                },
                            ],
                            "label": {
                                "show": True,
                                "position": "center",
                                "formatter": f"{progress_data[i]['value']}%",
                                "fontSize": 18,
                                "fontWeight": "bold",
                                "color": progress_data[i]['color'],
                            },
                        }
                    ]
                }
                st_echarts(option, height="200px")

        st.subheader("Total Electricity Consumption")
        consumption_data = {
            'Day': [f"Day {i+1}" for i in range(10)],
            'Usage': [np.random.randint(50, 150) for _ in range(10)],
        }
        df = pd.DataFrame(consumption_data)

        # Highlight usage > 100 with red bars
        colors = ['red' if usage > 100 else 'gray' for usage in df['Usage']]

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(df['Day'], df['Usage'], color=colors)
        ax.set_xlabel("Days")
        ax.set_ylabel("Electricity Usage (kWh)")
        ax.set_title("Daily Electricity Consumption")
        st.pyplot(fig)

        st.subheader("Today's Weather")
        col4, col5 = st.columns(2)

        with col4:
         st.markdown("☀️ **Sunny**")
        with col5:
         st.markdown("⛈️ **Stormy**")

    elif page == "💡 Lights":
        st.subheader("Lights Management")
        st.write("This section will manage street lights.")
    elif page == "⚙️ Settings":
        st.subheader("Settings")
        st.write("Update your preferences and profile here.")

