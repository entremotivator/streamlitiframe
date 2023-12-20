# main_app.py
import streamlit as st

def main():
    st.title("Main Streamlit App")
    st.write("This is the main Streamlit app.")

    # Settings
    st.sidebar.header("Embedding Settings")

    # Input for the URL of the Streamlit app to embed
    embedded_app_url = st.sidebar.text_input("Enter Streamlit App URL", "https://your-embedded-app-url")

    # Input for the width of the iframe
    iframe_width = st.sidebar.number_input("Enter Iframe Width", min_value=100, max_value=2000, value=800)

    # Input for the height of the iframe
    iframe_height = st.sidebar.number_input("Enter Iframe Height", min_value=100, max_value=2000, value=600)

    # Checkbox for allowing full-screen option
    allow_fullscreen = st.sidebar.checkbox("Allow Fullscreen", True)

    # 10 additional options
    option1 = st.sidebar.text_input("Option 1", "Default value 1")
    option2 = st.sidebar.selectbox("Option 2", ["Option A", "Option B", "Option C"])
    option3 = st.sidebar.slider("Option 3", 0.0, 10.0, 5.0)
    option4 = st.sidebar.radio("Option 4", ["Radio A", "Radio B", "Radio C"])
    option5 = st.sidebar.checkbox("Option 5", True)
    option6 = st.sidebar.number_input("Option 6", min_value=1, max_value=100, value=50)
    option7 = st.sidebar.date_input("Option 7", None)
    option8 = st.sidebar.time_input("Option 8", None)
    option9 = st.sidebar.color_picker("Option 9", "#00FF00")
    option10 = st.sidebar.file_uploader("Option 10", type=["csv", "xlsx"])

    # Create a responsive layout using columns
    col1, col2 = st.columns(2)

    # Display the iframe in the first column
    with col1:
        st.markdown(f'<iframe src="{embedded_app_url}" width="{iframe_width}" height="{iframe_height}" allowfullscreen="{allow_fullscreen}"></iframe>', unsafe_allow_html=True)

    # Display additional information or settings in the second column
    with col2:
        st.write(f"Option 1: {option1}")
        st.write(f"Option 2: {option2}")
        st.write(f"Option 3: {option3}")
        st.write(f"Option 4: {option4}")
        st.write(f"Option 5: {option5}")
        st.write(f"Option 6: {option6}")
        st.write(f"Option 7: {option7}")
        st.write(f"Option 8: {option8}")
        st.write(f"Option 9: {option9}")
        st.write(f"Option 10: {option10}")

if __name__ == "__main__":
    main()
