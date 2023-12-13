import streamlit as st
from PIL import Image 
import numpy as np
import cv2

def convert_to_gray(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

def sharpener(img):
    F1 =  np.array([[ 0, -1,  0],
                    [-1, +5, -1],
                    [ 0, -1,  0]])
    sharp = cv2.filter2D(img, -1, F1)
    return sharp

def blurer(img):
    F2 = np.ones((3, 3)) / 9
    blur = cv2.filter2D(img, -1, F2)
    return blur


st.title('Image Processor')
st.header('Upload Your Image And I will Do Some Magic')

image = st.file_uploader('Upload Your Image', type=['png', 'jpg', 'jpeg'])
if image is not None:
    file_bytes = np.array(bytearray(image.read()), dtype= np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    st.image(img, channels= 'BGR', use_column_width= True)

    if st.button('Convert To Gray'):
        img_gray = convert_to_gray(img)
        st.image(img_gray, use_column_width= True)

    if st.button('Sharpen the Image'):
        sharp_img = sharpener(img)
        st.image(sharp_img, use_column_width= True)

    if st.button('Blur the Image'):
        blured_img = blurer(img)
        st.image(blured_img, use_column_width= True)




 

