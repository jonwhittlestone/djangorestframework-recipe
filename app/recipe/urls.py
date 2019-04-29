from django.urls import path, include

# DefaultRouter: automatically generate the urls for our viewset
from rest_framework.routers import DefaultRouter
from recipe import views

# automatically generate our urls for our viewset
router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
