#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'liugang5'

from flask import Flask,request,render_template,session,redirect,url_for,flash

from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import required
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
momnet = Moment(app)
app.config['SECRET_KEY'] = "hard to guess string"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('templates/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('templates/500.html'), 500

'''
用户第一次访问程序时，服务器会收到一个没有表单数据的GET 请求，所以validate_on_submit() 将返回False。
if 语句的内容将被跳过，通过渲染模板处理请求，并传入表单对象和值为None 的name 变量作为参数。用户会看到浏览器中显示了一个表单。
用户提交表单后，服务器收到一个包含数据的POST 请求。validate_on_submit() 会调用name 字段上附属的Required() 验证函数。
如果名字不为空，就能通过验证，validate_on_submit() 返回True。现在，用户输入的名字可通过字段的data
属性获取。在if 语句中，把名字赋值给局部变量name，然后再把data 属性设为空字符串，从而清空表单字段。最后一行调用render_template() 函数渲染模板，但这一次参数name 的值为表单中输入的名
字，因此会显示一个针对该用户的欢迎消息。
'''
#app.route 修饰器中添加的methods 参数告诉Flask 在URL 映射中把这个视图函数注册为GET 和POST 请求的处理程序。如果没指定methods 参数，就只把视图函数注册为GET请求的处理程序。
@app.route('/', methods=['GET', 'POST'])
def index():
    #局部变量name 用来存放表单中输入的有效名字，如果没有输入，其值为None。
    name = None
    #视图函数中创建一个NameForm 类实例用于表示表单。提交表单后，如果数据能被所有验证函数接受，那么validate_on_submit() 方法的返回值为True，否则返回False。
    form = NameForm()
    if form.validate_on_submit():
        #局部变量name 被用于存储用户在表单中输入的名字。
        #name = form.name.data
        ## form.name.data = ''
        #局部变量name保存在session中

        '''请求完成后，有时需要让用户知道状态发生了变化。这里可以使用确认消息、警告或者错误提醒。
        一个典型例子是，用户提交了有一项错误的登录表单后，服务器发回的响应重新渲染了登录表单，并在表单上面显示一个消息，提示用户用户名或密码错误。
        这种功能是Flask 的核心特性。如示例4-6 所示，flash() 函数可实现这种效果。
        '''
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        '''包含合法表单数据的请求最后会调用redirect() 函数。redirect() 是个辅助函数，用来生成HTTP 重定向响应。redirect() 函数的参数是重定向的URL，这里使用的重定向
        URL 是程序的根地址，因此重定向响应本可以写得更简单一些，写成redirect('/')，但却会使用Flask 提供的URL 生成函数url_for()。推荐使用url_for() 生成URL，因为这
        个函数使用URL 映射生成URL，从而保证URL 和定义的路由兼容，而且修改路由名字后依然可用。
        url_for() 函数的第一个且唯一必须指定的参数是端点名，即路由的内部名字。默认情况下，路由的端点是相应视图函数的名字。在这个示例中，处理根地址的视图函数是index()，因此传给url_for() 函数的名字是index。'''
        return redirect(url_for('index'))
    #较前的一个版本
    # return render_template('index.html', form=form, name=name,current_time=datetime.utcnow())

    #最后一处改动位于render_function() 函数中，使用session.get('name') 直接从会话中读取name 参数的值。和普通的字典一样，这里使用get() 获取字典中键对应的值以避免未找到键的异常情况，因为对于不存在的键，get() 会返回默认值None。
    return render_template('index.html',form=form,name=session.get('name'),current_time=datetime.utcnow())

class NameForm(Form):
    name = StringField('What is your name',validators=[required()])
    submit = SubmitField('Submit')

if __name__ == "__main__":
    app.run(debug=True)
    pass