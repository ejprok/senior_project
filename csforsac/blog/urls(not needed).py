from django.conf.urls import include, url
from search import views as search_views

urlpatterns = [
    url('', search_views.home, name="blog_home")
]