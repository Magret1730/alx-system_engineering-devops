#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == '__main__':
    # url
    url = 'https://jsonplaceholder.typicode.com/users/'

    # Gets employee ID
    if len(sys.argv) != 2:
        print("Usage: python3 {}  <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetching data from API
    response = requests.get(url + '{}/todos'.format(employee_id))
    todos = response.json()

    # Getting employee name
    user_response = requests.get(url + '{}'.format(employee_id))
    user_data = user_response.json()
    employee_name = user_data['name']

    # Calculating progress
    total_tasks = len(todos)
    completed_tasks = sum(todo['completed'] for todo in todos)

    # Displaying progress
    print('Employee {} is done with tasks({}/{})'
          .format(employee_name, completed_tasks, total_tasks))

    # display the title of completed tasks
    for todo in todos:
        if todo['completed']:
            print('\t {}'.format(todo["title"]))
