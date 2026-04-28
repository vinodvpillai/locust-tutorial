from locust import User, task, constant


class MyScript(User):
    wait_time = constant(1)

    @task
    def lauch(self):
        print("Launch method from locust-tutorial")

    @task
    def search(self):
        print("Search method from locust-tutorial")



# To run the application simply type:
# locust -f test/first-test.py 
