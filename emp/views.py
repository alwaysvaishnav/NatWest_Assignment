from rest_framework import generics, status
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from django.http import HttpResponse

class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
   

class EmployeeDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


from django.shortcuts import render

def index(request):
    employees = Employee.objects.all()
    # Pass the employees queryset to the template context
    context = {'employees': employees}
    # Render the 'main.html' template with the context
    return render(request, 'main.html', context)
    


    
