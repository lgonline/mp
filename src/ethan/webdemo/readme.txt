安装应用中所需要的包
Linux:
flask/bin/pip install flask
flask/bin/pip install flask-login
flask/bin/pip install flask-openid
flask/bin/pip install flask-mail
flask/bin/pip install flask-sqlalchemy
flask/bin/pip install sqlalchemy-migrate
flask/bin/pip install flask-whooshalchemy
flask/bin/pip install flask-wtf
flask/bin/pip install flask-babel
flask/bin/pip install flup

Windows
flask\Scripts\pip install flask
flask\Scripts\pip install flask-login
flask\Scripts\pip install flask-openid
flask\Scripts\pip install flask-sqlalchemy
flask\Scripts\pip install sqlalchemy-migrate
flask\Scripts\pip install flask-whooshalchemy
flask\Scripts\pip install flask-wtf
flask\Scripts\pip install flask-babel
flask\Scripts\pip install flup

文件结构：
webdemo
    |-flask文件夹
    |-<一些虚拟环境的文件>
    |-app文件夹
    |  |-static文件夹
    |  |-templates文件夹
    |  |-__init__.py文件
    |  |-views.py文件
    |-tmp文件夹
    |-run.py文件