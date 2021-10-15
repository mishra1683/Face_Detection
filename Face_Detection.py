import cv2
from random import randrange
face_data=cv2.CascadeClassifier(r'C:\Users\hp\Desktop\Project\Face Detection using OpenCV\haarcascade_frontalface_default.xml')
import streamlit as st
st.title("Open webcam")
start=st.checkbox('START')
f=st.image([])
video=cv2.VideoCapture(0)
while start:
    rev,frame=video.read()
    frame=cv2.flip(frame,1,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    coordinate=face_data.detectMultiScale(gray)
    for (x,y,w,h) in coordinate:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
        cv2.putText(frame,"Beautiful Face",(x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)
    f.image(frame)
    cv2.waitKey(1)


