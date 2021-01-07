from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# REST FRAMEWORK 는 router라는 개념을 통해서 url을 결정하는구나

router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
