from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")
def restaurant(request):
    return render(request, "restaurant.html")
def floyd(request):
    return render(request, "floyd.html")
def recreation(request):
    return render(request, "recreation.html")
def showrec(request):
    return render(request, "showrec.html")
def recreational(request):
    return render(request, "recreation.html")
def showuniversity(request):
    return render(request, "showuniversity.html")
def university(request):
    return render(request, "university.html")
def showmall(request):
    return render(request, "showmall.html")
def mall(request):
    return render(request, "mall.html")
