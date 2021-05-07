from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
import requests
import json



'''
Handles form error that are passed back to AJAX calls
'''
def FormErrors(*args):
	message = ""
	for f in args:
		if f.errors:
			message = f.errors.as_text()
	return message


'''
Used to append url parameters when redirecting users
'''
def RedirectParams(**kwargs):
	url = kwargs.get("url")
	params = kwargs.get("params")
	response = redirect(url)
	if params:
		query_string = urlencode(params)
		response['Location'] += '?' + query_string
	return response


class APIMixin:

	def __init__(self, *args, **kwargs):

		self.query = kwargs.get("query")

	def get_data(self):

		full_url = f"https://api.postcodes.io/postcodes/{self.query}"
			
		r = requests.get(full_url)
		if r.status_code == 200:

			result = r.json()["result"]

			lat = result["latitude"]
			lng = result["longitude"]

			url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lng}&exclude=current,minutely,hourly,alerts&appid={settings.API_KEY}'
		
			r = requests.get(url)
			if r.status_code == 200:
				return r.json()['daily']
		return None



