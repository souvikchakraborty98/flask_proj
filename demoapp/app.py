from flask import Flask,request,render_template
app=Flask(__name__)

@app.route("/1")
def newpage1():
    return "It works 1."

@app.route("/2")
def newpage2():
    return "It works 2."

@app.route("/",methods= ['GET','POST'])
def rootpage():
    weight=0
    height=0
    bmi=0
    if request.method=='POST':
        if 'userweight' in request.form:
            weight=request.form.get('userweight')
        if 'userheight' in request.form:
            height=request.form.get('userheight')
        try:
            if weight and height:
                bmi=int(weight)/(pow(int(height),2))
        except:
            pass
        
    return render_template("index.html", weight=weight,height=height,bmi=bmi)

if __name__ == "__main__":
    app.run()