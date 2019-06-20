from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.home, name="home"),
    #path(r'^login/$', auth_views.login, {'template_name': 'post/login_user.html'}),
    #path('login/',auth_views.login, {'template_name': 'post/login_user.html'},name='login'),
    #path('home/', TemplateView.as_view(template_name='post/home.html'), name='valid'),
    #path('login', login, {'template_name': 'Registration/login.html'})
    path('login', auth_views.LoginView.as_view(template_name="post/login_user.html"), name='login'),
    #path('login', auth_views.LoginView.as_view(template_name="Registration/login.htmlname='login'"),name='login'),
    #url(r'^logout/$', auth_views.LogoutView.as_view(), name="logout"),
    #path('login', auth_views.LoginView.as_view(template_name="post/logout.html"),name='logout'),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    path('register', views.register, name='register'),
    path('view', views.hashtag_list, name='hashtag_list'),
    path('post/my_post',views.my_post,name='my_post'),
    path('art/', views.hashtag_art, name='hashtag_art'),
    path('food/', views.hashtag_food, name='hashtag_food'),
    path('fashion/', views.hashtag_fashion, name='hashtag_fashion'),
    path('mood/', views.hashtag_mood, name='hashtag_mood'),
    path('tech/', views.hashtag_tech, name='hashtag_tech'),
    path('wildlife/', views.hashtag_wildlife, name='hashtag_wildlife'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    #path('post/<int:pk>/edit/', views.PostEdit.as_view(), name='post_edit'),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
