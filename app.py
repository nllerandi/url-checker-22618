from flask import Flask, render_template, request, Response, jsonify
import pandas as pd
import numpy as np
import tempfile
import requests
# import re

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/fios')
def fios():
    return render_template("fios.html")


@app.route('/fiosUpload', methods=['POST'])
def fiosUpload():
    fiosFile = request.files['fiosFile']

    tempfile_path = tempfile.NamedTemporaryFile().name
    fiosFile.save(tempfile_path)

    data = open(tempfile_path).read()
    rows = data.split('\n')
    split_data = []
    for row in rows:
        split_row = row.split(',')
        split_data.append(split_row)

    # def is_allowed_specific_char(string):
    #     charRe = re.compile(r'[^a-zA-Z0-9.]')
    #     string = charRe.search(string)
    #     return not bool(string)

    data = []
    for i in split_data:
        dict_data = {}
        tc = i[8]
        tcr = "in progress"
        # lp = i[19]
        # lpr = str(requests.get(lp).status_code)
        uid = i[21][-4:]
        # cmp = i[32]
        # cmpuid = i[32][-4:]
        url = i[34]
        # urluid = i[34][-12:-8]
        urlr = str(requests.get(url).status_code)

        # if is_allowed_specific_char(tc) == False:
        #     tcr = "Remove special characters"
        # else:
        #     tcr = "cool"

        dict_data[uid] = (url, urlr, tcr)
        data.append(dict_data)

        print(uid + " : " + urlr)

    print(data)

    return render_template("fiosuploadresults.html", data=data)

if __name__ == '__main__':
    app.run()