from django.conf.urls import url
from ..view import company_view
from .. import tests


urlpatterns = [
     url(r'^$', company_view.CompanyList.as_view()),
    url(r'^(?P<company_id>[0-9]+)/$', company_view.CompanyDetail.as_view()),
    url(r'^a/$', tests.index,name='index'),

]