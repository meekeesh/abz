from rest_framework import serializers
from .models import Employee


class EmployeeListSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Employee
		fields = ('name', 'position', 'employment_date', 'salary', 'id')

class EmployeeDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Employee
		fields = ('name', 'position', 'employment_date',  'salary', 'parent', 'date_added')

class EmployeeUpdateSerializer(serializers.Serializer):
	pass

class ChiefSearchSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Employee
		fields = ('name', 'id')