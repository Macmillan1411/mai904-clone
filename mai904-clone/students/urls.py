from django.urls import path
from .views import HomeView,LitDetailView,TaskView

urlpatterns = [
    path('',HomeView.as_view(),name = 'home'),
    path('literature/',LitDetailView.as_view(),name='literature'),
    path('tasks/',TaskView.as_view(),name='tasks')
]
