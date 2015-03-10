from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Categories(models.Model):
        content = models.CharField(max_length=500, unique=True)
        views = models.IntegerField(default=0)
        #
        name = models.CharField(max_length=128, unique=True)

        slug = models.SlugField(unique=True)

        def save(self, *args, **kwargs):
                self.slug = slugify(self.name)
                super(Categories, self).save(*args, **kwargs)

        def __unicode__(self):
                return self.name
        

class Jokes(models.Model):
    category = models.ForeignKey(Categories)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
	user = models.OneToOneField(User)

    # The additional attributes we wish to include.
	location = models.CharField(max_length=50, unique=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.user.username

    #Test line to try and force a commit
