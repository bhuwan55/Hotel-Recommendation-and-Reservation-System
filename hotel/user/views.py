from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from all_hotels.models import Rate,Hotel
from all import all_category
import numpy as np
import pandas as pd
from django.db.models import Max
# Create your views here.

def dashboard(request):
    try:
        myrate = Rate.objects.filter(user_id=request.user.id).aggregate(Max('rating'))
        hotel = Rate.objects.filter(rating=myrate['rating__max'])[0]
        hotel_list = tuple(matrixfactorizatin(str(hotel.hotel)))
        recommended_hotel = Hotel.objects.filter(name__in=hotel_list)
    except:
        recommended_hotel = Hotel.objects.all()
    context = {
    'category':all_category.getAllCategory(),
    'hotel':recommended_hotel,
    }
    return render(request,'dashboard.html',context)

def register(request):
    if request.method=='GET':
        context = {
        'form':UserCreationForm(),
        'category':all_category.getAllCategory(),
        }
        return render(request,'registration/register.html',context)
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return redirect('user:login')
        else:
            return render(request,'registration/register.html',{'form':form,'category':all_category.getAllCategory(),})


def matrixfactorizatin(hotel_name):
    df = pd.DataFrame(list(Rate.objects.all().values()))
    hotel_df = pd.DataFrame(list(Hotel.objects.all().values()))
    print(hotel_df)
    hotel_df.rename(columns=lambda x: x.replace('id', 'hotel_id'), inplace=True)
    df = pd.merge(df,hotel_df,on='hotel_id')
    rating = pd.DataFrame(df.groupby('name')['rating'].mean().sort_values(ascending=False))
    rating['num_of_rating'] = pd.DataFrame(df.groupby('name')['rating'].count())
    matrix = df.pivot_table(index='user_id',columns='name',values='rating')
    print(matrix)
    hotel = matrix[hotel_name]
    similar_to_hotel= matrix.corrwith(hotel)
    print(similar_to_hotel)
    rec = pd.DataFrame(similar_to_hotel,columns=['correlation'])
    rec = rec[(rec['correlation']>-0.1)]
    myhotel = rec.index
    myhotel  = myhotel.tolist()
    return myhotel

# Create your views here.
