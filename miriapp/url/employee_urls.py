from django.conf.urls import url
from ..view import employee_view

urlpatterns = [
    url(r'^$', employee_view.EmployeeList.as_view()),
    url(r'^(?P<employee_id>[0-9]+)/$', employee_view.EmployeeDetail.as_view()),

]