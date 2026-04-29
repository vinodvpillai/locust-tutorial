from locust import HttpUser, task, constant, TaskSet


class MyScript(TaskSet):
    @task
    def get_status(self):
        self.client.get("/status/200")
        print("Got status code 200")


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyScript]
    wait_time = constant(1)
