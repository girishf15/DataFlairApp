from django.urls import include, path


urlpatterns = [
    path('', include('demo.urls')),
    path('', include('subscribe.urls')),
]
