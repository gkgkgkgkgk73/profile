import pytest
from django.urls import reverse
from jk_profile.tasks import do_something
from .models import Career
from rest_framework.test import APIClient
from rest_framework import status
import json

# Celery 비동기 작업을 실제 실행하지 않고 테스트할 수 있도록 Mock 처리
@pytest.fixture
def mock_do_something(mocker):
    mock_task = mocker.patch('jk_profile.tasks.do_something')
    mock_task.delay.return_value.ready.return_value = True
    mock_task.delay.return_value.successful.return_value = True
    mock_task.delay.return_value.result = 8  # 4 + 4의 결과를 모방
    return mock_task

@pytest.mark.django_db
def test_index_view(client, mock_do_something):
    # index 뷰 호출
    response = client.get(reverse('index'))
    
    # 상태 코드 확인 (200이어야 함)
    assert response.status_code == 200
    
    # HttpResponse의 값 확인 (결과는 '8'이어야 함)
    assert response.content == b'8'  # HttpResponse는 바이트로 반환됨

# @pytest.fixture
# def mock_do_multi(mocker):
#     mock_task = mocker.patch('jk_profile.tasks.do_multi')
#     mock_task.delay.return_value.ready.return_value = True
#     mock_task.delay.return_value.successful.return_value = True
#     mock_task.delay.return_value.result = 8  # 4 + 4의 결과를 모방
#     return mock_task

# @pytest.mark.django_db
# def test_multi_view(client, mock_do_multi):
    
#     # Call the multi view
#     response = client.get(reverse('multi'))
    
#     # Check status code
#     assert response.status_code == 200
    
#     # Check the content
#     assert response.content == b'16'

# @pytest.mark.django_db
# def test_multi_view_timeout(client, mocker):
#     # Simulate a timeout in the Celery task
#     mock_task = mocker.patch('jk_profile.tasks.do_multi')
#     mock_task.delay.return_value.get.side_effect = TimeoutError  # Simulate timeout
    
#     # Call the multi view
#     response = client.get(reverse('multi'))
    
#     # Check status code
#     assert response.status_code == 400
    
#     # Check if the content contains the timeout error message
#     assert response.content == b'Error: Task timed out'

@pytest.mark.django_db
def test_get_career(client, mocker):
    response = client.get(reverse('career'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_post_career(mocker):
    client = APIClient()
    response = client.post(reverse('career'), data=json.dumps({
                                'name' : 'PetBook',
                                'period' : '2023.01 ~',
                                'description' : {},
                                'role' : 'Full Stack'
                           }
    ), content_type='application/json')
    assert response.status_code == 200

@pytest.mark.django_db
def test_post_career_failure(mocker):
    client = APIClient()
    response = client.post(reverse('career'), data=json.dumps({
                           }
    ), content_type='application/json')
    assert response.status_code == 403