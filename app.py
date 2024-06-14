from flask import Flask,url_for,redirect,render_template

# print(":__name__:",__name__)
app = Flask(__name__)
# app = Flask(__name__,template_folder="")  # template_folder 参数可以指定flask应用寻找模板文件的地址
# print("app.template_folder",app.template_folder)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route("/login",methods=["GET"])
def loginview():


    return render_template("index.html",name="ytw")


if __name__ == '__main__':
    app.run()
