# employees/urls.py

from django.urls import path
from .views import EmployeeListCreateAPIView, EmployeeDetailUpdateAPIView, index

urlpatterns = [
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetailUpdateAPIView.as_view(), name='employee-detail-update'),
    path('', index, name='index')
]