from locust import HttpLocust, TaskSet, task

class MicroTaskSet(TaskSet):
    @task
    def send(l):
        l.client.get("/")

class MyLocust(HttpLocust):
    task_set = MicroTaskSet
    min_wait = 5000
    max_wait = 15000
    host = "http://nginx:9000"
