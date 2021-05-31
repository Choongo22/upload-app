import os
from app import app, ALLOWED_EXTENSIONS
from flask import Flask, render_template, request, flash, url_for, send_from_directory, render_template
from werkzeug.utils import redirect, secure_filename


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def form_upload():
    return render_template('form.html')


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('file is Successfully Uploaded')
            # return redirect(url_for('download_file'))
        return redirect(url_for('download_file', name=filename))
    return render_template('form.html')


"""@app.route('/uploads', methods=['GET'])
def download_file():
    return 'Download page'"""

if __name__ == '__main__':
    app.run(debug=True)
