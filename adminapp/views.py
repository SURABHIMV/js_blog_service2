from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
import re
from django.views.generic import TemplateView
import sweetify
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth import logout
from django.template import loader
from . models import *
from datetime import datetime
from django.views import View
from django.utils.decorators import method_decorator   #for class based view authentication login
from django.contrib.auth.decorators import login_required 

# Create your views here.

####################################################


class admin_login(View):

    def get(self, request):
        return render(request, "adminn/admin_login.html")
    def post(self, request):
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
    
@method_decorator(login_required, name='dispatch')      #authentication for class based view
class dashboard(TemplateView):
    template_name = "adminn/dashboard.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type_data'] = "dashboard"
        context['blog_count'] = Blog.objects.all().count()
        context['service_count']= Service.objects.all().count()
        return context

@method_decorator(login_required, name='dispatch')
class blog(TemplateView):
    template_name = "adminn/blog.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type_data'] = "Blog"
        context['data'] = Blog.objects.all()
        return context
    
@method_decorator(login_required, name='dispatch')
class logout_admin(View):
    def get(self, request):
        logout(request)
        return redirect('admin-login')


# from django.views.generic import TemplateView
# @method_decorator(login_required, name='dispatch')
# class dashboard(TemplateView):
#     template_name = "adminn/dashboard.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['type_data'] = "dashboard"
#         context['blog_count'] = Blog.objects.all().count()
#         return context

# @method_decorator(login_required, name='dispatch')
# class blog(TemplateView):
#     template_name = "adminn/blog.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['type_data'] = "Blog"
#         context['data'] = Blog.objects.all()
#         return context

    
@method_decorator(login_required, name='dispatch')
class create_blog(View):
    def get(self, request):
        return render(request, "adminn/blog.html")
        
    def post(self, request):
        id= request.POST.get("blog_id")
        name = request.POST.get("auther_name")
        date = request.POST.get("date")
        image = request.FILES.get("image")
        title = request.POST.get("title")
        description = request.POST.get("description")
         
        # Convert the string to a datetime object
        date_obj = datetime.strptime(date, "%Y-%m-%d")

        # Convert the datetime object to the desired format
        formatted_date = date_obj.strftime("%d/%m/%Y")
       
        # lastconnection = datetime.strptime(date, "%d/%m/%Y")

        print('lastconnection',formatted_date)
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
        if required_fields:
            response = f"{', '.join(required_fields)} are required"
            return JsonResponse({"message": response, "status": "error"})
        else:
            blog = Blog.objects.create(
                auther_name=name,
                date=date,
                image=image,
                title=title,
                description=description
            )
            # da=Blog.objects.get(id=id)
            
            response_data = {
                "id": blog.id,
                "auther_name": blog.auther_name,
                "date": formatted_date,
                "title": blog.title,
                "description": blog.description,
                "image_url": blog.image.url if blog.image else None
            }
            context = {
                'message': "success",
                "status": "success",
                'data':response_data
            }

            return JsonResponse(context)

    

    
@method_decorator(login_required, name='dispatch')
class delete_blog(View):
    def get(self, request):
        id = request.GET.get("id")
        required_fields=[]
        
        if id:
            prod = Blog.objects.get(id=id)
            prod.soft_delete()
            return JsonResponse({"message": "success", "status": "success"})
            

@method_decorator(login_required, name='dispatch')    
class edit_blog_action(View):
    def post(self, request):
  
        id = request.POST.get("product_id")
        username = request.POST.get("product_name")
        image_change = request.POST.get("image_change")
        title = request.POST.get("title")
        description = request.POST.get("description")
        date = request.POST.get("date")
        product_image=request.FILES.get('product_image')
        print(id,username,image_change,title,description,date, product_image)
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
            
            response_data = {
                "id": prod.id,
                "auther_name": prod.auther_name,
                "date": prod.date,
                "title": prod.title,
                "description": prod.description,
                "image_url": prod.image.url if prod.image else None
            }
            # response_data = {
            #     "id": prod.id
            # }
            print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk',prod.id)
            context = {
                'message': "success",
                "status": "success",
                'data':response_data
            }

            return JsonResponse(context)

    
