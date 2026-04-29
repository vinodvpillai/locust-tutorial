from locust import HttpUser, task, constant
from dotenv import load_dotenv
from os import environ

load_dotenv()


class MyScript(HttpUser):
    host = "https://reqres.in"
    wait_time = constant(1)

    def on_start(self):
        self.client.headers.update(
            {
                "x-api-key": environ.get("REQRES_IN_API_KEY", ""),
            }
        )

    @task
    def get_users(self):
        response = self.client.get("/api/users")
        print(response.json())

    @task
    def create_user(self):
        response = self.client.post(
            "/api/register",
            data="""
        {
            "email": "test@gmail.com",
            "password": "123456"
        }
        """,
        )
        print(response.json())
