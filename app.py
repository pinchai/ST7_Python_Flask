from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return '<center><h1 style="color: red">Home page</h1></center>'


@app.route('/product')
def product():
    return render_template("product_card.html")


if __name__ == '__main__':
    app.run()
