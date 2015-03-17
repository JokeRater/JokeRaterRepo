from django import template
from JokeRaterApp.models import Category, Joke

register = template.Library()

@register.inclusion_tag('JokeRater/cats.html')
def get_category_list():
    return {'cats': Category.objects.all()}

@register.inclusion_tag('JokeRater/overall.html')
def get_top_overall():
	j = Joke.objects.order_by('-rating')[:5]
	return {'first':j[:1], 'second':j[1:2], 'third':j[2:3], 'fourth':j[3:4], 'fifth':j[4:5]}
