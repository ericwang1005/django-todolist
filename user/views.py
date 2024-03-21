from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def user_logout(request):
    logout(request)
    return redirect('login')


def user_profile(request):
    return render(request, "user/profile.html", {'user': request.user})


def user_login(request):
    message = ''
    if request.method == 'POST':
        if request.POST.get('register'):
            return redirect('register')
        elif request.POST.get('login'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username == '' or password == '':
                message = 'Account or Password Can Not Be Empty!'
            else:
                user = authenticate(
                    request, username=username, password=password)
                if user:
                    login(request, user)
                    message = '登入成功!'
                    return redirect(
                        "todo"
                    )
                else:
                    message = '帳號或密碼錯誤'
    return render(request, "user/login.html", {'message': message})


def user_register(request):
    message = ''
    form = UserCreationForm()
    # 取得所有All
    # 取得唯一get
    # 取得篩選filter
    # print(User.objects.filter(username,password))
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        # print('POST', request.POST)
        print(username, password1, password2)
        if len(password1) < 8:
            message = '密碼長度包含至少8個字元'
        elif password1 != password2:
            message = '兩次密碼不相同'
        else:
            User.objects.create_user(
                username=username, password=password1).save()
            message = '註冊成功!'
    return render(request, "user/register.html", {'form': form})
