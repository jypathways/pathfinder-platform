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

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Spark(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(db_index=False, blank=True, unique=True)
    url = models.URLField()
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=True,null=True)
    description = models.TextField(blank = True)
    category = models.ForeignKey(Category, default=1)
    author = models.ForeignKey(User, null=False)

    def __str__(self):
        return self.name
