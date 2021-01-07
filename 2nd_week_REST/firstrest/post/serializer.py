from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        
        # id: 각 인스턴스에 붙이는 고유번호
        # detail page url => ***/post/id 형식
        # fields = '__all__'
        fields = ['id', 'title', 'body']
        
        # 사람들이 꼭 이건 못바꿨으면 좋겠어! RO 항목!
        read_only_fields = ('title', )