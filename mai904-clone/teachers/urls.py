from django.urls import path
from .views import TeachersView

urlpatterns = [
    path('',TeachersView.as_view(),name = 'teacher_list')
]



