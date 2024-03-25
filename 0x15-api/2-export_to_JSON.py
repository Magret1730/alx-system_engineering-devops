#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import json
import requests
import sys


def export_to_csv(user_id):
    # url
    url = 'https://jsonplaceholder.typicode.com/users/'

    # Fetching data from API
    response = requests.get(url + '{}/todos'.format(user_id))
    todos = response.json()

    # Getting user name
    user_response = requests.get(url + '{}'.format(user_id))
    user_data = user_response.json()
    username = user_data['username']

    # Calculating progress
    total_tasks = len(todos)
    completed_tasks = sum(todo['completed'] for todo in todos)

    # Creating tasks list
    tasks = []
    for todo in todos:
        task = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        }
        tasks.append(task)

    # Writing data to JSON file
    output = {str(user_id): tasks}
    filename = f'{user_id}.json'
    with open(filename, 'w') as json_file:
        json.dump(output, json_file)


if __name__ == '__main__':
    # Gets user ID
    if len(sys.argv) != 2:
        print("Usage: python3 {}  <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = int(sys.argv[1])

    export_to_csv(user_id)
