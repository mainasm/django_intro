from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /phones/1/
    path('<int:phone_id>/', views.detail, name='detail')
]
