from django.shortcuts import render
from .models import reciepe_model
from django.http import HttpResponse
from .models import URLHitCount


# register 
from django.contrib.auth.models import User
from django.contrib import messages
def registerView(request):
    print(request.method)
    #this iis jflkdsajfdlajfaj;flkdajfljdalkfdajklfadssjfdlk
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

# djagno authentication module
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
        #session manage agar sassion valid hai to use automatic login ho jaega
        login(request,user_check)
        return redirect("form")
    return render(request,"login.html")

#get
def formView(request):
    if request.method.lower() == "get":
        #hit count
        current_url = request.path_info
        url_hit_count, created = URLHitCount.objects.get_or_create(url=current_url)
        url_hit_count.hit_count += 1
        url_hit_count.save()
        #------------        
        return render(request, "index.html")
#post
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
def searchView(request):
    search_value = request.POST.get('search')
    data = reciepe_model.objects.filter(Q(name__icontains = search_value) | Q(price__icontains=search_value) | Q(description__icontains=search_value)).order_by('-id')
    return render(request,"index.html",{"data":data})

# price range
def pricerenageView(request):
    min_value = request.POST['min_value'] if request.POST['min_value'] !="" else 0
    max_value = request.POST['max_value'] if request.POST['max_value'] !="" else 0
    if min_value !=0 and max_value !=0:
        range_value = reciepe_model.objects.filter(Q(price__gte = min_value) & Q(price__lte = max_value))
    
    elif min_value !=0:
        range_value = reciepe_model.objects.filter(Q(price__gte = min_value))
    
    elif max_value !=0:
        range_value = reciepe_model.objects.filter(Q(price__lte = max_value))
    else:
        range_value = reciepe_model.objects.all()

    return render(request,"index.html",{"data":range_value})

    

