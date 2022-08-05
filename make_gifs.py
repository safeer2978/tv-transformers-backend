import cv2
import os
import time
import imageio
import skimage.transform as st
from pygifsicle import optimize
cam = cv2.VideoCapture("clip.mp4")
fps=60
frame_seq = 2
frame_no = 0.3

video_time_in_sec= 573


def create_gif(milli_sec):
    frame_count=0
    start = milli_sec*fps
    frames = []
    cam.set(1, start)
    while(frame_count<fps*3):
        et, frame = cam.read()
        frame = st.resize(frame, (168, 400))
        frames.append(frame)
        frame_count+=1
    
    with imageio.get_writer("./"+"1"+"/"+str(milli_sec)+".gif", mode='I') as writer:
        for frame in frames:
            writer.append_data(frame)

    #imageio.mimsave("./"+"1"+"/"+str(milli_sec)+".gif",frames,fps=60)
    #optimize("./"+"1"+"/"+str(milli_sec)+".gif")

for i in range(0, video_time_in_sec):
    create_gif(i)