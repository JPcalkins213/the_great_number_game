from flask import Flask, request,redirect, session
from flask.templating import render_template
import random
app = Flask(__name__)
app.secret_key = 'root'

@app.route('/')
def the_number():
    

    print(session['guess'])
    if 'guess' not in session:        
        session['guess']  = random.randint(1, 100)
    if 'result' not in session:
        session['result'] = None
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['guess']) > session['guess']:
        session['result'] = 'high'
    elif int(request.form['guess']) < session['guess']:
        session['result'] = 'low'
    else: 
        session['result'] = 'perfect'
    return redirect('/')


if __name__ == '__main__':
    app.run(debug = True)
