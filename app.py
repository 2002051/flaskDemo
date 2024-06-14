from flask import Flask,url_for,redirect,render_template

# print(":__name__:",__name__)
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route("/login",methods=["GET"])
def loginview():


    return render_template("index.html")


if __name__ == '__main__':
    app.run()
