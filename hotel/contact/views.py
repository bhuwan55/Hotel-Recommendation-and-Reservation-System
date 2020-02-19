from django.shortcuts import render, redirect
from .forms import contactform
from .models import Cancel_request
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect

def  contact(request):
    if request.user.is_authenticated:
        if request.method =='GET':
            context ={
            'form':contactform(),
            }
            return render(request,'contactus.html',context)
        else:

            form = contactform(request.POST)
            if form.is_valid():
                mycontact= form.save(commit=False)
                us = User.objects.get(id=request.user.id)
                mycontact.user = us
                form.save()
                context = {
                'form':contactform(),
                'msg':'Your request was sent',
                }
                return render(request,'contactus.html',context)
            else:

                context = {
                'form':contactform(),
                'msg':'invalid request',
                 }
                return render(request,'contactus.html',context)

    else:
        return redirect('user:login')