@method_decorator(login_required, name='dispatch')
class status(View):
        def post(self, request):
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

    
@method_decorator(login_required, name='dispatch')    
class description_blog(View):
    def get(self, request):
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
        

@method_decorator(login_required, name='dispatch')
class delete_img(View):
    def get(self, request):
        id = request.GET.get("id")
        required_fields=[]
        if id:
            prod = Blog.objects.get(id=id)
            prod.image = None    #to delete single field  None is used , it will delete the data from database
            prod.save()
            return JsonResponse({"message": "success", "status": "success"})

    
@method_decorator(login_required, name='dispatch')   
class check_box(View):
    def get(self, request):
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
    
class forget_password(View):
    def post(self, request):
        username = request.POST.get("username")
        password= request.POST.get("password")
        user=User.objects.get(is_superuser=True)
        name=user.username
        if name==username:
             user.set_password(password)
             user.save()
             return redirect('admin-login')    
        return render(request,"adminn/forget_password.html")
    

class edit_blog(View):
    def get(self, request):
        id = request.GET.get("id")
        data = Blog.objects.get(id=id)
        template = loader.get_template('adminn/edit_blog.html')
        context={}
        context['data']=data
        print("context",context)
        rendered_template = template.render(context, request)
        return JsonResponse({"rendered_template":rendered_template})

#service modal

@method_decorator(login_required, name='dispatch')
class service(TemplateView):
    template_name = "adminn/service.html"
    
    def get_context_data(self,**kwargs,):
        context = super().get_context_data(**kwargs)
        context['type_data'] = "Service"
        context['data'] = Service.objects.all()
        return context


@method_decorator(login_required, name='dispatch')    
class edit_service_action(View):
    def post(self, request):
  
        id = request.POST.get("product_id")
        title = request.POST.get("product_name")
        image_ch = request.POST.get("image_ch")
        description = request.POST.get("description")
        product_image=request.FILES.get('product_image')
        print("kkkkkkkkkkkkkkkkkkkk",id,image_ch,title,description,product_image)
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
        if image_ch != "no":
            data_save = Service.objects.get(id=id)
            data_save.image = product_image
            data_save.save()
        # if not username:
        #     required_fields.append("Username")
        # if not image:
        #     required_fields.append("image")
        # if required_fields:
        #     response = f"{', '.join(required_fields)} are required"
        #     return JsonResponse({"message": response, "status": "error"})
        
        

        if id:
            prod = Service.objects.get(id=id)
            prod.title=title
            prod.description=description
            prod.save()
           
            return JsonResponse({"message": "success", "status": "success"})


class edit_service(View):
    def get(self, request):
        id = request.GET.get("id")
        data = Service.objects.get(id=id)
        template = loader.get_template('adminn/edit_service.html')
        context={}
        context['data']=data
        print("context",context)
        rendered_template = template.render(context, request)
        return JsonResponse({"rendered_template":rendered_template})
    

@method_decorator(login_required, name='dispatch')
class create_service(View):
    def get(self, request):
        return render(request, "adminn/service.html")
        
    def post(self, request):
        context={}
        id= request.POST.get("service_id")
        print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
        image = request.FILES.get("simage")
        title = request.POST.get("stitle")
        description = request.POST.get("sdescription")
         
        
        print('hhhhhhhhhhhhhhhhhhh',image)
    
        required_fields = []
  
        if not image:
            required_fields.append("image")
        if not title:
            required_fields.append("title")
        if not description:
            required_fields.append("description")
        if required_fields:
            response = f"{', '.join(required_fields)} are required"
            return JsonResponse({"message": response, "status": "error"})
        else:
            
            service = Service.objects.create(
                image=image,
                title=title,
                description=description
            )
            # da=Blog.objects.get(id=id)
            
            service=Service.objects.all()
            # context = {
            #     'message': "success",
            #     "status": "success",
            #     'data':response_data
            # }
            
            context['data'] = service
            template = loader.get_template('adminn/service_table.html')
            html_content = template.render(context, request)
            return JsonResponse({"status": "success", "message":"success", "template": html_content})


    
