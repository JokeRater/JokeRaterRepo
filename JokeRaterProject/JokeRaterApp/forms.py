from django import forms
from django.contrib.auth.models import User
from JokeRaterApp.models import Category, UserProfile, Joke


class JokeForm(forms.ModelForm):		
	content = forms.CharField(max_length=400, help_text="Please enter your joke:")
	punchline = forms.CharField(max_length=100, help_text="Please enter the punchline:")	
	category = forms.ModelChoiceField(queryset=Category.objects.all(), help_text="Please select a category:")
	rating = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	class Meta:
                model = Joke
                fields = ('content', 'punchline','category',)
                
        def clean(self):
                category = self.cleaned_data.get('Category')
                return self.cleaned_data
		
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('location', 'picture')
