from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

    #coockie
    path('setcookie', setcookie),
    path('getcookie', showcookie),

    #request.session
    path('testcookie/', cookie_session),
    path('deletecookie/', cookie_delete),

    #request.session[]
    path('createsession/', create_session),
    path('accesssession/', access_session),
    path('deletesession/', delete_session),
]
