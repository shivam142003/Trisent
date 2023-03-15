from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import products, contact, food

def index(request):
    p=products.objects.all()
    context={'p':p}
    return render(request,'index.html',context)


def register(request):
    if request.method =='POST':
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        password2=request.POST["password2"]

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exist')
                return redirect(register)
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exist')
                return redirect(register)
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'invalid password')
            return redirect(register)
    else:
        return render(request,'register.html')

    
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user= auth.authenticate(username=username,password=password)    

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Not registered')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



# def counteer(request):
#     text=request.GET['text']
#     no_of_words=len(text.split())
#     return render(request,'counteer.html', {'word': no_of_words})


def thrift(request):
    return render(request,'thrift.html',{})

def travel(request):
    return render(request,'travel.html',{})


def search_results(request):
    if request.is_ajax():
        products=request.POST.get('products')
        print(products)
        return JsonResponse({'data':products})
    return JsonResponse

def homedecor(request):
    return render(request,'homedecor.html',{})


def CultureNew(request):
    return render(request,'CultureNew.html',{})


def Contact(request):

    if request.method== "POST":
        Contact=contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        Contact.name= name
        Contact.email= email
        Contact.message= message
        contact.subject=subject
        Contact.save()
        messages.success(request,"message sent successfully")
        return HttpResponseRedirect('/')


def foods(request):
    Name=request.GET.get('Name')
    foods= food.objects.all()
    if Name:
        foods=foods.filter(name_icontains=Name)
    context={
        # 'form':foodNameFilterForm(),
        'foods':foods
    }
    return render(request,'food.html',context)