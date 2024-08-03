#!/usr/bin/python3
"""export data in the JSON format"""


if __name__ == "__main__":
    import json
    import requests
    import sys

    eid = int(sys.argv[1])

    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(eid)
    user = requests.get(url_user).json()
    url_todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        eid)
    todos = requests.get(url_todo).json()

    username = user.get('username')
    filename = "{}.json".format(eid)

    data = {eid: [{"task": todo.get("title"),
                   "completed": todo.get("completed"),
                   "username": username} for todo in todos]}

    with open(filename, mode='w') as jsonfile:
        json.dump(data, jsonfile)
