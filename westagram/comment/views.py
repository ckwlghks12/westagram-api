import json
from django.views import View
from django.http  import JsonResponse
from .models import Comment
# Create your views here.


class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)
        Comment(
            username = data['username'],
            comment = data['comment']
        ).save()

        return JsonResponse({'message':'SUCCESS'}, status=200)
        ## 질문 이상한값 입력시 실패코드는 자동 리턴?
    def get(self, request):
        return JsonResponse({'comment':list(Comment.objects.values())}, status=200)