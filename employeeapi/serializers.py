from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "pk",
            "fullname",
            "employee_code",
            "mobile",            
        ]
        # instead of mentioning all fields, you can also use
        # fields = '__all__'
        extra_kwargs = {
            "mobile": {"required": False},
        }
