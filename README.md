1. 安裝Django
  - pip install django
2. 創建專案
  - django-admins startproject [project name]
3. 啟動Server
  - python manage.py runserver
4. 資料庫同步(初登入django admin後台)
  - python manage.py migrate
5. 建立超級使用者
  - python manage.py createsuperuser
6. 新增功能app
  - python manage.py startpp [application name]
    - settings.py
        - install app
        - "user.apps.UserConfig" .
7. 在各個app當中新增獨立的template
  - user/templates/user
