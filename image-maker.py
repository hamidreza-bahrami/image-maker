import streamlit as st
from PIL import Image 
from PIL import ImageEnhance
import numpy as np
import cv2
import time
import random
from rembg import remove
from colorthief import ColorThief

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
    F2 = np.ones((9, 9)) / 81
    blur = cv2.filter2D(img, -1, F2)
    blured = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)
    return blured

def sp_noise(img, prob):
    output = np.zeros(img.shape,np.uint8)
    thres = 1 - prob 
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = img[i][j]
    outty = cv2.cvtColor(output, cv2.COLOR_RGB2BGR)
    return outty

def bright(img):
    curr_bri = ImageEnhance.Brightness(img) 
    fac = 2.5
    new_img = curr_bri.enhance(fac) 
    return new_img

def inverse(img):
    inverse_img = 255 - img
    return inverse_img

def bright(img):
    brightness = 2 
    contrast = 1.5  
    img2 = cv2.addWeighted(img, contrast, np.zeros(img.shape, img.dtype), 0, brightness)
    return img2 

def detail(img):
    dst = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15)
    new_dst = cv2.cvtColor(dst, cv2.COLOR_RGB2BGR)
    return new_dst
    
def draw(img):
    drawing1, drawing2 = cv2.pencilSketch(img, sigma_s=50, sigma_r=0.07, shade_factor=0.05)
    return drawing1


st.write("<h1 style='text-align: center; color: blue;'>مدل ویرایش تصویر</h1>", unsafe_allow_html=True)
st.write("<h3 style='text-align: center; color: gray;'>تصویر خود را وارد کنید</h3>", unsafe_allow_html=True)
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

    if st.button('نویز اضافه کن'):
        with st.chat_message("assistant"):
                with st.spinner('''درحال انجام، لطفا صبور باشید'''):
                    time.sleep(3)
                    st.success(u'\u2713''انجام شد')
                    noisy_img = sp_noise(img, 0.09)
                    st.image(noisy_img, use_column_width= True)

    if st.button('رنگ‌شو برعکس کن'):
        with st.chat_message("assistant"):
                with st.spinner('''درحال انجام، لطفا صبور باشید'''):
                    time.sleep(3)
                    st.success(u'\u2713''انجام شد')
                    new_img = inverse(img)
                    st.image(new_img, use_column_width= True)

    if st.button('روشن اش کن'):
        with st.chat_message("assistant"):
                with st.spinner('''درحال انجام، لطفا صبور باشید'''):
                    time.sleep(3)
                    st.success(u'\u2713''انجام شد')
                    new_img = bright(img)
                    st.image(new_img, use_column_width= True)

    if st.button('باکیفیت اش کن'):
        with st.chat_message("assistant"):
                with st.spinner('''درحال انجام، لطفا صبور باشید'''):
                    time.sleep(3)
                    st.success(u'\u2713''انجام شد')
                    new_img = detail(img)
                    st.image(new_img, use_column_width= True)

    if st.button('نقاشی اش کن'):
        with st.chat_message("assistant"):
                with st.spinner('''درحال انجام، لطفا صبور باشید'''):
                    time.sleep(3)
                    st.success(u'\u2713''انجام شد')
                    new_img = draw(img)
                    st.image(new_img, use_column_width= True)
                    
    if st.button('پس زمینه رو پاک کن'):
        gaga = Image.open(image)
        fixed = remove(gaga)
        with st.chat_message("assistant"):
                with st.spinner('''درحال انجام، لطفا صبور باشید'''):
                    time.sleep(3)
                    st.success(u'\u2713''انجام شد')
                    st.image(fixed, use_column_width= True)

    if st.button('رنگ غالب رو آنالیز کن'):
        ct = ColorThief(image)
        pallette = ct.get_color(quality=1)
        with st.chat_message("assistant"):
            with st.spinner('''درحال انجام، لطفا صبور باشید'''):
                time.sleep(3)
                st.success(u'\u2713''انجام شد')
                st.write("<h5 style='text-align: right; color: gray;'>رنگ غالب این تصویر</h5>", unsafe_allow_html=True)
                st.subheader(pallette)
    
    if st.button("پاکسازی حافظه"):
        st.cache_data.clear()
        st.rerun()
