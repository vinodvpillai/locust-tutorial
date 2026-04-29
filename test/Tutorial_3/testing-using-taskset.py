from locust import HttpUser, task, constant, TaskSet
import random


class MyScript(TaskSet):
    @task
    def get_status(self):
        self.client.get("/status/200")
        print("Got status code 200")
        # Interrupt and gives another task a chance
        self.interrupt()


class MySecondScript(TaskSet):
    @task
    def get_random_status(self):
        status_code = [100, 101, 102, 200, 201, 202]
        random_url = f"/status/{random.choice(status_code)}"
        self.client.get(random_url)
        print("Got random code")
        self.interrupt()


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyScript, MySecondScript]
    wait_time = constant(1)
