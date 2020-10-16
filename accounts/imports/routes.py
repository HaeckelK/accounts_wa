from pathlib import Path
import time
import json

from flask import render_template, current_app, url_for, jsonify, request, flash, redirect

from accounts.imports import bp


import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

from accounts.database import AccountsDatabase
from accounts.utils import datestamp


ALLOWED_EXTENSIONS = {'csv'}


# TODO move out of this module
def get_db():
    return AccountsDatabase(current_app.config['DBFILENAME'])


@bp.route('/')
@bp.route('/imports')
def imports_index():
    return '''Import Index<br><a href='/forms/upload_bank_statement'>Upload Bank Statement</a><br><a href='/api/upload'>List uploads</a>'''


@bp.route('/api/upload')
def api_upload():
    return jsonify(get_db().get_all_upload())


@bp.route('/forms/upload_bank_statement', methods=['GET', 'POST'])
def form_upload_bank_statement():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            time_added = int(str(time.time())[:10])
            # TODO check doesn't already exist
            new_name = str(time_added) + Path(filename).suffix

            db = get_db()
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], new_name))
            
            db.insert_upload(filename, new_name, 'bank_statement', 'form_upload_bank_statement', json.dumps(request.form.to_dict()),
                             datestamp(), time_added, 0, 0, 0)
            return redirect(url_for('imports.imports_index'))
    return render_template('imports/upload_bank_statement.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


from flask import send_from_directory

@bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'],
                               filename)
