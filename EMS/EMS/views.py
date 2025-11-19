from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome</h1><p>This is HTML from Django.</p>")