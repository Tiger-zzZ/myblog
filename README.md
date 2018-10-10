# myblog


基于`python3.6`和`Django2.1`的博客。   

[![python3.5](https://img.shields.io/badge/python-3.5-brightgreen.svg)]() [![django1.10](https://img.shields.io/badge/django-2.0-brightgreen.svg)]()     

## 主要功能：
- 文章，页面，分类目录，标签的添加，删除，编辑等。。
- 支持文章全文搜索。
- 评论功能，包括发表回复评论
- 侧边栏功能。


### 配置
配置都是在`setting.py`中.部分配置迁移到了后台配置中。


## 运行
	python manage.py runserver 8000

### 创建数据库
	数据库使用Django自带的sqlite。
### 创建超级用户

 终端下执行:

    ./manage.py createsuperuser
### 创建测试数据
终端下执行:

    ./manage.py create_testdata
### 收集静态文件
终端下执行:  

    ./manage.py collectstatic --noinput
    ./manage.py compress --force
### 开始运行：
 执行：
 `./manage.py runserver`





 浏览器打开: http://127.0.0.1:8000/  就可以看到效果了。
## 更多配置:
[更多配置介绍](/bin/config.md)
 ## 问题相关

 有任何问题欢迎提Issue,或者将问题描述发送至我邮箱 .
