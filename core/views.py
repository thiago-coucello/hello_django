from django.shortcuts import HttpResponse;

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse("<div>"
                        "   <h1> Hello {}, age {} </h1>"
                        "</div>".format(nome, idade))