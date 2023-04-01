from django.urls import path, include
from server import views

urlpatterns = [
    path('status/<int:user_id>/', views.Status.as_view())
]
