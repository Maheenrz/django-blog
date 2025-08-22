from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
    path('api/get/', views.get_data),
    path('api/post/', views.post_data),
    path('api/put/', views.put_data),
    path('api/delete/', views.delete_data),
]

