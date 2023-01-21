from app import db
import datetime


class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    category = db.Column(db.String(50))
    description = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    category = db.Column(db.String(50))
    description = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description


class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    category = db.Column(db.String(50))
    description = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description


class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    due_date = db.Column(db.DateTime)

    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
