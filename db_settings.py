DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",  # 엔진
        "NAME": "inneats_db",  # 데이터베이스 이름
        "USER": "root",  # 사용자
        "PASSWORD": "1234",  # 비밀번호
        "HOST": "localhost",  # 호스트
        "PORT": "3306",  # 포트번호
    }
}

SECRET_KEY = 'django-insecure-db^bgawm^oz-v1xtwbabfuk%9%l)04d4w&%sz5ir^ameaxjg26'