@method_decorator(login_required, name='dispatch')    
class description_service(View):
    def get(self, request):
        id = request.GET.get("id")
        required_fields=[]
        if id:
            data = Service.objects.get(id=id)
            template = loader.get_template('adminn/service_description.html')
            context={}
            context['data']=data
            print("context",context)
            rendered_template = template.render(context, request)
            return JsonResponse({"rendered_template":rendered_template})
        

@method_decorator(login_required, name='dispatch')
class delete_service(View):
    def get(self, request):
        context={}
        id = request.GET.get("id")
        required_fields=[]
        
        if id:
            prod = Service.objects.get(id=id)
            prod.soft_delete()
            sr=Service.objects.all()
    
            # context = {
            #     'message': "success",
            #     "status": "success",
            #     'data':response_data
            # }
            
            context['datas'] = sr
            template = loader.get_template('adminn/service_table.html')
            html_content = template.render(context, request)
            return JsonResponse({"status": "success", "message":"success", "template": html_content})
           

@method_decorator(login_required, name='dispatch')   
class check_service_box(View):
    def get(self, request):
        id= request.GET.get("serviceId")
        checked = request.GET.get("checked")
        if id:
            sr = Service.objects.get(id=id)
            if checked=='true':
                tr=True
                sr.status=tr
                sr.save()
                print(tr)
            elif checked=='false':
                fa=False
                sr.status=fa
                sr.save()
            
        return JsonResponse({"message": "success", "status": "success"})


@method_decorator(login_required, name='dispatch')
class delete_img_service(View):
    def get(self, request):
        id = request.GET.get("id")
        required_fields=[]
        if id:
            sr = Service.objects.get(id=id)
            sr.image = None    #to delete single field  None is used , it will delete the data from database
            sr.save()
            return JsonResponse({"message": "success", "status": "success"})
####################################################
#function based view

# def admin_login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         print(username,password)
#         user = authenticate(username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('dashboard')
#         else:
#           sweetify.error(request, 'Enter valid username and password')     
#     return render(request,"adminn/admin_login.html")

# @login_required
# def dashboard(request):
#     type_data = "dashboard"
#     prod= Blog.objects.all().count()
#     print('prod',prod)
#     context = {
#         'type_data':type_data,
#         'blog_count':prod
#     }
#     return render(request,"adminn/dashboard.html",context)
# @login_required
# def blog(request):
#     type_data = "Blog"
#     prod= Blog.objects.all() 
#     c=0
#     context = {
#         'type_data': type_data,
#         'data':prod
#     } 
#     return render(request,"adminn/blog.html",context)

# ##########################
# @login_required
# def create_blog(request):
#     if request.method == "POST":
#         print('*****************************************************')
#         name = request.POST.get("auther_name")
#         date= request.POST.get("date")
#         image = request.FILES.get("image")
#         title= request.POST.get("title")
#         description= request.POST.get("description")
#         status = request.POST.get('status') == 'on'

     
#         required_fields = []

#         if not name:
#             required_fields.append("name")
#         if not date:
#             required_fields.append("date")
#         if not image:
#             required_fields.append("image")
#         if not title:
#             required_fields.append("title")
#         if not description:
#             required_fields.append("description")
#         if not description:
#             required_fields.append("status")
#         if required_fields:
    
#             response = f"{', '.join(required_fields)} are required"
#             return JsonResponse({"message": response, "status": "error"})
#         else:
#             blog= Blog.objects.create(auther_name=name,date=date,image=image,title=title,description=description,status=status)
 
#             return JsonResponse({"message": "success", "status": "success"})
#     return render(request,"adminn/blog.html")  

# @login_required
# def edit_blog(request):

#     id = request.GET.get("id")
#     data = Blog.objects.get(id=id)
#     template = loader.get_template('adminn/edit_blog.html')
#     context={}
#     context['data']=data
#     print("context",context)
#     rendered_template = template.render(context, request)
#     return JsonResponse({"rendered_template":rendered_template})

