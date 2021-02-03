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