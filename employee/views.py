from django.shortcuts import render
from .models import Employee
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from django.views.generic.detail import DetailView
from .serializers import (
						EmployeeListSerializer,
						EmployeeDetailSerializer,
						EmployeeUpdateSerializer,
						ChiefSearchSerializer,
						ChiefNameSerializer
						)
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


def show_employee(request):
	return render(request, 'employee.html', {'employee': Employee.objects.all()})

def employee_info(request):
	return render(request, 'employee_info.html')

def edit_info(request, pk=None):
	return render(request, 'edit_info.html')

def add_employee(request):
	return render(request, 'create_employee.html')


class EmployeeViewSet(ViewSet):
	def list(self, request):
		def get_queryset(self):
			search_params = self.request.query_params

			search_name     = search_params['name']
			search_position = search_params['position']
			search_date     = search_params['date']
			search_salary   = search_params['salary']
			order           = search_params['order']

			queryset = Employee.objects.filter(
				name__icontains            = search_name,
				position__startswith       = search_position,
				employment_date__icontains = search_date,
				salary__startswith         = search_salary,
				)
			if order != '':
				queryset = queryset.order_by(order)
			return queryset

		queryset = get_queryset(self)
		serializer = EmployeeListSerializer(queryset, many=True)
		
		return Response(serializer.data)
    
	def retrieve(self, request, pk=None):
		queryset   = Employee.objects.all()
		employee   = get_object_or_404(queryset, pk=pk)
		serializer = EmployeeDetailSerializer(employee)
		return Response(serializer.data)

	def partial_update(self, request, pk=None, *args, **kwargs):
		employee = Employee.objects.get(pk=pk)
		serializer = EmployeeUpdateSerializer(employee, request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def destroy(self, request, pk=None, *args, **kwargs):
		employee = Employee.objects.get(pk=pk)
		employee.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def create(self, request):
		serializer = EmployeeUpdateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
	def create(self, request):
		data = self.request.data
		employee = Employee(
			name=data['name'],
			position=data['position'],
			salary=data['salary'],
			parent=Employee.objects.get(pk=data['chief']) if data['chief'] else None,
			employment_date=data['employment_date']
			)
		employee.save()

		return Response(data='create success')
'''

class ChiefSearchAPI(APIView):
	def get(self, request):
		search_name = request.query_params['name']

		queryset = Employee.objects.filter(name__icontains = search_name)[:10]
		serializer = ChiefSearchSerializer(queryset, many=True)

		return Response(serializer.data)

class ChiefNameAPI(APIView):
	def get(request, *args, **kwargs):
		employee = Employee.objects.get(pk=kwargs['pk'])
		serializer = ChiefNameSerializer(employee)
		return Response(serializer.data)
		