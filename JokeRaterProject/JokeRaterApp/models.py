from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import datetime
    
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
    
class Joke(models.Model):
    category = models.ForeignKey(Category)
    content = models.CharField(max_length=400)
    punchline = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    postingUser = models.ForeignKey(User,null=True)
    datePosted = models.DateField(default=datetime.datetime.now().date())
    reportFlag = models.BooleanField(default=False)
	
    def __unicode__(self):
        return self.content

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    location = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username


 
