from django.db import models
from django.contrib.auth.models import UserManager, User
from django.utils import timezone
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	date_joined = models.DateTimeField(('date_joined'), default=timezone.now)
	
	objects = UserManager()
	
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			UserProfile.objects.create(user=instance)

	def __str__(self):
		return self.user.username	
	post_save.connect(create_user_profile, sender=User)