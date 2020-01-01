from django.db import models

# Create your models here.

class Blog (models.Model):
	title = models.CharField(max_length = 200)
	pub_date = models.DateTimeField()
	body = models.CharField(max_length = 1000)
	image = models.ImageField(upload_to = 'images/')

	def summary (self):
		return self.body[:100] # ye basically agar body bahut badi hui,toh bas 100 characters tak display karwaega


	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')

	def __str__(self):
		 return self.title