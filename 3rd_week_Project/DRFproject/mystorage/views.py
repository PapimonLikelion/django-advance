from rest_framework import viewsets
from .models import Essay
from .serializers import EssaySerializer
from rest_framework.filters import SearchFilter # Search 기능을 import 해와서 구현하자!

class PostViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body') # Search 기능을 만들때에는 튜플로써 작성하자!

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # 현재 request를 보낸 유저 == self.request.user
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated: # 로그인 되어 있다면
            queryset = queryset.filter(author=self.request.user)
        else:
            queryset = queryset.none()
        return queryset