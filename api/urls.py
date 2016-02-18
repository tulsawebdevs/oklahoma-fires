from django.conf.urls import url

from .views import EventListView

urlpatterns = [
    url(r'^events/$', EventListView.as_view()),
]
