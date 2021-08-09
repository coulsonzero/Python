from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# 配置数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:0627@127.0.0.1/flask_sql_demo'
# 跟踪数据库的修改 --> 不建议开启，未来版本中会移除
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 数据库模型
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    # 外键
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))



# @app.route('/', methods=['GET', 'POST'])
@app.route('/')
def index():
    return 'Hello flask!'
    # if request.method == 'POST':
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     print(password)
    #     if not all([username, password]):
    #         flash(u'信息不全')
    #     elif username == "coulson" and password == "0627":
    #         return 'success'
    #     else:
    #         flash(u'密码错误')
    # return render_template('index.html')




if __name__ == '__main__':
    # 创建表, 实际开发用命令行
    # db.drop_all()
    db.create_all()

    app.run(debug=True)
