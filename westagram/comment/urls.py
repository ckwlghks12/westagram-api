from django.urls import path, include
from .views import CommentView


urlpatterns = [
  path('', CommentView.as_view()) # 질문 main url 이랑 차이 경로 부분
]