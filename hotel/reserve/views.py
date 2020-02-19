from django.shortcuts import render
from .forms import reserveform
from .models import reserve
from all import all_category
from all_hotels.models import Hotel, Category
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect

def  reserve(request, id):
    if request.user.is_authenticated():
        if request.method =='GET':
            context ={
            'category':all_category.getAllCategory(),
            'hotel':Hotel.objects.get(id=id),
            'form':reserveform(),
            }
            return render(request,'reserve.html',context)
        else:
            form = reserveform(request.POST or None)
            if form.is_valid():
                form.save()
                context = {
                'category':all_category.getAllCategory(),
                'hotel':Hotel.objects.get(id=id),
                'form':reserveform(),
                'msg':'You Have Successfully Reserved',
                }
                return render(request,'reserve.html',context)
    else:
        return redirect('login')
