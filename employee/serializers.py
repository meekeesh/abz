from rest_framework import serializers
from .models import Employee


class EmployeeListSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Employee
		fields = ('name', 'position', 'employment_date', 'salary', 'photo', 'id')

class EmployeeDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Employee
		fields = ('name', 'position', 'employment_date',  'salary', 'parent', 'photo', 'date_added')

class EmployeeUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Employee
		fields = ('name', 'position', 'employment_date',  'salary', 'parent')

class ChiefSearchSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Employee
		fields = ('name', 'position', 'id')

class ChiefNameSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Employee
		fields = ('name',)