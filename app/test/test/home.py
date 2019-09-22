from django.http import HttpResponse
import datetime

def hello(request):
    html = "<html><body>Hello, world!</body></html>"
    return HttpResponse(html)
