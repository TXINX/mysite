#coding=utf-8
'this file is used to parse extenal docs writed in markdown and save them into database'
import os
from models import Article


PATH = r"E:\Projects\mysite\trunk\test\docs"

def if_is_property(str_):
    'check if the string is a formated property and return a list if True'
    property_patterns = 'title'#'|'.join(dir(Article))
    from re import match
    return match('^(' + property_patterns + r')\s?=\s?(.*)\s', str_)

def convert_all(user,path=PATH):
    #test
    'convert all files in the directory of " path" into string'
    file_names = os.listdir(path)
    full_paths = (PATH + "/" + filename for filename in file_names)
    #之前把article的初始化写在外面，结果隐含的pk值没有改变，所以后面的文章把前面的覆盖掉了
    for path in full_paths:
        file_ = open(path, 'r')
        article = Article()
        line = ''
        while True:
            line = file_.readline()
            match = if_is_property(line)
            if match:
                print 'test'
                print match.groups()
                article.__dict__[match.group(1)] = match.group(2)
            else:
                break
        article.text = line + file_.read()
        #if article.author is None:
        article.author = user
        article.publish()
