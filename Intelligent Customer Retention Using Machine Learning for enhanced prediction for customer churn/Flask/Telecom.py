from flask import Flask, render_template, request
import keras
from keras.models import load_model
app = Flask(__name__)
model = load_model("telecom_churn.h5")
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/')
def helloworld():
    return render_template('base.html')
@app.route('/assessment')
def prediction():
    return render_template('index.html')


@app.route('/predict',methods =['POST'])
def admin():
    a = request.form ["gender"]
    if(a == 'f'):
        a = 0
    if(a == 'm'):
        a = 1
    b = request.form ["geography"]
    if(b == 'n'):
        b = 0
    if(b == 'y'):
        b = 1
    c = request.form["balance"]
    if(c == 'n'):
        c = 0
    if(c == 'y'):
        c = 1
    d = request.form["tenure"]
    e = request.form["NumOfProduct"]
    if(e == 'y'):
        e = 0
    if(e == 'n'):
        e = 1
    f = request.form["HasCrCard"]
    if (f == 'y'):
        f = 0
    if (f == 'n'):
        f = 1
    g = request.form["IsActiveMember"]
    if (g=='y'):
        g = 0
    if (g == 'n'):
        g = 1
print(t)
x=model.predict(t)
print(x=[0])
if (x=[[0]]<=0.5):
    y="No"
    return template("predno.html",z=y)

f (x=[[0]]>=0.5):
    y="Yes"
    return template("predyes.html",z=y)

