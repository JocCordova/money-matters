from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Income, Expense, Investment, Reminder
from sqlalchemy import func, extract
from datetime import datetime


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/income', methods=['GET', 'POST'])
def income():
    if request.method == 'POST':
        income = Income(request.form['amount'], request.form['category'], request.form['description'])
        db.session.add(income)
        db.session.commit()
        return redirect(url_for('income'))
    else:
        incomes = Income.query.all()
        return render_template('income.html', incomes=incomes)


@app.route('/expense', methods=['GET', 'POST'])
def expense():
    if request.method == 'POST':
        expense = Expense(request.form['amount'], request.form['category'], request.form['description'])
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('expense'))
    else:
        expenses = Expense.query.all()
        return render_template('expense.html', expenses=expenses)


@app.route('/investment', methods=['GET', 'POST'])
def investment():
    if request.method == 'POST':
        investment = Investment(request.form['amount'], request.form['category'], request.form['description'])
        db.session.add(investment)
        db.session.commit()
        return redirect(url_for('investment'))
    else:
        investments = Investment.query.all()
        return render_template('investment.html', investments=investments)


@app.route('/reminder', methods=['GET', 'POST'])
def reminder():
    if request.method == 'POST':
        reminder = Reminder(request.form['title'], request.form['due_date'])
        db.session.add(reminder)
        db.session.commit()
        return redirect(url_for('reminder'))
    else:
        reminders = Reminder.query.all()
        return render_template('reminder.html', reminders=reminders)


@app.route('/dashboard')
def dashboard():
    total_income = Income.query.filter(extract('month', Income.timestamp) == datetime.now().month).with_entities(func.sum(Income.amount)).scalar()
    total_expenses = Expense.query.filter(extract('month', Expense.timestamp) == datetime.now().month).with_entities(func.sum(Expense.amount)).scalar()
    total_investment = Investment.query.filter(extract('month', Investment.timestamp) == datetime.now().month).with_entities(func.sum(Investment.amount)).scalar()

    return render_template('dashboard.html', total_income=total_income, total_expenses=total_expenses,
                           total_investment=total_investment)
