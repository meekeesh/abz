from django.urls import path, include
from .views import show_employee, employee_info, EmployeeViewSet, ChiefSearchAPI


urlpatterns = [
	path('employee_structure/', show_employee, name='show_employee'),
	path('employee_info/', employee_info, name='employee_info'),
	path('accounts/', include('django.contrib.auth.urls')),

	path('employee-set/', EmployeeViewSet.as_view({'get': 'list'})),
	path('employee-set/<int:pk>', EmployeeViewSet.as_view({'get': 'retrieve', 'put': 'partial_update'}), name = 'detail'),
	
	path('chief-set/', ChiefSearchAPI.as_view()),
]
