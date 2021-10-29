from django.urls import path, include
from .views import show_employee, employee_info, edit_info, EmployeeViewSet, ChiefSearchAPI, ChiefNameAPI


urlpatterns = [
	path('employee_structure/', show_employee, name='show_employee'),
	path('employee_info/', employee_info, name='employee_info'),
	path('edit_employee_info/<int:pk>', edit_info, name='edit_info'),

	path('accounts/', include('django.contrib.auth.urls')),

	path('employee-set/', EmployeeViewSet.as_view({'get': 'list'})),
	path('employee-set/<int:pk>', EmployeeViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'}), name = 'detail'),
	path('chief-name/<int:pk>', ChiefNameAPI.as_view()),
	
	path('chief-set/', ChiefSearchAPI.as_view()),
]
