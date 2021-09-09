#From Flask I want to import Flask, render_template and request.
from flask import Flask, render_template, request

#Declare the app.
application = app = Flask(__name__)

#Start an app route which is '/'
@app.route('/')
#Declare the main function.
def main():
    return render_template('app.html')

#Form Submission Route.
@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']
    #Calculate IF Statements.
        if operation == 'add':
            sum = float(num1) + float(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'subtract':
            sum = float(num1) - float(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'multiply':
            sum = float(num1) * float(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'divide':
            sum = float(num1) / float(num2)
            return render_template('app.html', sum=sum)
        else:
            return render_template('app.html')