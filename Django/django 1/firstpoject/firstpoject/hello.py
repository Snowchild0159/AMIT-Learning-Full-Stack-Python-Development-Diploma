from django.http import HttpResponse
# MVT : 
# m for Models : any realtion with db 
# v for Views : buseniss logic
# T for Templates : UI : html, css, js
def say_hello(request):
    print(request.GET)
    name=  request.GET.get("name")
    return HttpResponse(f"<h1>Hello {name or 'World'}</h1> ") 
    