from flask import Flask, request, redirect, render_template
app = Flask(__name__)
@app.route('/', methods =["GET", "POST"])
def index():     
  return render_template("base.html")
   
if __name__=='__main__':
  app.run()