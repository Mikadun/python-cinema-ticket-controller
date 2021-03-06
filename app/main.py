import json
import os
import pytesseract
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = set(['png'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'image.png')
            file.save(filepath)
            text = pytesseract.image_to_string(filepath, lang='rus')
            if not text:
                text = 'None'

            with open('data.json', 'w', encoding='utf-8') as data_json:
                json.dump(text, data_json)
            
            return redirect(url_for('show'))
    else:
        return '''
        <h1>Upload image</h1>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit">
        </form>
        '''

@app.route("/show")
def show():
    with open('data.json', 'r', encoding='utf-8') as data_json:
        text = json.load(data_json)
    
    return f'<h4>{text}</h4>'


@app.route("/")
def home():
    return redirect(url_for('upload_file'))