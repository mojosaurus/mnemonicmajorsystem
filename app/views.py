from app.namemap import nameMap

__author__ = 'mojosaurus'

from app import app
from flask import render_template, send_file
import random


@app.route('/get_image/<image_id>')
def get_image(image_id):
    print image_id
    filename = 'static/%s.jpg' % image_id
    return send_file(filename, mimetype='image/jpg')


@app.route('/')
def index():
    user = {'handle': 'mojosaurus'}
    return render_template('index.html',
                           title='Home',
                           user=user)



@app.route('/learn')
def learn():
    user = {'handle': 'mojosaurus'}
    num = random.randrange(0,25)
    return render_template('learn.html',
                           title='Home',
                           user=user,
                           id="{0:02d}".format(num))


@app.route('/recall_int')
def recall_int():
    user = {'handle': 'mojosaurus'}
    num = random.randrange(0,25)
    return render_template('recall_int.html',
                           title='Home',
                           user=user,
                           id="{0:02d}".format(num))

@app.route('/recall_img')
def recall_img():
    user = {'handle': 'mojosaurus'}
    num = random.randrange(0,25)
    return render_template('recall_img.html',
                           title='Home',
                           user=user,
                           name=nameMap["{0:02d}".format(num)],
                           id="{0:02d}".format(num))