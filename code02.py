import streamlit as st
import cv2

img_file = st.file_uploader("เปิดไฟล์ภาพ", type=["png","jpg"])

if img_file is not None:
    st.image(img_file,channels="BGR")
