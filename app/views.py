from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

stocks = [
    {'分類': '日經指數', '指數': '22,920.30'}, {'分類': '日經指數', '指數': '22,920.30'}, {
        '分類': '日經指數', '指數': '22,920.30'}, {'分類': '日經指數', '指數': '22,920.30'}
]


def index(request):
    str1 = "<h1>Hello Django World</h1>"
    return HttpResponse(str1)


def get_stocks(request):
    return render(request, "stocks.html", {'stocks': stocks})
