from django.shortcuts import render
from .models import reciepe_model
from django.http import HttpResponse
from .models import URLHitCount

#iska use karne pe hamare url ko vahi use kar paega jo login hoga 
from django.contrib.auth.decorators import login_required

# register 
from django.contrib.auth.models import User
from django.contrib import messages
def registerView(request):
    print(request.method)
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username = username).exists():
            messages.error(request,"username must be unique")
            return render(request,"register.html")
        
        data = User.objects.create(first_name = first_name,
                                last_name = last_name,
                                username = username,
                                )
        data.set_password(password)
        data.save()
        return redirect("/form/")

    return render(request, "register.html")

# djagno authentication login
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
def loginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user_check = authenticate(username = username, password = password)
        if user_check is None:
            Warning = "Username and password not mach"
            return render(request,"login.html",{"warning":Warning})
        #session manage/agar sassion valid hai to user automatic login ho jaega
        login(request,user_check)
        return redirect("form")
    return render(request,"login.html")

#logout 
from django.contrib.auth import logout 
def logoutView(request):
    logout(request)
    return redirect("/login/")
    
# aggregation ke lie import module
from django.db.models import Count,Avg,Sum,Min,Max
#get
@login_required(login_url="/login/")
def formView(request):
    if request.method.lower() == "get":
        #aggregation
        count_find = reciepe_model.objects.aggregate(Count('price'))
        avarage_find = reciepe_model.objects.aggregate(Avg('price'))
        sum_find = reciepe_model.objects.aggregate(Sum('price'))
        min_find = reciepe_model.objects.aggregate(Min('price'))
        max_find = reciepe_model.objects.aggregate(Max('price'))
        print("count_find:",count_find['price__count'],"sum_find:",sum_find['price__sum'],"avarage_find:",avarage_find['price__avg'],"min_find:",min_find['price__min'],"max_find:",max_find['price__max'],"aaaaaaaaaaaaaaaaaaaa")
        # datafilter = reciepe_model.objects.filter(price=min_find["price__min"]) 
        # print(datafilter)
        
        #annotation
        annotatedata = reciepe_model.objects.values('price').annotate(Min('id'))
        print(annotatedata,"aaaaaaaaaaaaaaaaaaaa")      
        
        #hit count
        current_url = request.path_info
        url_hit_count, created = URLHitCount.objects.get_or_create(url=current_url)
        url_hit_count.hit_count += 1
        url_hit_count.save()
        #------------   
        data = reciepe_model.objects.all().order_by('name')
        return render(request, "index.html",{"data":data})

#post
@login_required(login_url="/login/")
def reciepepostView(request):
    if request.method == "POST":
        name = request.POST['name'] if  request.POST['name']!="" else ""
        image = request.FILES['image'] 
        price = request.POST['price'] if  request.POST['price']!="" else ""
        description = request.POST['description'] if  request.POST['description']!="" else ""
        data = reciepe_model.objects.create(name=name,image=image,price=price,description=description)
        ddd = reciepe_model.objects.all().order_by("-id")
    return render(request, "index.html",{"data":ddd})

#search
from django.db.models import Q
@login_required(login_url="/login/")
def searchView(request):
    search_value = request.POST.get('search')
    data = reciepe_model.objects.filter(Q(name__icontains = search_value) | Q(price__icontains=search_value) | Q(description__icontains=search_value)).order_by('-id')
    return render(request,"index.html",{"data":data})

# price range
@login_required(login_url="/login/")
def pricerenageView(request):
    min_value = request.POST['min_value'] if request.POST['min_value'] !="" else 0
    max_value = request.POST['max_value'] if request.POST['max_value'] !="" else 0
    if min_value !=0 and max_value !=0:
        range_value = reciepe_model.objects.filter(Q(price__gte = min_value) & Q(price__lte = max_value)).order_by("-id")
    
    elif min_value !=0:
        range_value = reciepe_model.objects.filter(Q(price__gte = min_value)).order_by("-id")
    
    elif max_value !=0:
        range_value = reciepe_model.objects.filter(Q(price__lte = max_value)).order_by("-id")
    else:
        range_value = reciepe_model.objects.all().order_by("-id")

    return render(request,"index.html",{"data":range_value})

    

