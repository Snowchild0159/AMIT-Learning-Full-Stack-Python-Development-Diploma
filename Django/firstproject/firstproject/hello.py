from django.http import HttpResponse

def snow(request) : 
    print("shs is bubbs")
    return HttpResponse("<h1>SNOW<h1>")