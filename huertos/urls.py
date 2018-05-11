from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from farms.views import FarmViewSet
from rest_framework_jwt.views import obtain_jwt_token

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'farms', FarmViewSet)




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/login/', obtain_jwt_token),
    url(r'^auth/', include('djoser.urls')),
    url(r'^activity/', include('actstream.urls')),
    url(r'^api/', include(router.urls)),

]
