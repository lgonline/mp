多文件Flask 程序的基本结构
|-flasky
    |-app/
        |-templates/
        |-static/
        |-main/
            |-__init__.py
            |-errors.py
            |-forms.py
            |-views.py
        |-__init__.py
        |-email.py
        |-models.py
        |-migrations/
    |-tests/
        |-__init__.py
        |-test*.py
    |-venv/
    |-requirements.txt
    |-config.py
    |-manage.py

这种结构有4 个顶级文件夹：
1.Flask程序一般都保存在名为app 的包中；
2.和之前一样，migrations文件夹包含数据库迁移脚本；
3.单元测试编写在 tests包中；
4.和之前一样，venv 文件夹包含 Python 虚拟环境。

同时还创建了一些新文件：
• requirements.txt列出了所有依赖包，便于在其他电脑中重新生成相同的虚拟环境；
• config.py 存储配置；
• manage.py用于启动程序以及其他的程序任务。