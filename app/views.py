from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.
# from . import signals
from .models import *
# from .tasks import demo_task
import time
from django.db.models import Count, Prefetch
from django.db.models.functions import TruncMonth
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from .utils import get_nested_comments


# @new_decorator
def home(request):
    # print("this is home view", request.new_data)
    blogs = Blog.objects.select_related('author').all()

    # demo_task()
    # #task which takes 5 minutes
    # time.sleep(3)

    context = {
        'blogs': blogs
    }
    return render(request, "app/index.html", context)



# def contact(request):

#     if request.method == "POST":
#         # print(request.POST)
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")

#         if not len(phone) == 10:
#             messages.error(request, "Please enter a valid phone number")
#             return redirect("contact")

#         print(name, email, phone, message)


#         return redirect("home")

#     return render(request, "app/contact.html")
# def contact(request):


#     if request.method == "POST":
#         contact_form = ContactForm(request.POST)
#         if contact_form.is_valid():
#             # contact_form.save()
#             print(contact_form.cleaned_data)
#             messages.success(request, "Your message has been sent")
#             return redirect("home")
#         else:
#             context = {
#                 'form': contact_form
#             }
#             # print("error")
#             return render(request, "app/contact.html", context)


#     contact_form = ContactForm()

#     context = {
#         'form': contact_form
#     }

#     return render(request, "app/contact.html", context)
def contact(request):


    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            # print(contact_form.cleaned_data)
            messages.success(request, "Your message has been sent")
            return redirect("home")
        else:
            context = {
                'form': contact_form
            }
            # print("error")
            return render(request, "app/contact.html", context)


    contact_form = ContactForm()

    context = {
        'form': contact_form
    }

    return render(request, "app/contact.html", context)






# def signup(request):


#     if request.method == "POST":
#         signup_form = CustomUserCreationForm(request.POST)

#         if signup_form.is_valid():
#             signup_form.save()

#             messages.success(request, "Your account has been created, now you can login")
#             return redirect("login")
#         else:
#             context = {
#                 'singup_form': signup_form
#             }
#             return render(request, "registration/signup.html", context)




#     context = {
#         'singup_form': CustomUserCreationForm()
#     }


#     return render(request, "registration/signup.html", context)
def signup(request):


    if request.method == "POST":
        signup_form = CustomUserCreationForm(request.POST, request.FILES)

        if signup_form.is_valid():
            signup_form.save()
            #print("email verification")

            messages.success(request, "Your account has been created, now you can login")
            return redirect("login")
        else:
            context = {
                'singup_form': signup_form
            }
            return render(request, "registration/signup.html", context)




    context = {
        'singup_form': CustomUserCreationForm()
    }


    return render(request, "registration/signup.html", context)



#How to purely handle login
"""
1. Get username and password from login Form
2. user = User.objects.get(username=username) OR  User.objects.filter(username=username).exists()
3. user.check_password(password)  #here password is the password entered by user in Login Form
# if user.password==password 
4. login(request, user)   #here, by default django uses Session Based Authentication



Logout
logout(request)



Blog.objects.create()


User.objects.create_user()
user = User()
user.username = "abc"
user.email = "abc@gmail.com"
# user.password = "abc" wrong
user.set_password("abc")
user.save()
"""



def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        # email = request.POST['email']
        password = request.POST.get("password")

        # try:
            # user = CustomUser.objects.get(email=email)
        user = authenticate(request, email=email, password=password)
        # except Exception:        
        #     messages.error(request, "Email or Password is incorrect")
        #     return redirect("login")
        # else:
        #     if not user.check_password(password):
        #         messages.error(request, "Email or Password is incorrect")
        #         return redirect("login")
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect("home")
        else:
            messages.error(request, "Email or Password is incorrect")
            return redirect("login")
        

    return render(request, "registration/login.html")





def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        mobile = request.POST.get("mobile")
        profile_pic = request.FILES.get("profile_pic")

        # print(username, email, password, mobile, profile_pic)

        # user = CustomUser.objects.create_user(username=username, email=email, password=password, mobile=mobile, profile_pic=profile_pic)
        user = CustomUser()
        user.username = username
        user.email = email
        user.set_password(password)
        user.mobile = mobile
        user.profile_pic = profile_pic
        user.save()
        messages.success(request, "Your account has been created, now you can login")



        return redirect("login")

    return render(request, "registration/signup.html")





