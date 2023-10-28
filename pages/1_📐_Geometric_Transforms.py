import ast
import io

import streamlit as st
from PIL import Image
from torchvision.transforms import v2
from transforms.geometric_transforms import *

st.set_page_config(
    page_title="Geometric Transforms",
    page_icon="📐",
)

st.title("Geometric Transforms")

views = st.multiselect(
    "Select Transforms",
    [
        "All",
        "Pad",
        "Resize",
        "CenterCrop",
        "RandomPerspective",
        "RandomRotation",
        "RandomAffine",
        "RandomCrop",
        "RandomResizedCrop",
    ],
)

if "uploaded_file" in st.session_state:
    bytes_data = st.session_state["uploaded_file"]
    image = Image.open(io.BytesIO(bytes_data))
else:
    image = Image.open("statics/demo.jpeg")

if "All" in views:
    Pad(image)
    Resize(image)
    CenterCrop(image)
    RandomPerspective(image)
    RandomRotation(image)
    RandomAffine(image)
    RandomCrop(image)
    RandomResizedCrop(image)
else:
    # Pad
    if "Pad" in views:
        Pad(image)

    # Resize
    if "Resize" in views:
        Resize(image)

    # CenterCrop
    if "CenterCrop" in views:
        CenterCrop(image)

    # RandomPerspective
    if "RandomPerspective" in views:
        RandomPerspective(image)

    # RandomRotation
    if "RandomRotation" in views:
        RandomRotation(image)

    # RandomAffine
    if "RandomAffine" in views:
        RandomAffine(image)

    # Random Crop
    if "RandomCrop" in views:
        RandomCrop(image)

    # Random Resized Crop
    if "RandomResizedCrop" in views:
        RandomResizedCrop(image)
