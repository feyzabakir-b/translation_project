from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from main.views import home, city_list
from rest_framework.routers import DefaultRouter
from main.views import CityViewSet

router = DefaultRouter()
router.register(r'cities', CityViewSet)

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cities/', city_list, name='city_list'),
    path('api/', include(router.urls)),
    prefix_default_language=False
)