from flask import Flask, render_template
import dao

app = Flask(__name__)
@app.route("/")
def index():
    cates = dao.get_categories()
    prod = dao.get_product()
    return render_template('index.html', categories = cates, product = prod)

if __name__ == "__main__":
    app.run(debug = True)