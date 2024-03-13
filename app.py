## Create a simple flask application

from flask import Flask,render_template,request

## create the flask app

app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello Dhruv</h1>"

@app.route('/welcome')
def welcome():
    return "Welcome to learn flash"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "Congratulations! You passed, your score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "Sorry! You failed, your score is "+str(score)

@app.route('/calculate', methods = ['POST','GET'])
def calculate():
    if request.method=="GET":
        return render_template('calculate.html')
    else:
        maths=float (request.form['mark1'])
        science=float (request.form['mark2'])
        history=float (request.form['mark3'])

        average_marks=(maths+science+history)/3

        return render_template('result.html',results=average_marks)

if __name__=='__main__':
    app.run(debug=True)