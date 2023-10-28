import ast
import io

import streamlit as st
from PIL import Image
from torchvision.transforms import v2
from transforms.augmentation_transforms import *

st.set_page_config(
    page_title="Augmentation Transforms",
    page_icon="🧠",
)

st.title("Augmentation Transforms")

views = st.multiselect(
    "Select a view", ["All", "RandAugment", "TrivialAugmentWide", "AugMix"]
)

if "uploaded_file" in st.session_state:
    bytes_data = st.session_state["uploaded_file"]
    image = Image.open(io.BytesIO(bytes_data))
else:
    image = Image.open("statics/demo.jpeg")

if "All" in views:
    RandAugment(image)
    TrivialAugmentWide(image)
    AugMix(image)
else:
    if "RandAugment" in views:
        RandAugment(image)
    if "TrivialAugmentWide" in views:
        TrivialAugmentWide(image)
    if "AugMix" in views:
        AugMix(image)
