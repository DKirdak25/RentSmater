from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
				user = models.OneToOneField(User, on_delete=models.CASCADE )
				bio = models.TextField()
				birth_date = models.DateField(null=True, blank=True)
				photo = models.FileField(upload_to='images/')
				
				def __str__(self):
								   return str(self.user)
				
				def get_absolute_url(self):
								return reverse('profile_edit', args=[str(self.id)])

