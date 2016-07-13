from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
            url(r'^foodCoop/', include('foodCoop.urls')),
                url(r'^admin/', admin.site.urls),
                ]
