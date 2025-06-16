import streamlit as st
from PIL import Image, ImageOps

st.title("🖼️ Basic Image Editor")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    filter_type = st.selectbox("Choose Filter", ["Grayscale", "Rotate 90°", "Flip Horizontal"])

    if filter_type == "Grayscale":
        edited = ImageOps.grayscale(image)
    elif filter_type == "Rotate 90°":
        edited = image.rotate(90)
    else:
        edited = ImageOps.mirror(image)

    st.image(edited, caption="Edited Image", use_column_width=True)
