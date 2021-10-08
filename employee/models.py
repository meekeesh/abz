from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Employee(MPTTModel):
	name            = models.CharField(max_length=50)
	position        = models.CharField(max_length=200)
	#employment_date = models.DateTimeField(auto_now_add=False)
	employment_date = models.DateField(auto_now_add=False)
	salary          = models.IntegerField()
	parent          = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	#date_added      = models.DateTimeField(auto_now_add=True)
	date_added      = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name

	class MPTTMeta:
		order_insersion_by = ['name']
