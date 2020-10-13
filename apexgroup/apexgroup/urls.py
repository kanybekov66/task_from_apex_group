from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('innsaver/', include('innsaver.urls')),
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
]