# @login_required
# def delete_blog(request):
   
#     id = request.GET.get("id")
#     required_fields=[]
#     if id:
#          prod = Blog.objects.get(id=id)
#          prod.soft_delete()
#          return JsonResponse({"message": "success", "status": "success"})
# @login_required    
# def edit_blog_action(request):
#   if request.method == "POST":
#         id = request.POST.get("product_id")
#         username = request.POST.get("product_name")
#         image_change = request.POST.get("image_change")
#         title = request.POST.get("title")
#         description = request.POST.get("description")
#         date = request.POST.get("date")
#         product_image=request.FILES.get('product_image')
#         # date = datetime.strptime(date, '%d/%m/%Y')
#         # convert datetime format into %Y-%m-%d-%H:%M:%S
#         # format using strftime
#         # date=d.strftime("%Y-%m-%d")
   
#         ##################################
#         #logic to access the image from backend 
#         # if request.FILES :
#         #     product_image=request.FILES.get('product_image',None)
        
   
#         # required_fields = []
#         # if 'product_image' in request.FILES:
#         #     data_save = Blog.objects.get(id=id)
#         #     data_save.image = product_image
#         #     data_save.save()

#         ##########################################
#         required_fields = []
#         if image_change != "no":
#             data_save = Blog.objects.get(id=id)
#             data_save.image = product_image
#             data_save.save()
#         # if not username:
#         #     required_fields.append("Username")
#         # if not image:
#         #     required_fields.append("image")
#         # if required_fields:
#         #     response = f"{', '.join(required_fields)} are required"
#         #     return JsonResponse({"message": response, "status": "error"})
        
        

#         if username:
#             prod = Blog.objects.get(id=id)
#             prod.auther_name=username
#             prod.date=date
#             prod.title=title
#             prod.description=description
#             prod.save()
           
#             return JsonResponse({"message": "success", "status": "success"})
# ###############
# @login_required
# def status(request):
#         if request.method == "POST":
#             id = request.POST.get("blog_id")
#             status = request.POST.get("status")
#             is_checked = bool(status) 
#             print("is_checked",is_checked)
#             if id:
#                 prod = Blog.objects.get(id=id)
#                 if is_checked==True:
#                     prod.status= True
#                     prod.save()
#                     return redirect('Blog')
#                 else:
#                     prod.status= False
#                     prod.save()
#                     return redirect('Blog')
#         return render(request,"adminn/blog.html")
# @login_required       
# def description_blog(request):
#     id = request.GET.get("id")
#     required_fields=[]
#     if id:
#          data = Blog.objects.get(id=id)
#          template = loader.get_template('adminn/description.html')
#          context={}
#          context['data']=data
#          print("context",context)
#          rendered_template = template.render(context, request)
#          return JsonResponse({"rendered_template":rendered_template})

# @login_required
# def logout_admin(request):
#    logout(request)
#    return redirect('admin-login') 
# @login_required
# def delete_img(request):
   
#     id = request.GET.get("id")
    
#     required_fields=[]
#     if id:
#          prod = Blog.objects.get(id=id)
#          img=prod.image
#          img.soft_delete()
#          return JsonResponse({"message": "success", "status": "success"})
# @login_required    
# def check_box(request):
#     id= request.GET.get("productId")
#     checked = request.GET.get("checked")
#     if id:
#         prod = Blog.objects.get(id=id)
#         if checked=='true':
#             tr=True
#             prod.status=tr
#             prod.save()
#             print(tr)
#         elif checked=='false':
#             fa=False
#             prod.status=fa
#             prod.save()
        
#     return JsonResponse({"message": "success", "status": "success"})


# def forget_password(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password= request.POST.get("password")
#         user=User.objects.get(is_superuser=True)
#         name=user.username
#         if name==username:
#              user.set_password(password)
#              user.save()
#              return redirect('admin-login')    
#     return render(request,"adminn/forget_password.html")

