from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from farms.views import FarmViewSet,ZoneViewSet
from actions.views import ActionViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'farms', FarmViewSet)
router.register(r'zones', ZoneViewSet)
router.register(r'actions', ActionViewSet)





urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^auth/login/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^auth/', include('djoser.urls')),
    url(r'^activity/', include('actstream.urls')),

    url(r'^api/', include(router.urls)),
]
