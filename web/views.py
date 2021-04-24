from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url='login')
def index(request):
    return render(request,"index.html")

def userPage(request):
    context= {}
    return render(request,'templates/user.html',context)



