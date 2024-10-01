from locust import HttpUser, task, between
class WebsiteTestUser(HttpUser):
    wait_time = between(1, 2.5) # 1초에서 2.5초 기다렸다가 요청하겠다. 기다리는건 1 ~ 2.5 초 랜덤

    # @task
    # def my_task(self):
    #     self.client.get('/jk_profile/index')
        
    @task
    def my_non_redis_task(self):
        self.client.get('/jk_profile/career')