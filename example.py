from flask import Flask
from flask import request
import cv2
import os
import time
import imageio
import base64

app = Flask(__name__)
#client = storage.Client()

@app.route('/users/<frame_seq>', methods = ['GET', 'POST'])
def user(frame_seq):
    if request.method == 'GET':
        """return the information for <user_id>"""
        data = request.form # a multidict containing POST data
        cam = cv2.VideoCapture("clip1.mp4")
        time_length = 181.0
        fps=30
        frame_seq = 2
        frame_no = 0.3 #(frame_seq /(time_length*fps))
        cam.set(1, 264)
        frame_count=0
        frames = []
        while(frame_count<fps*5):
            et, frame = cam.read()
            frames.append(frame)
            frame_count+=1
        print(frames)
        imageio.mimsave("./vid.gif",frames)
        encoded_string = ""
        with open("./vid.gif", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
    
        return encoded_string

    
if __name__ == "__main__":
    app.run(debug=True)