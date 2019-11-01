from django.urls import path
from . import views


urlpatterns = [
    path('create',views.create,name='create'),
    path('<int:blog_id>',views.blog_details,name='blogpage'),
    path('<int:blog_id>/like',views.like,name='like'),
    path('<int:blog_id>/comments',views.addComment,name='comments'),
    

    
]
