from flask import Flask, render_template, request, redirect, url_for, flash
from pagelogic.cart import Cart

app = Flask(__name__)

app.secret_key = 'your_secret_key'

cart = Cart()

@app.route('/')
def index():
    return render_template('add_item.html')

@app.route('/cart')
def view_cart():
    return render_template('cart.html', items=cart.view_cart())

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form['verif']
    if item:
        cart.add_item(item)
        flash(f'{item} added to the cart!', 'success')
    else:
        flash('Please enter an item!', 'error')
    return redirect(url_for('index'))

@app.route('/remove', methods=['POST'])
def remove_item():
    item = request.form['verif']
    if item in cart.view_cart():
        cart.remove_item(item)
        flash(f'{item} removed from the cart!', 'success')
    else:
        flash(f'{item} is not in the cart!', 'error')
    return redirect(url_for('view_cart'))

if __name__ == '__main__':
    app.run(debug=True)
