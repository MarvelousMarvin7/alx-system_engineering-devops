#!/usr/bin/python3
"""export data in the CSV format"""


if __name__ == "__main__":
    import csv
    import requests
    import sys

    eid = int(sys.argv[1])

    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(eid)
    user = requests.get(url_user).json()
    url_todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        eid)
    todos = requests.get(url_todo).json()

    username = user.get('username')
    filename = "{}.csv".format(eid)

    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([eid, username,
                             todo.get('completed'),
                             todo.get('title')])
