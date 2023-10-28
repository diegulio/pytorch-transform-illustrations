import ast

import streamlit as st
from torchvision.transforms import v2
from utils import reload_button, show_results


def Pad(image):
    st.subheader("Pad")
    # Inputs
    sequence = st.checkbox("Use padding sequence")
    fill_value = st.color_picker("Pick A fill color", "#000000").strip("#")
    fill_rgb = tuple(int(fill_value[i : i + 2], 16) for i in (0, 2, 4))

    if sequence:  # If want to insert sequence
        sequence = st.text_input("Provide sequence as a list", value=[30, 30, 30, 30])
        try:
            pad_list = ast.literal_eval(sequence)
            if len(pad_list) != 4 and len(pad_list) != 2:
                raise Exception("Please provide a valid list of length 4 or 2")

            padded_img = v2.Pad(padding=pad_list, fill=fill_rgb)(image)
            pad_code = f"v2.Pad(padding={pad_list}, fill = {fill_rgb})"

        except Exception as e:
            st.error(f"Please provide a valid list. Error: {e}")
    else:
        pad = st.slider("Pick a pad", 0, 1000)
        padded_img = v2.Pad(padding=pad, fill=fill_rgb)(image)
        pad_code = f"v2.Pad(padding={pad}, fill = {fill_rgb})"

    # Show
    col1, col2 = st.columns(2)
    col1.image(image)
    col2.image(padded_img)
    st.code(pad_code)


def Resize(image):
    st.subheader("Resize")
    size = st.text_input("Provide a tuple with the new size", value="(224, 224)")
    try:
        new_size = ast.literal_eval(size)
        image_resized = v2.Resize(size=new_size)(image)
    except Exception as e:
        st.error(f"Please provide a valid tuple. Error: {e}")
        st.stop()
    resized_code = f"v2.Resize(size={new_size})"
    # Show
    col1, col2 = st.columns(2)
    col1.image(image)
    col2.image(image_resized)
    st.code(resized_code)


def CenterCrop(image):
    st.subheader("CenterCrop")
    cc_size = st.text_input("Provide a tuple with the new size", value="(50, 50)")
    try:
        cc_size = ast.literal_eval(cc_size)
        cropped_image = v2.CenterCrop(size=cc_size)(image)
    except Exception as e:
        st.error(f"Please provide a valid tuple. Error: {e}")
        st.stop()
    cropped_code = f"v2.CenterCrop(size={cc_size})"
    # Show
    col1, col2 = st.columns(2)
    col1.image(image)
    col2.image(cropped_image)
    st.code(cropped_code)


def RandomPerspective(image):
    st.subheader("RandomPerspective")
    # Inputs
    col1, col2, col3 = st.columns(3)
    dist_fill_value = col1.color_picker(
        "Pick A fill color", "#000000", key="perspective"
    ).strip("#")
    pers_fill_rgb = tuple(int(dist_fill_value[i : i + 2], 16) for i in (0, 2, 4))
    distortion_scale = col2.slider(
        "Distortion Scale", min_value=0.0, max_value=1.0, value=0.6
    )
    distortion_p = col3.slider(
        "Distortion Probability", min_value=0.0, max_value=1.0, value=1.0
    )
    # Transform
    perspective_transformer = v2.RandomPerspective(
        distortion_scale=distortion_scale, p=distortion_p, fill=pers_fill_rgb
    )
    perspective_code = f"v2.RandomPerspective(distortion_scale={distortion_scale}, p={distortion_p}, fill={pers_fill_rgb})"
    image_perspective = perspective_transformer(image)
    # Show
    col1, col2 = st.columns(2)
    col1.image(image)
    col2.image(image_perspective)
    st.code(perspective_code)
    reload_button("random_perspective")


def RandomRotation(image):
    st.subheader("RandomRotation")
    # Inputs
    col1, col2, col3 = st.columns(3)
    rot_fill_value = col1.color_picker(
        "Pick A fill color", "#000000", key="rotation"
    ).strip("#")
    rot_fill_rgb = tuple(int(rot_fill_value[i : i + 2], 16) for i in (0, 2, 4))
    min_degree = col2.slider("Min Degree", min_value=0, max_value=180, value=0)
    max_degree = col3.slider("Max Degree", min_value=0, max_value=180, value=180)
    if min_degree > max_degree:
        st.error("Min Degree cannot be greater than Max Degree")
        st.stop()
    # Transform
    rotater = v2.RandomRotation(degrees=(min_degree, max_degree), fill=rot_fill_rgb)
    image_rotated = rotater(image)
    rotation_code = (
        f"v2.RandomRotation(degrees=({min_degree}, {max_degree}), fill={rot_fill_rgb})"
    )
    # Show
    col1, col2 = st.columns(2)
    col1.image(image)
    col2.image(image_rotated)
    st.code(rotation_code)
    reload_button("random_rotation")


