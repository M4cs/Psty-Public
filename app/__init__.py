from flask import Flask, request, redirect, render_template, send_file
from flask_restful import Resource, Api
from app.resources.constants import languages
from app.resources.helpers import generateOptions

app = Flask(__name__)
api = Api(app)

@app.route('/')
def returnit():
    return redirect('https://psty.io/new')

@app.route('/new')
def get():
    options = generateOptions(languages)
    return render_template('new.html', options=options)

@app.route('/assets/css/<css>')
def css(css):
    return send_file('templates/assets/css/{}'.format(css))

@app.route('/assets/js/<js>')
def js(js):
    return send_file('templates/assets/js/{}'.format(js))

@app.route('/assets/images/<image>')
def image(image):
    return send_file('templates/assets/images/{}'.format(image))

from app.resources import upload
from app.resources import pastes

api.add_resource(upload.Upload, '/upload')
api.add_resource(pastes.Pastes, '/p')
