from django.shortcuts import redirect,render
from all import all_category
from all_hotels.models import Hotel,Category
# Create your views here.

def index(request):
    context = {
    'category':all_category.getAllCategory()[:7],
    }
    return render(request,'index.html',context)

def contactus(request):
    context = {
    'category':all_category.getAllCategory()[:7],
    }
    return render(request,'contactus.html',context)


def team(request):
    context = {
    'category':all_category.getAllCategory()[:7],
    }
    return render(request,'team.html',context)


def search(request):
    if request.method=='GET':
        return redirect('home')
    else:
        keyword = request.POST.get('key')
        hotel = Hotel.objects.filter(name__contains=keyword)
        context = {
        'searchhotel':hotel,
        }
        return render(request,'search_result.html',context)


def searchloc(request):
    if request.method=='GET':
        return redirect('home')
    else:
        keyword = request.POST.get('key')
        hotel = Hotel.objects.filter(location__contains=keyword)
        context = {
        'searchhotel':hotel,
        }
        return render(request,'search_result0.html',context)
