from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from farms.views import FarmViewSet, ZoneViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'farms', FarmViewSet)
router.register(r'zones', ZoneViewSet)




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),
    url(r'^api/', include(router.urls)),
]
