# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from . import views

# # REST FRAMEWORK 는 router라는 개념을 통해서 url을 결정하는구나

# router = DefaultRouter()
# router.register('post', views.PostViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

### API VIEW
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from post import views

# Default Router는 사용하지 않는다. API ROOT가 없기때문?

urlpatterns = [
    path('post/', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)