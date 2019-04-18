from django.http import HttpResponse


def hello(request):
    return HttpResponse("under HyTest files test successful ! ")