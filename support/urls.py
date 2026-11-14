from django.urls import include, path
from .import views

urlpatterns = [
    path('chat/<int:order_id>/',views.chat,name='chat'),
]