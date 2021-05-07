from django.shortcuts import render, reverse, redirect
from django.conf import settings


from .mixins import (
	FormErrors,
	RedirectParams,
	APIMixin
)

'''
Basic view for selecting query
'''
def index(request):

	if request.method == "POST":
		query = request.POST.get("query", None)
		if query:
			return RedirectParams(url = 'main:results', params = {"query": query})

	return render(request, 'main/index.html', {})



'''
Basic view for displaying results
'''
def results(request):

	query = request.GET.get("query", None)

	if query:
		results = APIMixin(query=query).get_data()

		if results:
			context = {
				"results": results,
				"query": query,
			}

			return render(request, 'main/results.html', context)
	
	return redirect(reverse('main:home'))


