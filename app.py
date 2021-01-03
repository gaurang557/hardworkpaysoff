from flask import Flask,render_template,request,redirect
import imp

app=Flask(__name__)

@app.route('/')
def function():
	result=None
	return render_template("index.html")


@app.route("/submit",methods=["POST"])
def submit():
	result=None
	inp=request.form['hours']
	result=imp.predict(float(inp))
	return render_template("index.html",result=result)

if __name__=='__main__':
	app.run(debug=True)