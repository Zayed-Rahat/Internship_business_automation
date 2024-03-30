from locust import HttpUser, task,between

class WebsiteTestUser(HttpUser):
    # wait_time = between(5, 10)

    def on_start(self):

        pass

    def on_stop(self):

        pass

    @task(1)
    def hello_world(self):
        self.client.get("")