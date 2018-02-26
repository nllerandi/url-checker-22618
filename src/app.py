from flask import Flask, render_template, request, Response
import pandas as pd
import numpy as np
import tempfile
import os

app = Flask(__name__)


@app.route('/')
def home():
    return "Available endpoints:<br>" \
           "/fios"


@app.route('/fios')
def fios():
    return render_template("fios.html")


@app.route('/fiosUpload', methods=['POST'])
def fiosUpload():
    fiosFile = request.files['fiosFile']

    tempfile_path = tempfile.NamedTemporaryFile().name
    fiosFile.save(tempfile_path)

    # make sure these are getting deleted - or add delete command
    # print(tempfile_path)

    # pandas
    # sheet = pd.read_csv(tempfile_path)

    data = open(tempfile_path).read()
    rows = data.split('\n')
    split_data = []
    for row in rows:
        split_row = row.split(',')
        split_data.append(split_row)

    return str(split_data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)