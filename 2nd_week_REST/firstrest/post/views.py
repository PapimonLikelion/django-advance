####### API VIEW ########
# # 데이터 처리 대상
# from post.models import Post
# from post.serializer import PostSerializer
# # status에 따라 직접 Response를 처리할 것
# from django.http import Http404
# from rest_framework.response import Response
# from rest_framework import status
# # APIView를 상속받은 CBV
# from rest_framework.views import APIView
# # PostDetail 클래스의 get_object 메소드 대신 이거 써도 괜찮다
# # from django.shortcuts import get_object_or_404

####### Mixin ########
# from post.models import Post
# from post.serializer import PostSerializer

# from rest_framework import generics
# from rest_framework import mixins

####### API VIEW ########
# class PostList(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)   # 쿼리셋 넘기기 (many=True 인자)

#         return Response(serializer.data)                # 직접 Response 리턴해주기: serializer.data
    
#     def post(self, request):
#         serializer = PostSerializer(data = request.data)
#         if serializer.is_valid():   # 직접 유효성 검사
#             serializer.save()       # 저장
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ####### Mixin ########
# class PostList(mixins.ListModelMixin, mixins.CreateModelMixin, 
#                 generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

####### API VIEW ########
# # PostList 클래스와 달리 pk값을 받음 (메소드에 pk 인자 포함)
# class PostDetail(APIView):
#     # get_object_or_404를 구현해주는 helper function
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Http404
    
#     def get(self, request, pk, format=None):
#         post = self.get_object(pk)
#         # post = get_object_or_404(Post, pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # valid 하지 않음
    
#     def delete(self, request, pk, format=None):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

####### Mixin ########
# class PostDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
#                 mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

####### ViewSet #######
from post.models import Post
from post.serializer import PostSerializer

from rest_framework import viewsets

# @action 처리 
from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse

'''
# ReadOnlyModelViewSet은 말 그대로 ListView, DetailView의 ``조회``만 가능하다. 
class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
'''

# ModelViewSet은 CRUD가 모두 가능하다. 
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # 그냥 얍을 띄워주는 custom API
    # ~~/post/2/highlight ==> HTML에 얍 띄워줌
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("얍")