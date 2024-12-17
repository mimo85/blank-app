import streamlit as st

def light_control_page():
    st.header("Light Control")

    # Lamp 1
    st.subheader("Lamp 1")
    col1, col2 = st.columns([2, 1])

    with col1:
        st.image("pictures/lamp1.png", caption="Lamp 1")  # Replace with actual image URL
        power_1 = st.checkbox("Power On/Off", key="lamp1_power")
    with col2:
        intensity_1 = st.slider("Intensity (%)", min_value=0, max_value=100, value=60, key="lamp1_intensity")

    st.text(f"Lamp 1 Status: {'On' if power_1 else 'Off'} | Intensity: {intensity_1}%")

    # Lamp 2
    st.subheader("Lamp 2")
    col3, col4 = st.columns([2, 1])

    with col3:
        st.image("pictures/lamp2.png", caption="Lamp 2")  # Replace with actual image URL
        power_2 = st.checkbox("Power On/Off", key="lamp2_power")
    with col4:
        intensity_2 = st.slider("Intensity (%)", min_value=0, max_value=100, value=35, key="lamp2_intensity")

    st.text(f"Lamp 2 Status: {'On' if power_2 else 'Off'} | Intensity: {intensity_2}%")

    # Optional: Add action buttons for saving settings or controlling IoT devices
    if st.button("Save Settings"):
        st.success("Settings saved successfully!")
        # You can add the logic here to save or send control commands to the lamps (IoT integration)

# Use the function in your main app logic or wherever you handle navigation
