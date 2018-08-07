from django.conf.urls import url

from hello.views import HomePageView

app_name='hello'

urlpatterns = [

    url(r'^$', HomePageView.as_view(), name='home'),
]