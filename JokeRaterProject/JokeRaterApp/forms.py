from django import forms
from django.contrib.auth.models import User
from JokeRaterApp.models import Category, UserProfile, Joke

class JokeForm(forms.ModelForm):
	class Meta:
                model = Joke
                fields = ('content', 'punchline')
		
	#content = forms.CharField(max_length=400, help_text="Please enter your joke:")
	#punchline = forms.CharField(max_length=100, help_text="Please enter the punchline:")
	
	# category = models.ForeignKey(Category)
	# content = models.CharField(max_length=400)
	# punchline = models.CharField(max_length=100)
	# rating = models.IntegerField(default=0)
	# postingUser = models.ForeignKey(Category)

# class CategoryForm(forms.ModelForm):
    # name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    # views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    # likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    # slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # class Meta:
        # model = Category
        # fields = ('name',)


# class PageForm(forms.ModelForm):
    # title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    # url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    # views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # def clean(self):
        # cleaned_data = self.cleaned_data
        # url = cleaned_data.get('url')

        # if url and not url.startswith('http://'):
            # url = 'http://' + url
            # cleaned_data['url'] = url

        # return cleaned_data
    
    # class Meta:
        # model = Page
        # exclude = ('category',)
		
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('location', 'picture')
