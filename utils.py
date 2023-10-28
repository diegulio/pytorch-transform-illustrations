import streamlit as st


def reload_button(key="reload"):
    """Rerun the whole app."""
    button = st.button("Re Run", key=key)
    if button:
        st.rerun()


def show_results(image, transformed_image):
    col1, col2 = st.columns(2)
    col1.image(image)
    col2.image(transformed_image)
