'empty'
import os
from django.conf import settings

BASE_DIR = settings.BASE_DIR

PATH = os.path.join(BASE_DIR, r'static/musics')#r"E:\Github\mysite\test\docs"

def full_paths():
    music_names = os.listdir(PATH)
    return [os.path.join('musics', filename) for filename in music_names]
