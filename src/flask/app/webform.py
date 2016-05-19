#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'liugang5'

from flask.ext.bootstrap import Bootstrap
from flask import Flask,render_template,url_for,request,session,redirect,flash
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'i dont know'

#使用 Flask-WTF 时，每个 Web 表单都由一个继承自 Form 的类表示。这个类定义表单中的一组字段，每个字段都用对象表示。字段对象可附属一个或多个验证函数。验证函数用来验证用户提交的输入值是否符合要求。
class NameForm(Form):
    #NameForm 表单中有一个名为 name 的文本字段和一个名为 submit 的提交按钮。
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')

#app.route 修饰器中添加的 methods 参数告诉 Flask 在 URL 映射中把这个视图函数注册为GET 和 POST 请求的处理程序,默认为GET
#用户第一次访问程序时， 服务器会收到一个没有表单数据的 GET 请求，所以 validate_on_submit() 将返回 False。
#if 语句的内容将被跳过，通过渲染模板处理请求，并传入表单对象和值为 None 的 name 变量作为参数。用户会看到浏览器中显示了一个表单。
#用户提交表单后， 服务器收到一个包含数据的 POST 请求。 validate_on_submit() 会调用name 字段上附属的 Required() 验证函数。如果名字不为空，就能通过验证， validate_on_submit() 返回 True。现在，用户输入的名字可通过字段的 data 属性获取。在 if 语句中，把名字赋值给局部变量 name，然后再把 data 属性设为空字符串，从而清空表单字段。最后一行调用 render_template() 函数渲染模板，但这一次参数 name 的值为表单中输入的名字，因此会显示一个针对该用户的欢迎消息。
@app.route('/',methods=['GET','POST'])
def index():
    #name = None
    '''
    最新版的 hello.py 存在一个可用性问题。用户输入名字后提交表单，然后点击浏览器的刷新按钮，会看到一个莫名其妙的警告，要求在再次提交表单之前进行确认。
    之所以出现这种情况，是因为刷新页面时浏览器会重新发送之前已经发送过的最后一个请求。如果这个请求是一个包含表单数据的 POST 请求，刷新页面后会再次提交表单。最好别让 Web 程序把 POST 请
求作为浏览器发送的最后一个请求。这种需求的实现方式是， 使用重定向作为 POST 请求的响应，而不是使用常规响应。
    重定向是一种特殊的响应， 响应内容是 URL，而不是包含 HTML 代码的字符串。浏览器收到这种响应时， 会向重定向的 URL 发起 GET 请求，显示页面的内容。这个页面的加载可能
要多花几微秒， 因为要先把第二个请求发给服务器。除此之外，用户不会察觉到有什么不同。现在，最后一个请求是 GET 请求，所以刷新命令能像预期的那样正常使用了。这个技巧称为 Post/ 重定向 /Get 模式。
    '''
    #form = NameForm()
    #if form.validate_on_submit():
    #    name = form.name.data
    #    form.name.data = ''
    #return render_template('index.html',form=form,name=name)

    #更新的版本，实现了重定向和用户会话
    form = NameForm()
    if form.validate_on_submit():
        #请求完成后，有时需要让用户知道状态发生了变化。这里可以使用确认消息、警告或者错误提醒。一个典型例子是，用户提交了有一项错误的登录表单后，服务器发回的响应重新渲染了登录表单，并在表单上面显示一个消息，提示用户用户名或密码错误。
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        # #redirect() 是个辅助函数，用来生成 HTTP 重定向响应。 redirect() 函数的参数是重定向的 URL，这里使用的重定向URL 是程序的根地址
        #url_for() 函数的第一个且唯一必须指定的参数是端点名，即路由的内部名字。 默认情况下，路由的端点是相应视图函数的名字。在这个示例中，处理根地址的视图函数是index()，因此传给 url_for() 函数的名字是 index。
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'))

if __name__ == "__main__":
    app.run(debug=True)
    pass