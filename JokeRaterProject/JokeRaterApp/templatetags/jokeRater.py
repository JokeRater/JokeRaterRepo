from django import template
from JokeRaterApp.models import Category, Joke

register = template.Library()

@register.inclusion_tag('JokeRater/cats.html')
def get_category_list():
    return {'cats': Category.objects.all()}

@register.inclusion_tag('JokeRater/overall.html')
def get_top_overall():
	return {'overall': Joke.objects.order_by('-rating')[:5]}