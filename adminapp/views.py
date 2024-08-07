from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
import re
import sweetify
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth import logout
from django.template import loader
from . models import *
from datetime import datetime
from django.contrib.auth.decorators import login_required 

# Create your views here.

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
          sweetify.error(request, 'Enter valid username and password')     
    return render(request,"adminn/admin_login.html")

@login_required
def dashboard(request):
    type_data = "dashboard"
    prod= Blog.objects.all().count()
    print('prod',prod)
    context = {
        'type_data':type_data,
        'blog_count':prod
    }
    return render(request,"adminn/dashboard.html",context)
@login_required
def blog(request):
    type_data = "Blog"
    prod= Blog.objects.all()    
    c=0
    context = {
        'type_data': type_data,
        'data':prod
    } 
    return render(request,"adminn/blog.html",context)

##########################
@login_required
def create_blog(request):
    if request.method == "POST":
        print('*****************************************************')
        name = request.POST.get("auther_name")
        date= request.POST.get("date")
        image = request.FILES.get("image")
        title= request.POST.get("title")
        description= request.POST.get("description")
        status = request.POST.get('status') == 'on'

     
        required_fields = []

        if not name:
            required_fields.append("name")
        if not date:
            required_fields.append("date")
        if not image:
            required_fields.append("image")
        if not title:
            required_fields.append("title")
        if not description:
            required_fields.append("description")
        if not description:
            required_fields.append("status")
        if required_fields:
    
            response = f"{', '.join(required_fields)} are required"
            return JsonResponse({"message": response, "status": "error"})
        else:
            blog= Blog.objects.create(auther_name=name,date=date,image=image,title=title,description=description,status=status)
 
            return JsonResponse({"message": "success", "status": "success"})
    return render(request,"adminn/blog.html")  

@login_required
def edit_blog(request):

    id = request.GET.get("id")
    data = Blog.objects.get(id=id)
    template = loader.get_template('adminn/edit_blog.html')
    context={}
    context['data']=data
    print("context",context)
    rendered_template = template.render(context, request)
    return JsonResponse({"rendered_template":rendered_template})

@login_required
def delete_blog(request):
   
    id = request.GET.get("id")
    required_fields=[]
    if id:
         prod = Blog.objects.get(id=id)
         prod.delete()
         return JsonResponse({"message": "success", "status": "success"})
@login_required    
def edit_blog_action(request):
  if request.method == "POST":
        id = request.POST.get("product_id")
        username = request.POST.get("product_name")
        image_change = request.POST.get("image_change")
        title = request.POST.get("title")
        description = request.POST.get("description")
        date = request.POST.get("date")
        product_image=request.FILES.get('product_image')
        # date = datetime.strptime(date, '%d/%m/%Y')
        # convert datetime format into %Y-%m-%d-%H:%M:%S
        # format using strftime
        # date=d.strftime("%Y-%m-%d")
   
        ##################################
        #logic to access the image from backend 
        # if request.FILES :
        #     product_image=request.FILES.get('product_image',None)
        
   
        # required_fields = []
        # if 'product_image' in request.FILES:
        #     data_save = Blog.objects.get(id=id)
        #     data_save.image = product_image
        #     data_save.save()

        ##########################################
        required_fields = []
        if image_change != "no":
            data_save = Blog.objects.get(id=id)
            data_save.image = product_image
            data_save.save()
        # if not username:
        #     required_fields.append("Username")
        # if not image:
        #     required_fields.append("image")
        # if required_fields:
        #     response = f"{', '.join(required_fields)} are required"
        #     return JsonResponse({"message": response, "status": "error"})
        
        

        if username:
            prod = Blog.objects.get(id=id)
            prod.auther_name=username
            prod.date=date
            prod.title=title
            prod.description=description
            prod.save()
           
            return JsonResponse({"message": "success", "status": "success"})
###############
@login_required
def status(request):
        if request.method == "POST":
            id = request.POST.get("blog_id")
            status = request.POST.get("status")
            is_checked = bool(status) 
            print("is_checked",is_checked)
            if id:
                prod = Blog.objects.get(id=id)
                if is_checked==True:
                    prod.status= True
                    prod.save()
                    return redirect('Blog')
                else:
                    prod.status= False
                    prod.save()
                    return redirect('Blog')
        return render(request,"adminn/blog.html")
@login_required       
def description_blog(request):
    id = request.GET.get("id")
    required_fields=[]
    if id:
         data = Blog.objects.get(id=id)
         template = loader.get_template('adminn/description.html')
         context={}
         context['data']=data
         print("context",context)
         rendered_template = template.render(context, request)
         return JsonResponse({"rendered_template":rendered_template})

@login_required
def logout_admin(request):
   logout(request)
   return redirect('admin-login') 
@login_required
def delete_img(request):
   
    id = request.GET.get("id")
    
    required_fields=[]
    if id:
         prod = Blog.objects.get(id=id)
         img=prod.image
         img.delete()
         return JsonResponse({"message": "success", "status": "success"})
@login_required    
def check_box(request):
    id= request.GET.get("productId")
    checked = request.GET.get("checked")
    if id:
        prod = Blog.objects.get(id=id)
        if checked=='true':
            tr=True
            prod.status=tr
            prod.save()
            print(tr)
        elif checked=='false':
            fa=False
            prod.status=fa
            prod.save()
        
    return JsonResponse({"message": "success", "status": "success"})
