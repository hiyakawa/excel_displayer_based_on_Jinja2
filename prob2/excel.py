from flask import Flask, request, render_template, flash, redirect, url_for, make_response
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import os
import xlrd

app = Flask(__name__)

bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = os.urandom(24)

base_dir = os.path.abspath(os.path.dirname(__file__))
upload_dir = os.path.join(base_dir, 'static/uploads')

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
            file_name = secure_filename(f.filename)
            valid_types = ['xls', 'xlsx']

            if file_name.split('.')[-1] in valid_types:
                upload_path = os.path.join(upload_dir, file_name)
                f.save(upload_path)
                flash('Successfully uploaded', 'success')

                datalist = xlrd.open_workbook(upload_path, encoding_override="utf-8")
                table = datalist.sheets()[0]
                nrows = table.nrows
                ncols = table.ncols

                titles = [table.cell_value(0, j) for j in range(ncols)]
                rows = [table.row_values(i) for i in range(1, nrows)]

                return render_template('result.html', titles=titles, rows=rows)

            else:
                flash('Invalid file type', 'danger')
                return redirect('/select')

        else:
            flash('Please select the file to be uploaded', 'danger')

    return render_template('input.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)
