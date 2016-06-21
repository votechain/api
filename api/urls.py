from django.conf.urls import url

from api.views import VoteView

urlpatterns = [
    url(r'^votes/$', VoteView.as_view(), name='api'),
]
