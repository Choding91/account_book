from rest_framework import permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import Post
from posts.serializers import PostDetailSerializer, PostSerializer
import pyshorteners as ps


# 가계부 전체 조회 / 등록
class PostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        posts = user.post_user.all().order_by("-pk")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 가계부 상세 조회(+ 단축 URL) / 복제 / 수정 / 삭제
class PostDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        url = request.build_absolute_uri()
        sh = ps.Shortener()
        short_url = sh.dagd.short(url)
        if request.user == post.user:
            serializer = PostDetailSerializer(post)
            return Response((serializer.data, short_url), status=status.HTTP_200_OK)
        else:
            return Response({"message": "가계부 상세 조회 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post.id = None
        if request.user == post.user:
            serializer = PostDetailSerializer(post, data=post.__dict__)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "가계부 복제 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if request.user == post.user:
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "가계부 수정 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if request.user == post.user:
            post.delete()
            return Response({"message": "가계부가 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "가계부 삭제 권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN)
