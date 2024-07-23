from django.shortcuts import redirect, render,HttpResponse
from agroplus.models import Sell,price
from datetime import datetime
import requests
import pandas as pd 
import json

# FOR LOGIN AND LOGOUT 

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm
from django.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def farmercorner(request):
    data = Sell.objects.all()
    return render(request, 'farmercorner.html',{'data': data})

def Buy(request):
    data = Sell.objects.all()
    return render(request, 'Buy.html',{'data': data})

def SellFun(request):
    if request.method == "POST":
        SellerName = request.POST.get('SellerName')
        CropName = request.POST.get('CropName')
        # Image = request.POST.get('Image')
        Image = request.FILES.get('Image')
        # Price = request.POST.get('Price')
        Description = request.POST.get('Description')
        imgpath = request.POST.get('imgpath')
        # imgpath = 'media/'+imgpath
        # if(not Image):
        #     Image= "static/Sell_images/AGROPLUS.png"
        # data2=price.objects.filter(CropName=CropName)
        sample_instance = price.objects.get(CropName=CropName)
        value= sample_instance.Price
        print(value)
        sell = Sell(SellerName=SellerName,CropName=CropName,Image=Image,Price=value,Description=Description,imgpath=imgpath,date=datetime.now())
        sell.save()
        return redirect('Buy')
    return render(request, 'Sell.html')

def Croprate(request):
    # data = pd.read_csv("../project/static/dataset.csv")
    # pune_data = data[data['district']=='Pune']
    # html_table = dataframe.to_html()
    dataframe = pd.read_csv("./static/dataset.csv")
    search = 'a'
    if request.method == 'POST':
        search = request.POST.get('district')
        print(search)
        if(search != 'a'):
            dataframe = dataframe[dataframe["District"] == search]
            dataframe = dataframe
        # elif(len(search) <= 1):
        #     # dataframe = dataframe[dataframe["District"] == search]
        #     print(dataframe)
        #     # dataframe = pd.read_csv("./static/dataset.csv")
    else:
         dataframe = pd.read_csv("./static/dataset.csv")
         
    json_records = dataframe.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    
    return render(request, 'croprate.html', context)


def loginpage(request): 
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            #authenticate user

            user = authenticate(request, username=username, password=password)

            if user is not None :
                login(request, user)
                return redirect('home')
            else :
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'login.html')

def feedback(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request, 'feedback.html')
    
def logoutUser(request):
    logout(request)
    return redirect('feedback')


def registerpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:    
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account Created successfully for '+ user)
                return redirect('login')
        context = {'form':form}
        return render(request, 'register.html',context)
    
# def pricecal(CropName):
#     data = price.objects.get(CropName=CropName)
#     Price = getattr(data, CropName)
#     return Price
    # context = {
    #     'html_table' : html_table,
    #     'data' : data,
    #     'cols' : data.columns,
    #     'row_len' : len(data),
    #     'col_len' : len(data.columns)
    # }

    # return render(request,'croprate.html', context=context)
    # return render(request,html_table, context=context)
    # return HttpResponse(html_table)

