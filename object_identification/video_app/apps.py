import os
from django.apps import AppConfig
from django.apps import AppConfig
from django.conf import settings

#we will place the code to load our models here because this code will not run every time a request is made

class VideoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'video_app'

    path = os.path.join(settings.MODELS, "yolov4.h5") #.h5 for model weights
    path1 = os.path.join(settings.MODELS, "yolov4.json") #.json for model