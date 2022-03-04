from django.urls import path
from orderapp import views

urlpatterns = [
    path('upload/', views.AdminUpload.as_view(),name="Adminupload"),
]