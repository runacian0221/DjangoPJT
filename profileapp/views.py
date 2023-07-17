from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:detail')
    # detail은 pk가 필요하고 따로 넘겨줄 수 있는 방법이 없어 다른 방법을 사용
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)
    
    # model의 profile 클래스의 user의 pk를 찾아서 detail에 넘겨줌
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

        # model의 profile 클래스의 user의 pk를 찾아서 detail에 넘겨줌
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})