def RandomAffine(image):
    st.subheader("RandomAffine")
    # Inputs
    col1, col2, col3 = st.columns(3)
    aff_fill_value = col1.color_picker(
        "Pick A fill color", "#000000", key="affine"
    ).strip("#")
    aff_fill_rgb = tuple(int(aff_fill_value[i : i + 2], 16) for i in (0, 2, 4))
    min_degree_aff = col2.slider(
        "Min Degree", min_value=0, max_value=360, value=0, key="min_affine"
    )
    max_degree_aff = col3.slider(
        "Max Degree", min_value=0, max_value=360, value=180, key="max_affine"
    )

    col1, col2 = st.columns(2)
    translate_min = col1.slider(
        "Min Translation", min_value=0.0, max_value=1.0, value=0.1, key="min_trans"
    )
    translate_max = col2.slider(
        "Max Translation", min_value=0.0, max_value=1.0, value=0.3, key="max_trans"
    )

    col1, col2 = st.columns(2)
    scale_min = col1.slider(
        "Min Scale", min_value=0.0, max_value=1.0, value=0.5, key="min_scale"
    )
    scale_max = col2.slider(
        "Max Scale", min_value=0.0, max_value=1.0, value=0.75, key="max_scale"
    )

    # Transform
    affine_transfomer = v2.RandomAffine(
        degrees=(min_degree_aff, max_degree_aff),
        translate=(translate_min, translate_max),
        scale=(scale_min, scale_max),
        fill=aff_fill_rgb,
    )
    image_affine = affine_transfomer(image)
    affine_code = f"v2.RandomAffine(degrees=({min_degree_aff}, {max_degree_aff}), translate=({translate_min}, {translate_max}), scale=({scale_min}, {scale_max}), fill={aff_fill_rgb})"
    # Show
    col1, col2 = st.columns(2)
    col1.image(image)
    col2.image(image_affine)
    st.code(affine_code)
    reload_button("random_affine")


def RandomCrop(image):
    st.subheader("RandomCrop")
    # Inputs
    r_cc_size = st.text_input(
        "Provide a tuple with the new size", value="(50, 50)", key="r_cc_size"
    )
    try:
        r_cc_size = ast.literal_eval(r_cc_size)
        # Transform
        cropper = v2.RandomCrop(size=r_cc_size)
    except Exception as e:
        st.error(f"Please provide a valid tuple. Error: {e}")
        st.stop()
    r_cropped_image = cropper(image)
    r_crop_code = f"v2.RandomCrop(size={r_cc_size})"
    # Show
    col1, col2 = st.columns(2)
    col1.image(image)
    col2.image(r_cropped_image)
    st.code(r_crop_code)
    reload_button("random_crop")


def RandomResizedCrop(image):
    st.subheader("RandomResizedCrop")
    # Inputs
    r_rs_size = st.text_input(
        "Provide a tuple with the new size", value="(50, 50)", key="r_rs_size"
    )
    r_rs_size = ast.literal_eval(r_rs_size)
    # Transform
    resize_cropper = v2.RandomResizedCrop(size=r_rs_size)
    r_rs_image = resize_cropper(image)
    r_rs_code = f"v2.RandomResizedCrop(size={r_rs_size})"
    # Show
    col1, col2 = st.columns(2)
    col1.image(image)
    col2.image(r_rs_image)
    st.code(r_rs_code)
    reload_button("random_resized_crop")


def ElasticTransform(image):
    # Elastic
    st.subheader("Elastic Transform")
    # Inputs
    col1, col2 = st.columns(2)
    alpha = col1.slider(
        "Alpha", min_value=0.0, max_value=1000.0, value=250.0, key="alpha"
    )
    sigma = col2.slider(
        "Sigma", min_value=0.0, max_value=1000.0, value=5.0, key="sigma"
    )
    # Transform
    elastic_transformer = v2.ElasticTransform(alpha=alpha, sigma=sigma)
    image_elastic = elastic_transformer(image)
    elastic_code = f"v2.ElasticTransform(alpha={alpha}, sigma={sigma})"
    # Show
    col1, col2 = st.columns(2)
    col1.image(image)
    col2.image(image_elastic)
    st.code(elastic_code)
