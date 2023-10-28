import io

import streamlit as st
from PIL import Image
from transforms.photometric_transforms import *

st.set_page_config(
    page_title="Photometric Transforms",
    page_icon="🌄",
)

st.title("Photometric Transforms")

views = st.multiselect(
    "Select a view",
    [
        "All",
        "GrayScale",
        "ColorJitter",
        "GaussianBlur",
        "RandomInvert",
        "RandomPosterize",
        "RandomSolarize",
        "RandomAdjustSharpness",
        "RandomAutocontrast",
        "RandomEqualize",
    ],
)

if "uploaded_file" in st.session_state:
    bytes_data = st.session_state["uploaded_file"]
    image = Image.open(io.BytesIO(bytes_data))
else:
    image = Image.open("statics/demo.jpeg")

if "All" in views:
    GrayScale(image)
    ColorJitter(image)
    GaussianBlur(image)
    RandomInvert(image)
    RandomPosterize(image)
    RandomSolarize(image)
    RandomAdjustSharpness(image)
    RandomAutocontrast(image)
    RandomEqualize(image)
else:
    if "GrayScale" in views:
        GrayScale(image)
    if "ColorJitter" in views:
        ColorJitter(image)
    if "GaussianBlur" in views:
        GaussianBlur(image)
    if "RandomInvert" in views:
        RandomInvert(image)
    if "RandomPosterize" in views:
        RandomPosterize(image)
    if "RandomSolarize" in views:
        RandomSolarize(image)
    if "RandomAdjustSharpness" in views:
        RandomAdjustSharpness(image)
    if "RandomAutocontrast" in views:
        RandomAutocontrast(image)
    if "RandomEqualize" in views:
        RandomEqualize(image)
