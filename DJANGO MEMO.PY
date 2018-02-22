Django
	env
		proj1
			app1
			app2
		proj2




**改pip下载路径，国内载pip较快 , %USERPROFILE%  建pip文件夹 放 pip.ini
	[global]
	index-url = http://mirrors.aliyun.com/pypi/simple/

	[install]
	trusted-host = mirrors.aliyun.com

**使用cmder，可以直接用linux指令

**vscode : Ctrl + Shift + P , 改语系为 en:us

**vscode : Ctrl + Shift + X , 装外挂
	Git history
	Python
	Django Template
	jquery Code Snippets
	Bootstrap 3 Snippets
	
建list.txt  ,  pip可以txt批次安装
	django<1.10
	pylint
	pylint-django
	autopep8
	
virtualenv
	刷建虚拟目录结构 , 在cmder，cd到目录C:\__code\python\DJANGO , 执行 virtualenv env  刷建目录结构 
	进入虚拟环境 , 贴到cmder执行 "C:\__code\python\DJANGO\env\Scripts\activate.bat" 
	安装相关模块 , 执行 pip install -r list.txt 
	刷建django目录 , 执行 django-admin startproject pro1 
	cd pro1
	新建django app , 执行 python manage.py startapp app1 
	执行 code . 在当前配置打开vscode项目 , vscode 进到env 目录
	
	vscode : Ctrl + Shift + P
		interpre -> Python: Select Workspace Interpreter
		在出现的选项中将Python解析器指向env文件夹中的python
	vscode : Ctrl + Shift + P
		workspace -> Preferences: Open Workspace Settings
			{
				"python.pythonPath": "e:/temp/django_demo/env/scripts/python.exe",
				"python.linting.pylintPath": "pylint",
				"python.linting.pylintArgs": [
					"--load-plugins", "pylint_django"
				],
				"python.formatting.autopep8Path": "autopep8"
			}


			
#大老板开专案给PM，PM开APP CASE
django_admin.py
	/proj1/manage.py
		/app1
		/app2
	/proj2/manage.py
		/app3344
		/app8899

建立 proj
	环境里任何路径 : django_admin.py startproject proj1
		#在环境里django_admin.py已经是全域，大老板脚色

建立app
	进入到proj下面路径，用proj1的manage.py，开一个app : manage.py startapp app1
		#要开APP CASE，要找到对的专案经理PM，也就是manage.py

把app加到proj的app list
	/proj1/settings.py的INSTALLED_APPS，加上'app1'
		
建立proj的db
	proj路径下，刷出sqlite3的db : 
	manage.py makemigrations app3
	manage.py migrate app3
		
设定的proj的后台admin
	manage.py createsuperuser
	
把proj1的web run起来，去127.0.0.1/admin    后台试试
	manage.py runserver
		
ok后，去github建个新仓库把东西git进入
git remote add origin https://github.com/gameyayaya/hel lo_django.git
git push -u origin master

		
************
1.proj/url  建立网页/hello ， 映射对应的funtion:hello_view
2.app/views 定义funtion内容 ， 链结到app/template里的html #template必须放在app下



1.proj/url  建立网页/hello ， 链结对应的funtion
	from django.conf.urls import url
	from django.contrib import admin
	#from app3.views import hello_view

	urlpatterns = [
		url(r'^admin/', admin.site.urls),
		#url(r'^hello/', hello_view),
	]


2.app/views 定义funtion内容 ， 链结到app/template里的html #template必须放在app下
app/views.py
	def hello_view(request):
    return render(request, 'hello_django.html', {
        'data': "Hello Django ", #把变数data  设为文字Hello Django
    })

app/templates/hello_django.html
		<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Title</title>
	</head>
	<body>
		{{data}}
	</body>
	</html>
