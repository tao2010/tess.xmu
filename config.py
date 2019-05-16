# -*- coding: utf-8 -*-

'''配置文件

flack框架的配置文件，所有的参数在www的init.py中写入app
eg：调用app[SECRET_KEY] 返回字符串'hard to guess'
'''
__author__ = 'tao'

# 文件上传路径
UPLOAD_FOLDER = './data/uploads'
#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
ALLOWED_EXTENSIONS = set(['pdf', 'jpg'])