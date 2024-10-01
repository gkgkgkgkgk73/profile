from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework import status

import json
from .serializers import CareerSerializer
from .models import Career

# 비동기 처리를 위함.
from jk_profile.tasks import do_something, do_multi

# 논블로킹, 주기적인 체크 필요
def index(request):
    task = do_something.delay(4,4)
    
    while not task.ready():
        pass
    
    if task.successful():
        res = task.result
        return HttpResponse(res)
    else:
        return HttpResponse('Error: Task failed', status=400)

# 블로킹, 타임아웃 가능
def multi(request):
    task = do_multi.delay(4,4)
    
    try:
        result = task.get(timeout=10)
        return HttpResponse(result)
    except TimeoutError:
        return HttpResponse('Error: Task timed out', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return HttpResponse(f'Error: {str(e)}', status=403)

from django.core.cache import cache

def career(request):
# get에 레디스 캐시 적용
    if request.method == 'GET':
        career_list = cache.get(f'careerlist')
        if not career_list:
            career_list = Career.objects.all()
            try:
                serializer = CareerSerializer(career_list, many=True)
            except Exception as e:
                return HttpResponse(status=404)
            cache.set(f'careerllist', career_list)
            return JsonResponse(serializer.data, status=200, safe=False)
        else:
            return JsonResponse(career_list, status=200, safe=False)
    elif request.method == 'POST':
        # json 데이터 처리
        data = json.loads(request.body)
        
        # serializer 로 받아서 유효성 검증
        serializer = CareerSerializer(data=data)
        if serializer.is_valid():
            # 저장
            serializer.save()
            return JsonResponse(serializer.data, status=200, safe=False)
        else:
            return HttpResponse(status=403)