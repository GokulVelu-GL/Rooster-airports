import os
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.urandom(24)
app.config.from_envvar('FLASKR_SETTINGS',silent=True)




@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/tir', methods=['GET', 'POST'])
def tir():
    return render_template("tir.html")

@app.route('/sag', methods=['GET', 'POST'])
def sag():
    return render_template("sag.html")

@app.route('/mle', methods=['GET', 'POST'])
def mle():
    return render_template("mle.html")

@app.route('/ixc', methods=['GET', 'POST'])
def ixc():
    return render_template("ixc.html")

@app.route('/dxb', methods=['GET', 'POST'])
def dxb():
    return render_template("dxb.html")

@app.route('/cjb', methods=['GET', 'POST'])
def cjb():
    return render_template("cjb.html")



if __name__ == '__main__':
    app.run(debug=True)
