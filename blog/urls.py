from django import urls
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('post/<slug:slug>', views.Post.as_view(), name='post'),
    path('about', views.About.as_view(), name='about'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)