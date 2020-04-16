from django.urls import path, include
from .views import SignUpView, SignInView

urlpatterns = [
  path('/sign-up', SignUpView.as_view()), # 질문 main url 이랑 차이 경로 부분
  path('/sign-in', SignInView.as_view()) 
]