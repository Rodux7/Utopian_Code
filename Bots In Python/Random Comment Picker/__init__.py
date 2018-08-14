# Imports
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from data import rand_com

# Variables
app = Flask(__name__)
app.config["SECRET_KEY"] = "abracadabra"

# Classes For Forms
class post_link(FlaskForm):
    link = StringField("Post Link")

# Routes
@app.route("/", methods=["POST", "GET"])
def index():
  form = post_link(name="form")
  if form.validate_on_submit():
    data = str(form.link.data)
    authorperm = data.split("@")
    return redirect("http://127.0.0.1:5000/@" + authorperm[1])
  return render_template("index.html", form=form)

@app.route("/@<author>/<permlink>")
def comment(author, permlink):
  fake_link = "https://steemit.com/steemhunt/@%s/%s" % (author, permlink)
  com = rand_com(fake_link)
  return render_template("com.html", com=com)

# Run App
if __name__ == "__main__":
  app.run(debug="true")
