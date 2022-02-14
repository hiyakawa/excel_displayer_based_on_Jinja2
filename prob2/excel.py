from flask import Flask, request, render_template, flash, redirect, url_for, make_response, send_file
from werkzeug.utils import secure_filename
from pypinyin import lazy_pinyin
from uuid import uuid4
import os
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
base_dir = os.path.abspath(os.path.dirname(__file__))
upload_dir = os.path.join(base_dir, 'static/uploads')

def random_filename(string):
    ident = uuid4().__str__()
    return f"{ident}-{string}"

@app.route('/select', methods = ['GET', 'POST'])
def select():
    return render_template('input.html')

@app.route('/result', methods = ['GET', 'POST'])
def print_table():
    if request.method == 'POST':
        f = request.files['file']

        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        if f:
            original_filename = secure_filename(''.join(lazy_pinyin(f.filename)))
            valid_types = ['xls', 'xlsx']

            if original_filename.split('.')[-1] in valid_types:
                unique_filename = random_filename(original_filename)
                upload_path = os.path.join(upload_dir, unique_filename)
                f.save(upload_path)
                flash('Successfully uploaded', 'success')

                df = pd.read_excel(upload_path)
                return render_template('result.html', titles = df.columns.values, rows = list(df.values.tolist()))

            else:
                flash('Invalid file type', 'danger')
                return redirect('/select')

        else:
            flash('Please select the file to be uploaded', 'danger')

    return render_template('input.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)
