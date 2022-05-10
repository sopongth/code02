import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("ทดสอบกล้อง")

webrtc_streamer(key="test",
                media_stream_constraints={"video": True,"audio": False},
                rtc_configuration={"iceServers":[{"urls",:["stun:stun.l.google.com:19302"]}])}
