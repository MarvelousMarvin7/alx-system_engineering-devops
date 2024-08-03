#!/usr/bin/python3
"""Python script that, using REST API,
for a given employee ID, returns information about his/her TODO list progress
"""

if __name__ == "__main__":
    import requests
    import sys

    eid = int(sys.argv[1])

    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(eid)
    user = requests.get(url_user).json()
    url_todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        eid)
    todos = requests.get(url_todo).json()

    employee_name = user.get('name')

    completed_tasks = [todo for todo in todos if todo.get('completed')]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          done_tasks,
                                                          total_tasks))
    for task in completed_tasks:
        print('\t {}'.format(task.get('title')))
