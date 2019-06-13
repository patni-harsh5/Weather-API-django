from django.conf.urls import url
from hello.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    # url(r'^register/$', 'register', name='urlname')
    #url(r'^products/$', 'viewname', name='urlname'),
]
