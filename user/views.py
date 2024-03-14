from django.shortcuts import render

# Create your views here.


def user_regist(request):

    return render(request, "user/register.html")
