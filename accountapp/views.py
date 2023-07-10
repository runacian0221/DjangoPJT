from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from accountapp.models import HelloWorld

# Create your views here.


def hello_world(request):
    # return HttpResponse('안녕하세요')

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        # 모든 오브젝트를 가져오기
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})