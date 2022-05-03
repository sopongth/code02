import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
import numpy as np

st.title("ตรวจจับวัตถุสีแดง")

def dip(img):    
    img = cv2.flip(img,1) 
    imgYCrCb  = cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
    channels = cv2.split(imgYCrCb)
    Cr = channels[1]
    ret,BW = cv2.threshold(Cr,180,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(BW,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt = contours[max_index]
    x,y,w,h = cv2.boundingRect(cnt)    
    img_out = img.copy()
    cv2.rectangle(img_out,(x,y),(x+w,y+h),(0,255,255),4) 
    return img_out

class VideoProcessor:  
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img_out = dip(img)
        return av.VideoFrame.from_ndarray(img_out,format="bgr24")

webrtc_streamer(key="test",
                video_processor_factory=VideoProcessor,
                media_stream_constraints={"video": True,"audio": False})
