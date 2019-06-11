from app import app
from flask import request, redirect, render_template
from flask_restful import Resource, reqparse
from app.resources.constants import languages
from app.resources.helpers import generateOptions
from uuid import uuid4

def upload_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('code', required=True)
    parser.add_argument('lang', required=True)
    parser.add_argument('title', required=True)
    return parser

class Upload(Resource):
    def post(self):
        parser = upload_parser()
        data = parser.parse_args()
        code = data['code']
        lang = data['lang']
        title = data['title'].replace(' ', '-')
        for key, value in languages.items():
            if key == data['lang'] or value == data['lang']:
                language_proper = key
                lang_short = value
                with open('app/templates/index.html', 'r') as html_file:
                    new_html = html_file.read().replace('class="language-{{language}}"', 'class="lang-%s"' % lang_short).replace("{{lang}}", language_proper)
                    new_html = new_html.replace("{{code}}", code)
                    uid = str(uuid4()).split('-')[0]
                    filename = uid + '-' + title
                    with open('app/templates/pastes/{}.html'.format(filename), 'w') as out:
                        out.write(new_html)
                        out.close()
                    html_file.close()
                return redirect('https://psty.io/p?q={}.html'.format(filename))
            if data['lang'] == "Plaintext":
                with open('app/templates/plain.html', 'r') as html_file_1:
                    new_html = html_file_1.read().replace('{{code}}', code)
                    uid = str(uuid4()).split('-')[0]
                    filename = uid + '-' + title
                    with open('app/templates/pastes/{}.html'.format(filename), 'w') as out:
                        out.write(new_html)
                        out.close()
                    html_file_1.close()
                return redirect('https://psty.io/p?q={}.html'.format(filename))
        return {
            'status': 400
        }
