from flask import Flask,render_template,request,redirect

app=Flask(__name__)

import joblib
import numpy as np

@app.route("/")
def home():
	return render_template("index.html")

@app.route('/submit',methods=['POST'])
def submit():
	model=joblib.load("linear_regression.pkl")
	st=float(request.form['num'])
	marks=model.predict([[st]])
	marks=marks[0][0]
	# return str(store[0][0])
	return render_template("index.html",your_marks='%.3f'%marks)
# 	# return "<h1>the number is {}</h1>".format(int(request.form['n1'])+int(request.form['n2']))
	
if __name__=='__main__':
	app.run(debug=True)