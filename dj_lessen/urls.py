from django.contrib import admin
from django.urls import path

from lessen1.views import time, home, workdir

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('time/', time, name='time'),
    path('workdir/', workdir, name='workdir')
]