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
    inp=float(request.form['hours'])
    result=imp.predict(inp/60.0)[0][0]
    if float(result)>100.0:
        result="Woah you will get full 100 marks if you study that much!!!"
    else:
        result="your score is {}".format(result)    
    return render_template("index.html",result=result)

if __name__=='__main__':
	app.run(debug=True)