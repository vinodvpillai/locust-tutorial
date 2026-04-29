from locust import User, task, constant


class MyScript(User):
    # When we define multiple User classes, we can assign different weights to each one. The higher the weight, the more likely it is to be selected.
    weight = 2
    # A User’s wait_time makes it easy to introduce delays after each task execution.
    wait_time = constant(1)

    @task
    def lauch(self):
        print("Launch method from MyScript")

    @task
    def search(self):
        print("Search method from MyScript")


# While running with 2 Class make sure to have (Number of Users = 4, Number of Ramp Up = 4)
class MySecondScript(User):
    #
    weight = 2
    wait_time = constant(1)

    @task
    def lauch(self):
        print("Launch method from MySecondScript")

    @task
    def search(self):
        print("Search method from MySecondScript")


# To run the application simply type:
# locust -f test/first-test.py
