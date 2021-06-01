from django.shortcuts import render,redirect
from .forms import adduserform,loginform,createaccountform
from .models import User

def adduser(request):
    context={}
    form=adduserform()
    context["form"]=form#"form" is key value
    if request.method=="POST":
        form=adduserform(request.POST)
        if form.is_valid():
            fname=form.cleaned_data.get("firstname")
            lname=form.cleaned_data.get("lastname")
            email=form.cleaned_data.get("email")
            password=form.cleaned_data.get("password")
            confirmpassword=form.cleaned_data.get("confirmpassword")
            username=form.cleaned_data.get("username")
            user=User(fristname=fname,lastname=lname,email=email,
                      password=password,username=username)
            user.save()
            return redirect("login")
        else:
            context["form"] = form
        return render(request, "bankapp/adduser.html", context)
    return render(request,"bankapp/adduser.html",context)


def login(request):
    context={}
    form= loginform()
    context["log"]=form
    if request.method == "POST":
        form=loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username,password)
            return redirect("adduser")
    return render(request,"bankapp/login.html",context)


def createaccount(request):
    form = createaccountform()
    context = {}
    context["create"]=form
    if request.method == "POST":
        form = createaccountform(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            accountnum = form.cleaned_data.get("accountnum")
            acctype = form.cleaned_data.get("acctype")
            min_bal = form.cleaned_data.get("min bal")
            account=Accounts(username=username,accountnum=accountnum,acctype=acctype,min_bal=min_bal)
            account.save()
            return redirect("adduser")
        else:
            context["form"]=form
        return render(request, "bankapp/adduser.html", context)
    return render(request,"bankapp/createaccount.html",context)