import sqlite3
from flask import render_template, redirect, url_for, session, request
from app import app, User, Question

from app import initDB

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    error=None
    last_survey=0
    if 'username' in session:
        username=session['username']
        last_survey=session['last_survey']
    else:
        username=None
    if 'next' in session:
        next=session['next']
    else:
        next=0
    if request.method == 'POST':
        user = User.getUser(app.database_url, request.form['username'], request.form['password'])
        if user == None:
            error='error password'
        else:
            session['id'] = user['id']
            session['username'] = user['username']
            session['last_survey'] = user['last_survey']
            return redirect(url_for('index'))
    return render_template('index.html', error=error, username=username, next=next, last_survey=last_survey)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question(question_id):
    question = Question.getQuestion(app.database_url, question_id)
    if question == None:
        return redirect(url_for('finish'))
    if request.method == 'POST':
        Question.setAnswer(question_id, request.form)
        return redirect('/question/'+str(question_id+1))
    return render_template('question.html', question=question)

@app.route('/finish')
def finish():
    if 'id' not in session or 'answers' not in session or session['answers']==[]:
        return redirect(url_for('index'))
    Question.setFinish(app.database_url)
    return render_template('finish.html')

@app.route('/result')
def result():
    if 'id' not in session:
        return redirect(url_for('index'))
    result = Question.getResult(app.database_url)
    return render_template('result.html', result=result)
