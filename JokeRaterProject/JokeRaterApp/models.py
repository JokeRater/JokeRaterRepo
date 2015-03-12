from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Category(models.Model):
        name = models.CharField(max_length=128, unique=True)
		
        slug = models.SlugField(unique=True)

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Category, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.name
        

# class Joke(models.Model):
    # category = models.ForeignKey(Category)
    # title = models.CharField(max_length=128)
    # views = models.IntegerField(default=0)

    # def __unicode__(self):
        # return self.title

# class UserProfile(models.Model):
	# user = models.OneToOneField(User)

	# location = models.CharField(max_length=50, unique=True)
	# picture = models.ImageField(upload_to='profile_images', blank=True)

	# def __unicode__(self):
		# return self.user.username

 
