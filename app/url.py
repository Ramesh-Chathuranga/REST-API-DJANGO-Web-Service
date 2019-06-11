from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/login/', admin.site.urls),
    path('api/v1/companys/', include('miriapp.url.company_urls')),
    path('api/v1/employees/', include('miriapp.url.employee_urls')),

]
