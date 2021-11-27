from website import create_app
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
@app.route('/', methods =["GET", "POST"])
def index():     
  return render_template("base.html")
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
