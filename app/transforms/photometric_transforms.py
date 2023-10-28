import ast

import streamlit as st
from torchvision.transforms import v2
from utils import reload_button, show_results


def GrayScale(image):
    st.subheader("GrayScale")
    # Transform
    gray_img = v2.Grayscale()(image)
    code_gray = "v2.Grayscale()"
    show_results(image, gray_img)
    st.code(code_gray)


def ColorJitter(image):
    st.subheader("ColorJitter")
    # Inputs
    col1, col2, col3, col4 = st.columns(4)
    bri = col1.slider("Brightness", 0.0, 1.0, 0.5, key="brightness")
    con = col2.slider("Contrast", 0.0, 1.0, 0.5, key="contrast")
    sat = col3.slider("Saturation", 0.0, 1.0, 0.5, key="saturation")
    hue = col4.slider("Hue", 0.0, 1.0, 0.3, key="hue")
    # Transform
    jitter = v2.ColorJitter(brightness=bri, contrast=con, saturation=sat, hue=hue)
    jitter_img = jitter(image)
    show_results(image, jitter_img)
    code_jitter = (
        f"v2.ColorJitter(brightness={bri}, contrast={con}, saturation={sat}, hue={hue})"
    )
    st.code(code_jitter)


def GaussianBlur(image):
    st.subheader("GaussianBlur")
    # Inputs
    col1, col2 = st.columns(2)
    kernel = col1.text_input("Provide a tuple with the kernel size", value="(5, 9)")
    sigma = col2.text_input("Provide a tuple with the sigma range", value="(0.1, 5)")
    try:
        kernel = ast.literal_eval(kernel)
        sigma = ast.literal_eval(sigma)
        blur = v2.GaussianBlur(kernel_size=kernel, sigma=sigma)
    except Exception as e:
        st.error(f"Please provide a valid tuple. Error: {e}")
        st.stop()
    # Transform
    blur_img = blur(image)
    show_results(image, blur_img)
    code_blur = f"v2.GaussianBlur(kernel_size={kernel}, sigma={sigma})"
    st.code(code_blur)
    reload_button()


def RandomInvert(image):
    st.subheader("RandomInvert")
    # Transform
    inverter = v2.RandomInvert()
    inv_img = inverter(image)
    show_results(image, inv_img)
    code_inv = "v2.RandomInvert()"
    st.code(code_inv)
    reload_button(key="random_invert")


def RandomPosterize(image):
    st.subheader("RandomPosterize")
    # Inputs
    bits = st.slider("Bits", 0, 8, 2)
    # Transform
    posterizer = v2.RandomPosterize(bits=2, p=1)
    posterized_img = posterizer(image)
    show_results(image, posterized_img)
    code_posterize = f"v2.RandomPosterize(bits={bits}, p = 1)"
    st.code(code_posterize)


def RandomSolarize(image):
    st.subheader("RandomSolarize")
    # Inputs
    threshold = st.slider("Threshold", 0, 255, 192)
    # Transform
    solarizer = v2.RandomSolarize(threshold=threshold, p=1)
    solarized_img = solarizer(image)
    show_results(image, solarized_img)
    code_solarize = f"v2.RandomSolarize(threshold={threshold}, p = 1)"
    st.code(code_solarize)


def RandomAdjustSharpness(image):
    st.subheader("RandomAdjustSharpness")
    # Inputs
    sharpness = st.slider("Sharpness", 0.0, 2.0, 2.0)
    # Transform
    sharpener = v2.RandomAdjustSharpness(sharpness_factor=sharpness, p=1)
    sharpened_img = sharpener(image)
    show_results(image, sharpened_img)
    code_sharpness = f"v2.RandomAdjustSharpness(sharpness_factor={sharpness}, p = 1)"
    st.code(code_sharpness)


def RandomAutocontrast(image):
    st.subheader("RandomAutocontrast")
    # Transform
    autocontrast = v2.RandomAutocontrast(p=1)
    autocontrast_img = autocontrast(image)
    show_results(image, autocontrast_img)
    code_autocontrast = "v2.RandomAutocontrast(p = 1)"
    st.code(code_autocontrast)


def RandomEqualize(image):
    st.subheader("RandomEqualize")
    # Transform
    equalizer = v2.RandomEqualize(p=1)
    equalized_img = equalizer(image)
    show_results(image, equalized_img)
    code_equalize = "v2.RandomEqualize(p = 1)"
    st.code(code_equalize)
