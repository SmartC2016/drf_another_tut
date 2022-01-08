from rest_framework import viewsets
from . import models
from . import serializers


class EmployeeViewset(viewsets.ModelViewSet):
    # this viewset will create "views" for
    # list, retrieve individual, create, update, destroy
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
