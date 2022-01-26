#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("profile1.html")

@app.route('/msg', methods=['GET'])
def recup():
    text = request.args.get['text']


if __name__ == '__main__':
    app.run(debug=True)
