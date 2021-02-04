# djangoDemo
> 介绍：这个一个djaingo项目，之前零零碎碎的学了写，现在做个总结
## 2021.2.3
#### 开始
- 安装虚拟环境
```
#安装虚拟环境
apt install python3-venv
y
#在当前目录下，创建一个python3.6的虚拟环境，取名为env36
python3 -m venv venv
. venv/bin/activate
#进入虚拟环境
#退出虚拟环境 deactivate
```
- 安装django
```
pip3 install Django==2.1.4
```
- 创建app01

```
python3 manage.py startapp app01

# 添加到setting中
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01',
]
```
- 同步数据库，创建超级用户
```
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py createsuperuser

root
python3

```
- 启动项目问题
```
# 直接 python3 manage.py runserver 
# 输入域名夹端口号无法访问
# 记得自己以前遇到这个问题的
# 办法，setting中
ALLOWED_HOSTS = ['*']
python3 manage.py runserver 0.0.0.0:8000

```
> 还是直接在终端输入命令吧，不去探索怎么配置vscode调试功能

- 设置语言和时区
```
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
```

- 安装django代码补全插件
```
pip install pylint_django
```

- 出现了问题：OperationalError: no such table: main.auth_user__old
参考博客 ：https://blog.csdn.net/weixin_44649870/article/details/89450706
```
pip install Django==2.1.5
```
- 我以为升级到2.1.5就可以了，他那时python3.7，我的是3.8，升到2.1.5不可以，我就直接升级到最新
```
pip install Django --upgrade
# 还是不行
```
- 然后我把sqlite3和migrations删除了
```
python3 manage.py  makemigrations
python3 manage.py  migrate
# 创建超级用户
# 错误：no such table
# 我重复迁移文件，结果还是不行
# 然后我指定具体的app，创建成功了
python3 manage.py  makemigrations app01
```
## 2021.2.4

- HttpResponse使用
> 返回原生的字符串，可以包含标签
```
from django.http import HttpResponse
from .models import Post

def homepage(request):
    post = Post.objects.all()
    post_list = list()
    for count,post in enumerate(post):
        post_list.append("No.{}".format(str(count)+str(post)+'<br>'))
    return HttpResponse(post_list)



from app01.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
]
```

- setting中加入模版,创建templates文件夹,里面存放html等模板文件
```
        'DIRS': [os.path.join(BASE_DIR,'templates')],
```

- 使用render：直接渲染html文件
```
from django.shortcuts import render

def homepage2(request):
    return render(request,'index.html')
```

- 使用for 和插入变量
```
    <h1>测试</h1>
    {% for post in posts %}
    <h4>{{ post.title }}</h4>
    <h4>{{ post.slug }}</h4>
    {% endfor %}
    <h6>{{ now }}</h6>
```
```
# 使用函数渲染
def homepage3(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

```
- 动态匹配路由，传递参数，页面调转(使用正则表达式匹配未成功，有待探索)

```
from django.shortcuts import redirect

def showpost(request,slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')



path('post/<int:slug>',showpost),
```

#### 使用公用模板
> 初学的时候没有觉得什么，学完vue、hexo后再来学，感觉这种思想是通用的，django真是nice，感觉很方便的
- base.index
```
    <title>{% block title%}{% endblock %}</title>
</head>
<body>
    {% include 'header.html'%}
    {% block headmessage %}{% endblock %}
    <hr>
    {% block content %}{% endblock %}
    <hr>
    {% 'footer.html'%}
</body>
```
- index.html
> {% extends 'base.html'%} 继承模板
```
{% extends 'base.html'%}
{% block title %}首页的标题{% endblock %}
{% block headmessage %}
    <h3>本站文章列表</h3>
{% endblock %}
{% block contet %}
{% for post in posts %}
    <p>
        <a href="/post/{{post.slug}}">{{post.title}}</a>
    </p>
{% endfor %}
{% endblock %}
```
- post.html
```
{% extends 'base.html' %}
{% block title %}{{post.title}}-文学天地{% endblock %}
{% block headmessage %}
    <h3>{{post.title}}</h3>
    <a href="/">回首页</a>
{% endblock %}

{% block content%}
<p>
    {{post.body}}
</p>
{% endblock %}

```
- header.html
````
<h1>欢迎光临，文学天地</h1>
```
- foot.html
> 这个写法有点不一样，可能是一般不修改，但可以修改
```
{% block footer%}
{% if now %}
<p>现在时刻：{{now}}</p>
{% else %}
<p>已经下架</p>
{% endif %}
{% endblock %}
```
> 各个组件之间还可以传值，现在没有用到

#### 引入bootstrap 样式
- base.html
```
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title%}{% endblock %}</title>

    <!-- CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l" crossorigin="anonymous">
</head>
```
#### 添加static文件夹
- 应该在setting中直接设置了，不用再改了。显示里面的图片失败，因为我是在远程访问服务器的本地测试
- 我使用花生壳内网穿透映射的地址也访问不了，后面可能会出问题

#### 使用解析markdown插件
- 安装
```
pip install django-markdown-deux
pip freeze > requirements.txt
```
- 注册app
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'markdown_deux',
    'app01',
]
```
- 使用post.index
```
{% extends 'base.html' %}
{% load markdown_deux_tags %}
{% block title %}{{post.title}}-文学天地{% endblock %}
{% block headmessage %}
    <h3>{{post.title}}</h3>
    <a href="/">回首页</a>
{% endblock %}

{% block content%}
<p>
    {{post.body | markdown}}
</p>
{% endblock %}

```
- 内容
```
## 二号标题
![](https://cdn.jsdelivr.net/gh/liangxinxin5102/image2/cartoon01/wallhaven-5wqq28.jpg)
```
> 好家伙，自己一年前苦苦寻找的markdown插件，勉强实现了，使用这个插件直接就实现了，而且**使用简单**，我直接好家伙
> 之前学习了一波hexo，知道了竟然有这么多的插件可以用，使用django做个博客时机成熟了，暂时不用vue搞什么前后端分离了。