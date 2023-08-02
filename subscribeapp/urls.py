from django.urls import path

from subscribeapp.views import SubscriptionView, SubsriptionListView


app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubsriptionListView.as_view(), name='list'),
]