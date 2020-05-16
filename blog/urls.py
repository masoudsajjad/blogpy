from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^$', views.IndexPage.as_view(), name='index'),
    url(r'^contact/$', views.ContactPage.as_view(), name='contact'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^category/$', views.CategoryPage.as_view(), name='category'),

]