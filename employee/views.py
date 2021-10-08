from django.shortcuts import render
from .models import Employee
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from .serializers import (EmployeeListSerializer,
			  EmployeeDetailSerializer,
			  EmployeeUpdateSerializer,
			  ChiefSearchSerializer)
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework.renderers import TemplateHTMLRenderer


def show_employee(request):
	return render(request, 'employee.html', {'employee': Employee.objects.all()})

def employee_info(request):
	return render(request, 'employee_info.html')


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
		render_classes = [TemplateHTMLRenderer]
		queryset       = Employee.objects.all()
		employee       = get_object_or_404(queryset, pk=pk)
		serializer     = EmployeeDetailSerializer(employee)
		try:
			chief = queryset.get(pk=serializer.data['parent'])
		except:
			chief = 'None'

		return render(request, 'ttt.html', {'employee': serializer.data, 'chief': chief})


	def partial_update(self, request, pk=None):
		queryset = Employee.objects.all()
		employee = get_object_or_404(queryset, pk=pk)
		serializer = EmployeeUpdateSerializer(employee, data=request.data, partial=True)

		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data)


class ChiefSearchAPI(APIView):
	def get(self, request):
		search_name = request.query_params['name']

		queryset = Employee.objects.filter(name__icontains = search_name)
		serializer = ChiefSearchSerializer(queryset, many=True)

		return Response(serializer.data)
