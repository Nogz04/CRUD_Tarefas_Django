from django.http import HttpResponse

def teste_view(request):
    return HttpResponse('Hello, World!')

def index_view(request):
    return HttpResponse('<h1>Bem-vindo à página inicial!</h1>')