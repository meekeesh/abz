from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import show_employee, employee_info, edit_info, add_employee, EmployeeViewSet, ChiefSearchAPI, ChiefNameAPI


urlpatterns = [
	path('employee_structure/', show_employee, name='show_employee'),
	path('employee_info/', employee_info, name='employee_info'),
	path('edit_employee_info/<int:pk>', edit_info, name='edit_info'),
	path('add_new_employee/', add_employee, name='add_employee'),

	path('accounts/', include('django.contrib.auth.urls')),

	path('employee-set/', EmployeeViewSet.as_view({'get': 'list'})),
	path('employee-set/<int:pk>', EmployeeViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name = 'detail'),
	path('employee-set/new-employee', EmployeeViewSet.as_view({'post': 'create'}), name='create'),
	path('chief-name/<int:pk>', ChiefNameAPI.as_view()),
	
	path('chief-set/', ChiefSearchAPI.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
