from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('data', views.DataListCreateAPIView.as_view(), name='data'),
]
