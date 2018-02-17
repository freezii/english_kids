from django.urls import path
from api.views import DashboardView

urlpatterns = [
    path('/', DashboardView()),
]
