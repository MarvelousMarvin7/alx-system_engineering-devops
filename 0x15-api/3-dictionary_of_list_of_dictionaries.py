#!/usr/bin/python3
"""export data in the JSON format"""


if __name__ == "__main__":
    import json
    import requests

    url_user = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url_user).json()

    all_data = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url_todo = "https://jsonplaceholder.typicode.com/todos?userId={}"\
            .format(user_id)
        todos = requests.get(url_todo).json()
        all_data[user_id] = [{"username": username,
                              "task": todo.get("title"),
                              "completed": todo.get("completed")}
                             for todo in todos]

    filename = "todo_all_employees.json"

    with open(filename, mode='w') as jsonfile:
        json.dump(all_data, jsonfile)
