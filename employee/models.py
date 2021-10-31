from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from PIL import Image


class Employee(MPTTModel):
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

	name            = models.CharField(max_length=50)
	position        = models.PositiveSmallIntegerField(choices=POSITIONS, blank=False, default=1)
	employment_date = models.DateField(auto_now_add=False)
	salary          = models.IntegerField()
	parent          = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
	date_added      = models.DateField(auto_now_add=True)
	photo           = models.ImageField(upload_to='media', null=False, blank=True, default='media/default.png')


	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		super(Employee, self).save(*args, **kwargs)

		img = Image.open(self.photo.path)
		img.thumbnail((120, 120))
		img.save(self.photo.path)


	class MPTTMeta:
		order_insersion_by = ['name']
