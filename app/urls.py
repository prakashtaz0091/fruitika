from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),


    #auth
    # path('login/', LoginView.as_view(), name="login"),
    path('login/', login_view, name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    # path('sign_up/', signup, name="sign_up"),
    path('sign_up/', signup_view, name="sign_up"),



    #blog
    path('blog/', blog, name="blog"),
    path('blog/<int:blog_id>/', blog_detail, name="blog_detail"),


    #comment
    # path('comment/<int:blog_id>/', comment, name="comment"),
    path('comment/', comment, name="comment"),


    #replies
    path('replies/<int:comment_id>/', replies, name="replies"),
    path('reply/<int:comment_id>/', reply, name="reply"),


    #tag
    path('tag/blogs/<int:tag_id>/', tag_blogs, name="tag_blogs"),
    


    



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)