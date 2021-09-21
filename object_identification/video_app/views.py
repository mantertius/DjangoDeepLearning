import glob
import json
import os
import time

import cv2
import numpy as np
import requests
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from scipy import ndimage
from scipy.ndimage import zoom

from .apps import VideoAppConfig  # for linking apps.py to model weights


def getFrame (vidcap, sec, count):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        cv2.imwrite("frames/frame"+ str(count) + ".jpg")

@api_view(["POST"]) #receives the request
def check_result(request):
    #Get video file url
    url = request.POST.get('url') #we are using dictionary (key-value) to store the request
    head,tail = os.path.split(url)
    
    r = request.get(url,allow_redirects=True)
    open("resume/" + tail, "wb").write(r.content)
    
    video_path = 'resume/'
    files = []

    for i in os.listdir(video_path): #appends the video path to files
        if i.endswith('.mp4'):
            files.append(i)
    
    for j in files:
        vidcap = cv2.VideoCapture("resume/"+j)
        sec = 0
        count = 1
        frameRate = 5
        success = getFrame(vidcap, sec, count)

        while success:
            count = count +1
            sec = sec + frameRate
            sec = round(sec,2)
            success = getFrame(vidcap, sec, count)
    
    img_path = glob.glob("frames/*.jpg")
    data = []
    for image1 in img_path:
        n = cv2.imshow(image1)
        boo = cv2.imread(n)
        print(boo)
        x = {
            'tem video': 'SIM',
            'nao tem video': 'NAO'}
        y = json.dumps(x)

    return JsonResponse(x)
