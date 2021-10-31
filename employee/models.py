from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from PIL import Image


class Employee(MPTTModel):
	name = models.CharField(max_length=50)

	LVL_1 = 1
	LVL_2 = 2
	LVL_3 = 3
	LVL_4 = 4
	LVL_5 = 5
	POSITIONS = [
		(LVL_1, 'level 1'),
		(LVL_2, 'level 2'),
		(LVL_3, 'level 3'),
		(LVL_4, 'level 4'),
		(LVL_5, 'level 5'),
		]
	position        = models.PositiveSmallIntegerField(choices=POSITIONS, blank=False, default=1)
	
	employment_date = models.DateField(auto_now_add=False)
	salary          = models.IntegerField()
	parent          = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
	date_added      = models.DateField(auto_now_add=True)
	photo           = models.ImageField(upload_to='media', blank=True)


	def __str__(self):
		return self.name

	def save(self):
		super().save()

		img = Image.open(self.photo.path)

		img.thumbnail((120, 120))
		img.save(self.photo.path)


	class MPTTMeta:
		order_insersion_by = ['name']
