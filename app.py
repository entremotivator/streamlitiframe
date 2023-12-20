# advanced_main_app.py
import streamlit as st

def main():
    st.title("Advanced Embed Streamlit App")

    # Settings
    with st.sidebar.expander("Embedding Settings"):
        num_embedded_apps = st.number_input("Number of Embedded Apps", min_value=1, value=1)

        embedded_apps = []
        for i in range(num_embedded_apps):
            st.subheader(f"Embedded App {i+1}")
            app_url = st.text_input(f"App {i+1} URL", f"https://your-embedded-app-url-{i+1}")
            embedded_apps.append(app_url)

        iframe_width = st.slider("Select Iframe Width", min_value=100, max_value=2000, value=800)
        iframe_height = st.slider("Select Iframe Height", min_value=100, max_value=2000, value=600)
        allow_fullscreen = st.checkbox("Allow Fullscreen", True)

        # Dynamic theming
        st.sidebar.subheader("Dynamic Theming")
        dynamic_theme = st.sidebar.checkbox("Enable Dynamic Theme", False)
        if dynamic_theme:
            theme_color = st.sidebar.color_picker("Select Theme Color", "#3498db")
            st.markdown(f"""<style>
                            :root {{
                                --primary-color: {theme_color};
                            }}
                            </style>
                        """, unsafe_allow_html=True)

    # Light and Dark Mode
    dark_mode = st.sidebar.checkbox("Dark Mode", False)
    if dark_mode:
        st.markdown('<style>body {background-color: #333; color: #fff;}</style>', unsafe_allow_html=True)

    # Preview and Embed buttons
    if st.button("Preview", key="preview_button"):
        st.subheader("Embedded App Preview:")
        for i, app_url in enumerate(embedded_apps):
            preview_code = f'<iframe id="preview_iframe_{i}" src="{app_url}" width="{iframe_width}" height="{iframe_height}" allowfullscreen="{allow_fullscreen}"></iframe>'
            st.markdown(preview_code, unsafe_allow_html=True)

            # Dynamically update iframe using JavaScript
            st.script_runner(f"""
                document.getElementById('preview_iframe_{i}').src = "{app_url}";
                document.getElementById('preview_iframe_{i}').width = "{iframe_width}";
                document.getElementById('preview_iframe_{i}').height = "{iframe_height}";
                document.getElementById('preview_iframe_{i}').allowfullscreen = "{allow_fullscreen}";
            """)

    if st.button("Embed", key="embed_button"):
        # Create a responsive layout using columns
        col1, col2 = st.columns(2)

        # Display the iframes in columns
        for i, app_url in enumerate(embedded_apps):
            with col1 if i % 2 == 0 else col2:
                st.subheader(f"Embedded App {i+1}:")
                st.markdown(f'<iframe src="{app_url}" width="{iframe_width}" height="{iframe_height}" allowfullscreen="{allow_fullscreen}"></iframe>', unsafe_allow_html=True)

        # Display additional information or settings
        with st.expander("Settings Summary"):
            st.subheader("Embedded App Settings:")
            for i, app_url in enumerate(embedded_apps):
                st.write(f"App {i+1} URL: [{app_url}]({app_url})")

            st.write(f"Iframe Width: {iframe_width}")
            st.write(f"Iframe Height: {iframe_height}")
            st.write(f"Allow Fullscreen: {allow_fullscreen}")

            if dynamic_theme:
                st.subheader("Dynamic Theming:")
                st.write(f"Dynamic Theme Enabled with Color: {theme_color}")

            st.subheader("Appearance:")
            st.write(f"Dark Mode: {'Enabled' if dark_mode else 'Disabled'}")

if __name__ == "__main__":
    main()
