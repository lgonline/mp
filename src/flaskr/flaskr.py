#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

import sqlite3
from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash
from contextlib import closing

# configuration
DATABASE = 'D:\\JetBrains\\workspaces\\mp\\src\\flaskr\\mydb.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'admin'

app = Flask(__name__)
#from_object() 会查看给定的对象（如果该对象是一个字符串就会 直接导入它），搜索对象中所有变量名均为大字字母的变量。在我们的应用中，已经将配 置写在前面了。你可以把这些配置放到一个独立的文件中。
app.config.from_object(__name__)
app.config['SECURE_KEY'] = 'HARD TO GUESS'

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

#创建一个用来初始化数据库的 init_db 函数，其中我们使用了先前创建的 connect_db 函数。把这个初始化函数放在 flaskr.py 文件中的`connect_db` 函数 下面
def init_db():
    #closing() 帮助函数允许我们在 with 代码块保持数据库连接 打开
    with closing(connect_db()) as db:
        #应用对象的 open_resource() 方法支持也支持这个功能， 可以在 with 代码块中直接使用。这个函数打开一个位于来源位置（你的 flaskr 文件夹）的文件并允许你读取文件的内容
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

'''
之前，完成了连接数据库，如何在请求时使用它呢？会在每一个函数中用到数据库连接，有必要在请求之前初始化连接，并在 请求之后关闭连接。
使用 before_request() 装饰的函数会在请求之前调用，且不传递参数。
使用 after_request() 装饰的函数会在请求之后调用，且传递发送给客户端响应对象。它们必须传递响应对象，所以在出错的情况下就不会执行。
因此我们就要用到teardown_request()装饰器了。这个装饰器下的函数在响应对象构建后被调用。它们不允许修改请求，并且它们的返回值被忽略。如果请求过程中出错，那么这个错误会传递给每个函数；否则传递 None 。
我们把数据库连接保存在Flask提供的特殊的g对象中。这个对象与每一个请求是一一对应的，并且只在函数内部有效。不要在其它对象中储存类似信息，因为在多线程环境下无效。这个特殊的g对象会在后台神奇的工作，保证系统正常运行。
'''
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()

#这个视图显示所有数据库中的条目。 它绑定应用的根地址，并从数据库中读取 title 和 text 字段。
@app.route('/')
def show_entries():
    #id 最大的记录（最新的条目）在最上面
    cur = g.db.execute('select title, text from entries order by id desc')
    #从指针返回的记录集是一个包含 select 语句查询结果的元组
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    # 这个视图会把条目作为字典传递给 show_wblog.html 模板，并返回渲染结果
    return render_template('show_wblog.html', entries=entries)

#这个视图可以让一个登录后的用户添加一个新条目。
# 本视图只响应 POST 请求，。如果一切顺利，我们会 :
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    #flash() 一个消息给下一个请求并重定向回到 show_entries 页面
    flash('New entry was successfully posted')
    #真正的表单显示在 show_entries 页面中
    return redirect(url_for('show_entries'))

#这些函数用于用户登录和注销。
#登录视图根据配置中的用户名和密码验证用户并在会话中设置logged_in键值。
# 如果出现错误，模板会 提示错误信息，并让用户重新登录:
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            #如果用户通过验证，键值设为 True
            session['logged_in'] = True
            #闪现一个信息，告诉用户已登录成功
            flash('You were logged in')
            #用户会被重定向到 show_entries 页面
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

#登出视图则正好相反，把键值从会话中删除。
#这里使用了一个小技巧：。
@app.route('/logout')
def logout():
    #使用字典的pop()方法并且传递了第二个参数（键的缺省值），当字典中有这个键时就会删除这个键，否则什么也不做。这样做的好处是我们不用检查用户是否已经登录了
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == "__main__":
    app.run()
    pass