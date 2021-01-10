from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = UserPost.objects.all()
    serializer_class = UserSerializer

    # SearchFilter 기반으로 검색할 예정입니다
    filter_backends = [SearchFilter]
    # search_fields 어떤 칼럼을 기반으로 검색을 할 건가요? (튜플로 해주세용()()())
    search_fields = ('title', 'body',)

    def get_queryset(self):
        # 여기 내부에서 쿼리셋을 지지고 볶은 다음에 return queryset을 하는게 좋음
        queryset = super().get_queryset() 
        # queryset = queryset.filter(author__id = 1)
        # 지금 로그인한 유저의 글만 필터링 해라! (로그인이 안된 상태라면 예외처리 필요)
        # queryset = queryset.filter(author=self.request.user)
        ## __FINAL__VERSION__

        # 만약 로그인이 되어있다면 해당 유저의 글만 리턴
        if self.request.user.is_authenticated:
            queryset = queryset.filter(author=self.request.user)
        # 만약 로그인이 안되어있다면 빈 쿼리셋 리턴
        else:
            queryset = queryset.none()
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)