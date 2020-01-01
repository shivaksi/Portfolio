from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogHome , name = 'Blog'),
    path('<int:blog_id>/' , views.details , name = 'details')
] 
