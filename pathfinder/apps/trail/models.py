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
	
class Project(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    # slug = models.SlugField(db_index=False, blank=True, unique=True)
    url = models.URLField()
    likes = models.IntegerField(default=0)
    date_created = models.DateTimeField(('date_joined'), default=timezone.now)
    
    @models.permalink
    def get_absolute_url(self):
        return 'trail:project', (self.slug,)
	
    def __str__(self):
        return self.title