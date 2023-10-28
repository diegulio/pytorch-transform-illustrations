import streamlit as st

uploaded_file = st.sidebar.file_uploader("Upload an Image (Optional)", type=["jpg", "jpeg"])
if uploaded_file:
    st.session_state["uploaded_file"] = uploaded_file.getvalue()

st.title("Pytorch Transform Illustration")

mkd = """
Pytorch’s Illustration is an application to do online testing of different data augmentations provided by Pytorch. You can find these in the Pytorch documentation right [here](https://pytorch.org/vision/main/auto_examples/transforms/plot_transforms_illustrations.html). We have prioritized those ones which are mostly used (the same thing with their parameters). Here you can find a list with the available augmentations: 


> :warning: **To observe transformations faster we recommend to filter only transformations that you want to test.**

| **Geometric Transforms 📐**                   | **Photometric Transform 🌄**                        | **Augmentation Transforms 🧠**   |
|----------------------------------------------|----------------------------------------------------|---------------------------------|
| `Pad(padding, fill)`                           | `Grayscale()`                                        | `RandomAugment(num_ops)`          |
| `Resize(size)`                                | `ColorJitter(brightness, contrast, saturation, hue)` | `TrivialAugmentWide()`            |
| `CenterCrop(size)`                             | `GaussianBlur(kernel_size, sigma)`                   | `AugMix(severity, mixture_width)` |
| `RandomPerspective(distortion_scale, fill)`    | `RandomInvert()`                                     |                                 |
| `RandomRotation(degrees, fill)`                | `RandomPosterize(bits)`                              |                                 |
| `RandomAffine(degrees, translate, scale,fill)` | `RandomSolarize(threshold)`                          |                                 |
| `RandomCrop(size)`                             | `RandomAdjustSharpness(sharpness_factor)`            |                                 |
| `RandomResizedCrop(size)`                      | `RandomAutoContrast()`                               |                                 |
|                                              | `RandomEqualize()`                                   |                                 |

In the future we will keep adding more transforms and parameters. We encourage you to contribute if you want to add more!


"""



st.markdown(mkd)
# TODO: Document this
# TODO: add links to transform docs in each transform