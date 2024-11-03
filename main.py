import streamlit as st
from PIL import Image

st.header("Take a photo to convert it to grey scale!")

with st.expander("Start Camera"):
    camera_image = st.camera_input("Take a photo")

if camera_image:
    with st.expander("Click reveal your image"):
        # Create a pillow image
        img = Image.open(camera_image)
        # Convert pillow image into grey scale
        grey_image = img.convert("L")
        # Render image on page
        st.image(grey_image)
