from django.http import HttpResponse

def hello(request):
	name = 'Mike'
	html = '<html><bod> hi %s. this seems to have worked!</body></html>
	return HttpRespnse(html)