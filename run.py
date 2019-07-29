from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

MENUDB = 'menu.db'


@app.route('/')
def index():
    burgers = []
    drinks = []
    sides = []

    db = sqlite3.connect(MENUDB)

    print(db)

    cur = db.execute('SELECT burger,price FROM burgers')
    for row in cur:
        burgers.append(list(row))

    cur = db.execute('SELECT drink,price FROM Drinks')
    for row in cur:
        drinks.append(list(row))

    cur = db.execute('SELECT side,price FROM sides')
    for row in cur:
        sides.append(list(row))



    db.close()

    return render_template(
            'index.html',
            disclaimer='may contain traces of nuts',
            burgers=burgers,
            drinks=drinks,
            sides=sides
        )

@app.route('/order')
def order():
    return render_template('order.html')
