#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', username='world')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('sign_form.html')

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('sign_ok.html', username=username)
    return render_template('sign_form.html', message='bad username or password', username=username)

if __name__ == '__main__':
    app.run()