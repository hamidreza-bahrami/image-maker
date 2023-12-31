import streamlit as st
from PIL import Image 
import numpy as np
import cv2
import time

def convert_to_gray(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

def sharpener(img):
    F1 = np.array([[ 0, -1,  0],
                   [-1, +5, -1],
                   [ 0, -1,  0]])
    sharp = cv2.filter2D(img, -1, F1)
    sharpened = cv2.cvtColor(sharp, cv2.COLOR_BGR2RGB)
    return sharpened

def blurer(img):
    F2 = np.ones((5, 5)) / 25
    blur = cv2.filter2D(img, -1, F2)
    blured = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)
    return blured


st.write("<h1 style='text-align: center; color: blue;'>مدل پردازش تصویر</h1>", unsafe_allow_html=True)
st.write("<h2 style='text-align: center; color: gray;'>تصویر خود را وارد کنید</h2>", unsafe_allow_html=True)
st.write("<h4 style='text-align: center; color: gray;'>Robo-Ai.ir طراحی شده توسط</h4>", unsafe_allow_html=True)
st.link_button("Robo-Ai بازگشت به", "https://robo-ai.ir")

image = st.file_uploader('آپلود تصویر', type=['png', 'jpg', 'jpeg'])
if image is not None:
    file_bytes = np.array(bytearray(image.read()), dtype= np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    st.image(img, channels= 'BGR', use_column_width= True)

    if st.button('خاکستری کن'):
        with st.chat_message("assistant"):
                with st.spinner('''درحال انجام، لطفا صبور باشید'''):
                    time.sleep(3)
                    st.success(u'\u2713''انجام شد')
                    img_gray = convert_to_gray(img)
                    st.image(img_gray, use_column_width= True)

    if st.button('شارپ کن'):
        with st.chat_message("assistant"):
                with st.spinner('''درحال انجام، لطفا صبور باشید'''):
                    time.sleep(3)
                    st.success(u'\u2713''انجام شد')
                    sharp_img = sharpener(img)
                    st.image(sharp_img, use_column_width= True)

    if st.button('محو کن'):
        with st.chat_message("assistant"):
                with st.spinner('''درحال انجام، لطفا صبور باشید'''):
                    time.sleep(3)
                    st.success(u'\u2713''انجام شد')
                    blured_img = blurer(img)
                    st.image(blured_img, use_column_width= True)
