from flask import Flask, render_template, request
import dao

app = Flask(__name__)


@app.route("/")
def index():
    kw = request.args.get('kw')
    cates = dao.get_categories(kw)
    prod = dao.get_product(kw)
    return render_template('index.html', categories=cates, product=prod)


if __name__ == "__main__":
    app.run(debug=True)
