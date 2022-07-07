from django.db import models

# Create your models here.
class todo(models.Model):
	todo = models.CharField(max_length=200, null=True)
	is_completed = models.BooleanField(default=False, null=True)

	def __str__(self):
	   return self.todo