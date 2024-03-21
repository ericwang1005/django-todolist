1. 安裝 Django

- pip install django

2. 創建專案

- django-admins startproject [project name]

3. 啟動 Server

- python manage.py runserver

4. 資料庫同步(初登入 django admin 後台)

- python manage.py makemigrations
- python manage.py migrate

5. 建立超級使用者

- python manage.py createsuperuser

6. 新增功能 app

- python manage.py startpp [application name]
  - settings.py
    - install app
    - "[application name].apps.[application name]Config" .

7. 在各個 app 當中新增獨立的 template

- [application name]/templates/[application name]
