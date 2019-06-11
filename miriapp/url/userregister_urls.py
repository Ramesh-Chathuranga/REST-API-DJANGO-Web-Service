from django.conf.urls import url
from ..view import user_view

urlpatterns = [
    url(r'^$', user_view.UserFormView.as_view()),
]