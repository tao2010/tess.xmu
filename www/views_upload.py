# -*- coding:utf-8 -*-
"""上传文件视图层

处理上传文件的URL，提供视图
"""

__author__ = 'tao'

from flask import Blueprint, render_template, redirect, request, url_for, jsonify
from www import app
from cv2 import cv2
import os
from werkzeug.utils import secure_filename
from flask import jsonify
import pytesseract
from PIL import Image


upload = Blueprint('upload',__name__)


def allowed_file(filename):
    return '.' in filename and  filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@upload.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        img = cv2.imread(upload_path)
        text=pytesseract.image_to_string(img)
        print(text)
    return jsonify({"status": 200, "msg": "upload success","text": text})

if __name__ == '__main__':
    app.run(debug=True)