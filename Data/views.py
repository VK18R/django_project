from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader 
from .models import Contact
def data(request):
    template=loader.get_template("index.html")
    return HttpResponse(template.render())
def data2(request):
    template=loader.get_template("register.html")
    return HttpResponse(template.render())
def submit(request):
    template=loader.get_template("test.html")
    template1=loader.get_template("index.html")
    if request.method=="GET":
        user=request.GET.get("user")
        pswd=request.GET.get("pswd")
        C1=Contact.objects.filter(name=user,password=pswd).values()
        db=Contact.objects.all().values()
        if C1:
            context={
                "user":user,
                "username": db,
                }
            return HttpResponse(template.render(context,request))
        else:
            context={
                "Invalid":"INVALID USER...!",
            }
            return HttpResponse(template1.render(context,request))
    else:
        return HttpResponse("<h3 style='color:red'>Please Check the method</h3>")
def my_view(request):
    template=loader.get_template("register.html")
    print("registration successful..")
    if request.method=="GET":
        field_1=request.GET.get('user')
        field_2=request.GET.get('address')
        field_3=request.GET.get('email')
        field_4=request.GET.get('pass')
        field_5=request.GET.get('phone')
        if field_2=="":
            field_2="NA"
        new_insta=Contact(name=field_1,email=field_3,password=field_4,phone=field_5,address=field_2)
        new_insta.save()
        context={
            "datab":"Registered successfully",
        }
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponse("user not allowed...")
