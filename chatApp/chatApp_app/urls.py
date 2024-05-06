from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.chatroom, name='chatroom'),
    path('check_view', views.check_view, name='check_view'),
    path('send', views.send, name='send'),
    path('getMessage/<str:room>', views.getMessage, name='getMessage',)
]
