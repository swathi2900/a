from django.shortcuts import render
from django.contrib import messages
from user.models import Usermodel

import os
import pickle
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def Userlogin(request):
    return render(request, "user/Userlogin.html")

def userregister(request):
    return render(request, "user/userregister.html")

def userregisterAction(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upasswd')
        phoneno = request.POST.get('uphonenumber')
        form1 = Usermodel(name=name, email=email, password=password, phoneno=phoneno, status='waiting')
        form1.save()
        messages.success(request, 'Registration Successful')
        return render(request, "user/Userlogin.html")
    else:
        messages.error(request, 'Registration Unsuccessful')
        return render(request, "user/userregister.html")

def userloginaction(request):
    if request.method == 'POST':
        sname = request.POST.get('email')
        spasswd = request.POST.get('upasswd')
        try:
            check = Usermodel.objects.get(email=sname, password=spasswd)
            status = check.status
            if status == 'activated':
                messages.success(request, 'Login Successful')
                return render(request, "user/userhome.html")
            else:
                messages.error(request, 'Login Unsuccessful')
                return render(request, "user/Userlogin.html")
        except:
            messages.error(request, 'Login Unsuccessful')
            return render(request, "user/Userlogin.html")
    else:
        messages.error(request, 'Login Unsuccessful')
        return render(request, "user/userhome.html")

def predict(request):
    return render(request, "user/userhome.html",{})

def usrlogout(request):
    return render(request, "user/userlogin.html")

def predicts(request):
    if request.method == 'POST':
        l1 = request.POST.get('input1')
        l2 = request.POST.get('input2')
        l3 = request.POST.get('input3')
        l4 = request.POST.get('input4')
        l5 = request.POST.get('input5')
        l6 = request.POST.get('input6')
        l7 = request.POST.get('input7')
        l8 = request.POST.get('input8')
        l9 = request.POST.get('input9')
        l10 = request.POST.get('input10')
        with open(os.path.join(BASE_DIR, 'media/ba_rf_model'), 'rb') as f:
            rf = pickle.load(f)

        y_pred = rf.predict([[l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]])

        context = {'prediction': y_pred}
        return render(request, 'user/userhome.html', context)
    else:
        return render(request, 'user/userhome.html')
