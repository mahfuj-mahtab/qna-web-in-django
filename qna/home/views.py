from django.shortcuts import render, HttpResponse,HttpResponseRedirect
def home(request):
    return render(request,"index.html")