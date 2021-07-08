from Jigsapp.models import Users
from django.http.response import HttpResponse
from django.shortcuts import render
import requests,json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    url = 'https://reqres.in/api/users?page=2'
    #url = 'https://reqres.in/api/login'

    dat = requests.get(url).json()
    # print(dat.text)

    alldata = dat['data']
    # print(alldata)

    for data in alldata:
        users = Users(first_name=data['first_name'],email=data['email'],avtar=data['avatar'])
        users.save()
    
    return render(request, 'index.html')


def showData(request):
    userData = Users.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(userData, 6)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'users':users})


def loginData(request):
    if request.method == "POST":
        unm = request.POST.get('username')
        password = request.POST.get('password')

    return render(request, 'index.html')