from flask import Flask, render_template
from form import Application
app = Flask(__name__)

app.secret_key = "maria"


@app.route('/')
def index():
    form = Application()
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run()