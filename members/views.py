from django.shortcuts import render, HttpResponse

# Create your views here.
def fun(request):
    return HttpResponse("Hello My love")
def fun2(request):
    return HttpResponse("Hello My Jaan")
def fun3(request):
    return HttpResponse("Hello My Baby")
def fun4(request):
    return HttpResponse("<b>Hello Kavya Mishra</b>")
def fun5(request,courseid):
    return HttpResponse(courseid)

def homePage(request):
    return render(request, "index.html")