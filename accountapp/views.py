from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello_world(request):
    # return HttpResponse('안녕하세요')

    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html', context={'text':'POST METHOD!!'})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text':'GET METHOD!!'})