def blog(request):

    if request.user.is_anonymous:
        messages.warning(request, "Please login first")
        return redirect("login")

    blogs = Blog.objects.filter(author=request.user).prefetch_related('images').all()
    

    if request.method == "POST":
        blog_form = BlogForm(request.POST)
        blog_images = request.FILES.getlist("blog_images")

        if blog_form.is_valid():
            blog = Blog()
            blog.author = request.user
            blog.title = blog_form.cleaned_data['title']
            blog.body = blog_form.cleaned_data['body']
            blog.save()
            blog.tags.set(blog_form.cleaned_data['tags'])
            print(blog.title)
            messages.success(request, "Blog has been created")

            for image in blog_images:
                BlogImage.objects.create(blog=blog, image=image)

            return redirect("blog")
        
        else:
            context = {
                'blog_form': blog_form,
                'blogs':blogs
            }
            return render(request, "app/blog.html", context)


    context = {
        'blog_form': BlogForm(),
        'blogs':blogs

    }


    return render(request, "app/blog.html", context)







def blog_detail(request, blog_id):

    blog = Blog.objects.select_related('author').prefetch_related(
            'images',
            Prefetch('comments', queryset=Comment.objects.filter(parent=None).annotate(replies_count=(Count('replies'))), to_attr='root_comments'),
            'tags'
            ).get(id=blog_id)

    
    recent_blogs = Blog.objects.only('title')[:5]

    # Annotate the blogs by month and year, and count them
    monthly_blogs = (
        Blog.objects
        .annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(blog_count=Count('id'))
        .order_by('month')
    )

    # Format the result
    formatted_results = [
        {
            'month': blog['month'].strftime('%b %Y'),  # Format the date
            'count': blog['blog_count']
        }
        for blog in monthly_blogs
    ]

    # print(formatted_results)


    

    context = {
        'blog': blog,
        'recent_blogs': recent_blogs,
        'monthly_blogs': formatted_results
    }


    return render(request, "app/blog_detail.html", context)






# def comment(request, blog_id):
#     if request.method == "POST":
#         comment_message = request.POST.get("comment")
#         blog = Blog.objects.get(id=blog_id)
#         Comment.objects.create(body=comment_message, blog=blog, author=request.user)
#         return redirect("blog_detail", blog_id=blog_id)



@require_http_methods(["POST"])
def comment(request):
    try:
     
        data = json.loads(request.body)
        # print(data)
        user_id = data.get('user_id')
        blog_id = data.get('blog_id')
        comment_message = data.get('comment_message')
        print(user_id, blog_id, comment_message)

        try:
            comment_author = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)


        comment = Comment.objects.create(body=comment_message, blog_id=blog_id, author=comment_author)

        if comment is not None:
            response_data = {
                'message': 'Data received successfully!',
                'comment_id': comment.id,
                'comment_body':comment.body,
                'comment_author':comment.author.email,
                'comment_created_at': comment.created_at,
                'comment_author_profile_pic':comment.author.profile_pic.url if comment.author.profile_pic else None
            }
            return JsonResponse(response_data, status=200)
        else:
            return JsonResponse({'error': 'Something went wrong'}, status=500)


    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)



@require_http_methods(['GET'])
def replies(request, comment_id):

    # print(comment_id)
    try:
        comment = Comment.objects.get(id=comment_id)
        replies = Comment.objects.filter(parent=comment_id).select_related('author').annotate(replies_count=Count('replies')).order_by('-created_at')
    except Comment.DoesNotExist:
        return JsonResponse({'error': 'Comment not found'}, status=404)

    reply_data = []

    for reply in replies:
        reply_data.append({
            'comment_id': reply.id,
            'replies_count': reply.replies_count,
            'comment_body': reply.body,
            'comment_author': reply.author.email,
            'comment_created_at': reply.created_at,
            'comment_author_profile_pic':reply.author.profile_pic.url if reply.author.profile_pic else None
        })


    response = {
        'message': 'Data received successfully!',
        'replies': reply_data
    }

    return JsonResponse(response, status=200)    


@require_http_methods(["POST"])
def reply(request, comment_id):
    # print(comment_id)
    reply_message = request.POST.get("reply")
    if reply_message is None or len(reply_message) == 0:
        return JsonResponse({'error': 'Reply message is required'}, status=400)

    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        return JsonResponse({'error': 'Comment not found'}, status=404)

    Comment.objects.create(body=reply_message, parent=comment, author=request.user, blog=comment.blog)

    return JsonResponse({'message': 'Data received successfully!'}, status=200)





def tag_blogs(request, tag_id):
    
    tag = Tag.objects.prefetch_related('blogs', 'blogs__author').get(id=tag_id)
    
    # print(tag_blogs.blogs.all()[0].author)

    context = {
        'blogs': tag.blogs.all()
    }


    return render(request, "app/tag_blogs.html", context)


