from django import template
from JokeRaterApp.models import Category, Joke

register = template.Library()

@register.inclusion_tag('JokeRater/cats.html')
def get_compare_list():
    return {'cats': Category.objects.all()}

@register.inclusion_tag('JokeRater/cats2.html')
def get_joke_list():
    return {'cats': Category.objects.all()}
	
@register.inclusion_tag('JokeRater/overall.html')
def get_top_overall():
    return {'overall':Joke.objects.order_by('-rating')[:5]}

@register.inclusion_tag('JokeRater/weekly.html')
def get_top_weekly():
    from datetime import date, timedelta
    import datetime
    start_date = datetime.datetime.now().date() - timedelta(days=7)
    end_date = datetime.datetime.now().date()
    j = Joke.objects.filter(datePosted__range=(start_date, end_date)).order_by('-rating')[:5]
    return {'weekly':j}
	
