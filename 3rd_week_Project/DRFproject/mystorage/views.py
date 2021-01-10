from rest_framework import viewsets
from .models import Essay, Album, Files
from .serializers import EssaySerializer, AlbumSerializer, FilesSerializer
from rest_framework.filters import SearchFilter # Search 기능을 import 해와서 구현하자!
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

class EssayViewSet(viewsets.ModelViewSet):
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

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class FilesViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

    # parser_class -- 다양한 파일 형식의 인코딩을 지원해주자!
    parser_classes = (MultiPartParser, FormParser)
    
    # create logic -- POST 요청 따라서 포스트를 오버라이딩 해보자
    def post(self, request, *args, **kwargs):
        serializer = FilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.error, status=HTTP_400_BAD_REQUEST)
