#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

import os
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask,session,redirect,render_template,url_for
from flask.ext.wtf import Form
from wtforms.validators import Required
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from wtforms import StringField,SubmitField
from flask.ext.script import Shell
from flask.ext.script import Manager

#初始化及配置一个简单的SQLite 数据库
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
manager = Manager(app)

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'hard to guess string'

db = SQLAlchemy(app)
#db.create_all()

class NameForm(Form):
    name = StringField('What your are name?',validators=[Required()])
    submit = SubmitField('submit')

class Role(db.Model):
    #__tablename__定义在数据库中使用的表名
    __tablename__ = 'roles'
    #db.Column 类构造函数的第一个参数是数据库列和模型属性的类型
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)

    #定义了__repr()__ 方法，返回一个具有可读性的字符串表示模型，可在调试和测试时使用
    def __repr__(self):
        return '<Role %r>' % self.name

    #关系型数据库使用关系把不同表中的行联系起来,
    '''
    这里是角色到用户的一对多关系，因为一个角色可属于多个用户，而每个用户都只能有一个角色。
    db.relationship() 的第一个参数表明这个关系的另一端是哪个模型。如果模型类尚未定义，可使用字符串形式指定。
    db.relationship() 中的backref 参数向User 模型中添加一个role 属性，从而定义反向关系。这一属性可替代role_id 访问Role模型，此时获取的是模型对象，而不是外键的值。
    '''
    users = db.relationship('User',backref='role')

class User(db.Model):
    #__tablename__定义在数据库中使用的表名
    __tablename__ = 'users'
    #db.Column 类构造函数的第一个参数是数据库列和模型属性的类型
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)

    #定义了__repr()__ 方法，返回一个具有可读性的字符串表示模型，可在调试和测试时使用
    def __repr__(self):
        return '<User %r>' % self.username

     #关系使用users 表中的外键连接了两行。添加到User 模型中的role_id 列被定义为外键，
    # 就是这个外键建立起了关系。传给db.ForeignKey() 的参数'roles.id' 表明，这列的值是roles 表中行的id 值。
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

#每次启动shell 会话都要导入数据库实例和模型，这真是份枯燥的工作。为了避免一直重复导入，通过配置，让Flask-Script 的shell 命令自动导入特定的对象
def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role)
#把对象添加到导入列表中，我们要为shell 命令注册一个make_context 回调函数
manager.add_command("shell",Shell(make_context=make_shell_context()))
#make_shell_context() 函数注册了程序、数据库实例以及模型，因此这些对象能直接导入shell：
#python hello.py shell

#在视图函数中操作数据库
@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        #使用filter_by() 查询过滤器在数据库中查找提交的名字。
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    #return render_template('index_for_sqlalchemy.html',form = form, name = session.get('name'))
    return render_template('index_for_sqlalchemy.html',form = form, name = session.get('name'),known = session.get('known', False))
    #return render_template('index_for_sqlalchemy.html')                                                                         ))

if __name__ == "__main__":
    app.run(debug=True)
    pass