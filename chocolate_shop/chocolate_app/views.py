from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Customer_details

# Create your views here.
def home(request):
    return render(request,'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already used")
                return redirect('chocolate_app:register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('chocolate_app:login')

        else:
            messages.info(request,"password doesn't match")
            return redirect('chocolate_app:register')


    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('chocolate_app:shop')
        else:
            messages.info(request,"invalid username or password")
            return redirect('chocolate_app:login')
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('chocolate_app:home')

def shop(request):
    return render(request,'shop.html')


def confirm(request):
    if request.method == 'POST':
        customer_name=request.POST['customer_name']
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST['district']
        city = request.POST['city']
        chocolate = request.POST['chocolate']
        price = request.POST['price']
        quantity = request.POST['quantity']
        data=Customer_details(customer_name=customer_name,phone_no=phone_no,email=email,address=address,district=district,city=city,chocolate=chocolate,price=price,quantity=quantity)
        data.save();
        if data:
            messages.info(request,"success")
    return render(request,'confirm.html')