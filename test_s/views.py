from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

# appname = "test_s"

def test_s(request):
    # t= render_to_string('test_s/test_s.html')
    # return HttpResponse(t)
    # return HttpResponse("test_s/test_s111111")
    return render(request, 'test_s/test_s.html', {})