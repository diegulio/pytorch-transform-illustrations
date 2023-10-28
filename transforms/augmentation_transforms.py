import ast

import streamlit as st
from torchvision.transforms import v2
from utils import reload_button, show_results


def RandAugment(image):
    st.subheader("RandAugment")
    # Inputs
    n_ops = st.slider("Number of operations", 0, 5, 2)
    augmenter = v2.RandAugment(num_ops=n_ops)
    augmented_img = augmenter(image)
    show_results(image, augmented_img)
    code_augmenter = f"v2.RandAugment(num_ops={n_ops})"
    st.code(code_augmenter)
    reload_button("rand_augment")


def TrivialAugmentWide(image):
    st.subheader("TrivialAugmentWide")
    trivial_augmenter = v2.TrivialAugmentWide()
    trivial_augmented_img = trivial_augmenter(image)
    show_results(image, trivial_augmented_img)
    code_augmenter = f"v2.TrivialAugmentWide()"
    st.code(code_augmenter)
    reload_button("trivial_augment")


def AugMix(image):
    st.subheader("AugMix")
    # Inputs
    col1, col2 = st.columns(2)
    sev = col1.slider("Severity", 0, 10, 3)
    mix = col2.slider("Mixture Widht", 0, 10, 3)
    # Transform
    mix_augmenter = v2.AugMix(severity=sev, mixture_width=mix)
    mix_img = mix_augmenter(image)
    show_results(image, mix_img)
    code_mix = f"v2.AugMix(severity={sev}, mixture_width={mix})"
    st.code(code_mix)
    reload_button("aug_mix")
