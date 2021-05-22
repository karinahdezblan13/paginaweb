from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='templates')
@app.route("/")
def url_principal():
	return render_template("templatedos.html")

@app.route("/about_me")
def about_me():
      return render_template("about_me.html")
@app.route("/familia")
def familia():
      return render_template("familia.html")


if __name__== "__main__":

	app.run(debug=True)

