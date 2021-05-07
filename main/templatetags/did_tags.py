from django import template
from datetime import datetime
from django.utils.timezone import make_aware

register = template.Library()


def unix(value):

	# you can pass the following obj to a DateTimeField, when your settings.USE_TZ == True
	datetime_obj_with_tz = make_aware(datetime.fromtimestamp(value))
	return datetime_obj_with_tz

register.filter('unix', unix)