from flask import Flask, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
# print(":__name__:",__name__)
app = Flask(__name__)
# app = Flask(__name__,template_folder="")  # template_folder 参数可以指定flask应用寻找模板文件的地址
# print("app.template_folder",app.template_folder)
age = 1

## 数据库配置
# 主机
HOSTNAME = "127.0.0.1"
# 监听端口
PORT = 3306
USERNAME = "root"
PASSWORD = "4161010"
DATABASE = "flask_learning"
app.config["SQLALCHEMY_DATABASE_URI"]=f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"
db=SQLAlchemy(app)
with app.app_context():
    db.create_all()
    # 其他需要应用程序上下文的操作

    with db.engine.connect() as conn:
        rs = conn.execute(text("select 1"))
        print('查询结果',rs.fetchone())


# with db.engine.connect()as conn:
#     db.create_all()
#     rs = conn.execute("select 1")
#     print(rs.fetchone())


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/login", methods=["GET"])
def loginview():
    return render_template("login.html", name="ytw")


@app.route("/index")
def indexview():
    global age
    age += 1
    return render_template("index.html", age=age)


if __name__ == '__main__':
    app.run()
