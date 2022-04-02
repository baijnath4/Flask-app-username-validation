from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def reportuser():
    EnteredUsername=request.args.get('username')
    lwrAlp = "No Lower case is available in user Name"
    uprAlp = "No Upper case is available in user Name"
    numrAlp = "No Number is available in user Name"
    for i in EnteredUsername:

        if i.islower():
            lwrAlp = "Lower case is available in user Name"

        if i.isupper():
            uprAlp = "Upper case is available in user Name"

        if i.isnumeric():
            numrAlp = "Number is available in user Name"

    print(lwrAlp)
    print(uprAlp)
    print(numrAlp)
    return render_template('report.html',EnteredUsername=EnteredUsername,lwrAlp=lwrAlp,uprAlp=uprAlp,numrAlp=numrAlp)

if __name__=="__main__":
    app.run(debug=True)