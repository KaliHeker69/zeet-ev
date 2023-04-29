from flask import Flask,render_template,url_for,request,redirect,session
from functools import wraps
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

app = Flask(__name__)

@app.route('/')
def start():
    return render_template("index.html")

@app.route('/index.html')
def index():
    return render_template("index.html")


@app.route('/about.html',methods = ["POST","GET"])
def model():
    if request.method == 'POST':
        loaded_model = joblib.load('model_joblib')
        feature_list = request.form.to_dict()
        feature_list = list(feature_list.values())
        feature_list = list(map(float, feature_list))
        final_feature_list = np.array(feature_list)
        final_feature_list = final_feature_list.reshape(1,5)
        final = loaded_model.predict(final_feature_list)
        final = round(float(final),2)
        return render_template('about.html', prediction_text= ' {}$'.format(final))
    if request.method == 'GET':
        return render_template('about.html')


@app.route('/login.html',methods=["POST","GET"])
def log():
    return render_template("login.html")


@app.route('/welcome.html',methods=["POST","GET"])
def welcome():
    return render_template("welcome.html")

if (__name__) == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)

