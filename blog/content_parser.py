#coding=utf-8
'this file is used to parse extenal docs writed in markdown and save them into database'
import os
from models import Article

PATH = r"E:\Projects\mysite\trunk\test\docs"

def if_is_property(str_):
    'check if the string is a formated property and return a list if True'
    property_patterns = '|'.join(dir(Article))
    from re import match
    return match('^(' + property_patterns + r')\s?=\s?(.*)', str_)

def convert_all(path=PATH):
    'convert all files in the directory of " path" into string'
    file_names = os.listdir(path)
    full_paths = (PATH + "/" + filename for filename in file_names)
    article = Article()
    for path in full_paths:
        file_ = open(path, 'r')
        line = ''
        while True:
            line = file_.readline()
            match = if_is_property(line)
            if match:
                article.__dict__[match.group(1)] = match.group(2)
        article.text = line + file_.read()
        if article.author is None:
            article.author = '踢叉叉'
        article.publish()
