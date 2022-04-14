from ast import Num
from audioop import add
from email.headerregistry import Address
from platform import uname
from unicodedata import category
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from . models import *
from django.http import HttpResponse
from django.contrib import messages

from django.db.models.query_utils import Q


# Create your views here.


def hello(request):
    return HttpResponse("You are in priority................")

def SignupView(request):
    if request.POST: 
        Name = request.POST['name']
        Email = request.POST['email']
        Number = request.POST['number']
        Address = request.POST['address']
        Password = request.POST['password']
        ConfirmPassword = request.POST['confirmPassword']
        try:
            data = signUp.objects.filter(email=Email)
            if data:
                msg = "Email already registered"
                return render(request, 'sign-up.html', {'msg': msg})
            elif ConfirmPassword == Password:
                v = signUp()
                v.name = Name
                v.email = Email
                v.number = Number
                v.address = Address
                v.password = Password
                v.save()
                print(f"{v.name} Signed up successfully")
                return redirect('LOGIN1')
            else:
                msg = 'Please Enter Same Password'
                return render(request , 'sign-up.html',{'msg':msg}) 
        finally:
            messages.success(request, 'Signup Successfully Done...')
    return render(request,'sign-up.html')

def userLogin(request):
    if request.POST:
        print("inside login")
        em = request.POST.get('email')
        pass1 = request.POST.get('password')
      
        print("Inside first try block", em)

        check = signUp.objects.get(email = em)

        print("Email is ",em)
        if check.password == pass1:
            request.session['email'] = check.email
            print(f'{check.name} Successfully logged in')
            return redirect('INDEX')
        else:
            msg = 'Invalid Password'
            return render(request,'sign-in.html', {'msg': msg})
            # return HttpResponse('Invalid Password')
    return render(request,'sign-in.html')


def dashboard(request):
    if 'email' in request.session:
        name = signUp.objects.get(email = request.session['email'])
        
        if request.POST:
            prob = request.POST['problem']
            print(prob)
        
            db = Problems()
            db.problem = prob
            db.isappoved = 0  
            db.owner = name
            db.save()
        # to show the approved problem
        probl = Problems.objects.filter(owner=name)
        print(probl)
        
        return render(request,'dashboard.html', {'name': name, 'probl': probl})
    return redirect('LOGIN1')


def problem (request):
    if 'email' in request.session:
        name = signUp.objects.get(email = request.session['email'])
        
        if request.method == 'POST':
            prob = request.POST.get('problem')
            print(prob)
        
            db = Problems()
            db.problem = prob
            db.isappoved = 0  
            db.count = 1    
            db.owner = name
            db.save()
            msg = 'Your problem has been saved properly'
            return render(request,'problem.html', {'msg': msg})
            
        # to show the approved problem
        probl = Problems.objects.filter(owner=name)
        print(probl)
        
        return render(request,'problem.html', {'name': name, 'probl': probl})
    return redirect('LOGIN1')

def allProblem(request):
    if 'email' in request.session:
        name = signUp.objects.get(email = request.session['email'])
       
        # to show the all the POSTED problems
        allProblems = Problems.objects.all()
        # print(allProblems)
        
        if request.method == 'POST':
            plus = int(request.POST.get('plus'))
            idOfProb = request.POST.get('idOfProb')
            current = Problems.objects.get(id = idOfProb)
            print(current,"This is showing the problem")
            if current:
                try:
                    vot=Voting.objects.get(user=name,issue=current)
                    print("Already Voted")
                except:
                    v = Voting()
                    v.user = name
                    v.issue = current
                    v.save()
                    current.count += plus
                    name.isvoted = True
                    name.save()
                    current.save()

                msg = 'Your problem is saved Successfully'
                return redirect('ALLPROBLEM')
            
        return render(request,'allProblem.html', {'name': name, 'allProblems': allProblems})
    return redirect('LOGIN1')


def userLogOut(request):
    del request.session['email']
    print('User logged out successfully')
    return redirect('LOGIN1')

def index (request): 
    if 'email' in request.session:
        name1 = signUp.objects.get(email=request.session['email'])
        name2 = name1.name
        name = name2.capitalize()
        return render(request, 'index.html', {'name': name})
    return redirect('LOGIN1')

def about (request): 
    return render(request, 'about.html')

def contact (request): 
    print('Contact')
    msg = ''
    if request.method == 'POST':
        db = ContactForm(name = request.POST.get('name'), email = request.POST.get('email'), subject = request.POST.get('subject'), message = request.POST.get('message'))
        db.save()
        msg = "Message Sent Successfully"
    return render(request, 'contact.html', {'msg': msg})

def faqs (request): 
    return render(request, 'faq.html')

def productDetail (request): 
    return render(request, 'product-detail.html')

def products (request): 
    return render(request, 'products.html')

def signup1 (request): 
    return render(request, 'sign-up.html')

def login1 (request): 
    return render(request, 'sign-in.html')
