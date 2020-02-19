from django.shortcuts import render, redirect
from django.http import HttpResponse
from all import all_category
from .models import Hotel, Category, Reserve, Rate
from django.contrib.auth.models import User
from .forms import RateForm
from .reserveform import reserveform
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView

# from django.core.urlresolvers import reverse_lazy

# Create your views here.
def category_hotel(request,id):
    context = {
    'category':Category.objects.all(),
    'hotel':Hotel.objects.filter(category=id),
    'cat':Category.objects.get(id=id),
    }
    return render(request,'hotel_list.html',context)

def hotel(request,id):
    context = {
    'category':all_category.getAllCategory(),
    'hotel':Hotel.objects.get(id=id)
    }
    return render(request,'hotel.html',context)

def rate(request,id):
    if request.user.is_authenticated:
        if request.method =='GET':
            context = {
            'category':all_category.getAllCategory(),
            'hotel':Hotel.objects.get(id=id),
            'form':RateForm(),
            }
            return render(request,'rate_hotel.html',context)
        else:
            form = RateForm(request.POST)
            if form.is_valid():
                myrate = form.save(commit=False)
                hot = Hotel.objects.get(id = id)
                myrate.hotel = hot
                us = User.objects.get(id=request.user.id)
                myrate.user = us
                myrate.save()
                context = {
                'category':all_category.getAllCategory(),
                'hotel':Hotel.objects.get(id=id),
                'form':RateForm(),
                'msg':'Thanks for rating us',
                }
                return render(request,'rate_hotel.html',context)
    else:
        return redirect('user:login')


def detailhotel(request,id):
    ratings = average_rating()
    context = {
    'category':all_category.getAllCategory(),
    'hotel':Hotel.objects.get(id=id),
    }
    return render(request,'hotel.html',context)



def  reserve(request, id):
    if request.user.is_authenticated:
        if request.method =='GET':
            context ={
            'category':all_category.getAllCategory(),
            'hotel':Hotel.objects.get(id=id),
            'form':reserveform(),
            }
            return render(request,'reserve.html',context)
        else:
            form = reserveform(request.POST)
            if form.is_valid():
                myreserve = form.save(commit=False)
                hot = Hotel.objects.get(id = id)
                myreserve.hotel = hot
                us = User.objects.get(id=request.user.id)
                myreserve.user = us
                form.save()
                context = {
                'category':all_category.getAllCategory(),
                'hotel':Hotel.objects.get(id=id),
                'form':reserveform(),
                'msg':'You Have Successfully Reserved',
                }
                return render(request,'reserve.html',context)
            else:
                context = {
                'category':all_category.getAllCategory(),
                'hotel':Hotel.objects.get(id=id),
                'form':reserveform(),
                'msg':'invalid form',
                 }
                return render(request,'reserve.html',context)

    else:
        return redirect('user:login')
