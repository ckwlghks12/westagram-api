import json
from django.views import View
from django.http  import JsonResponse
from .models import User
# Create your views here.


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        User(
            username = data['username'],
            password = data['password']
        ).save()

        return JsonResponse({'message':'회원가입이 완료 되었습니다.'},status=200)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        if User.objects.filter(username = data['username']).exists() :
            user = User.objects.get(username = data['username'])
            if user.password == data['password'] :
                return JsonResponse({'message':f'{user.email}님 로그인 성공'}, status=200)
            else :
                return JsonResponse({'message':'비밀번호가 틀렸습니다.'},status=200)

        return JsonResponse({'message':'등록되지 않은 이메일 입니다.'},status=200)
 