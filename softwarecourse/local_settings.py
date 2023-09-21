LANGUAGE_CODE = 'zh-hans'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '12345',  # 数据库用户密码
        'NAME': 'work'  # 数据库名字
    }
}