'empty'
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PATH = os.path.join(BASE_DIR, r'static/musics')#r"E:\Github\mysite\test\docs"

def full_paths():
    music_names = os.listdir(PATH)
    return [os.path.join('musics', filename) for filename in music_names]
