#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
import sys


def export_to_json():
    # URL for fetching tasks
    url = 'https://jsonplaceholder.typicode.com/'

    # Dictionary to store tasks for all employees
    all_tasks = {}

    # Fetching data for all users
    response_users = requests.get(url + 'users')
    users = response_users.json()

    for user in users:
        user_id = user['id']
        username = user['username']

        # Fetching tasks for each user
        response_todos = requests.get(url + f"todos?userId={user_id}")
        todos = response_todos.json()

        # List to store tasks for the current user
        user_tasks = []

        # Processing tasks for the current user
        for todo in todos:
            task_info = {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            user_tasks.append(task_info)

        # Adding tasks for the current user to the dictionary
        all_tasks[user_id] = user_tasks

    # Writing data to JSON file
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == '__main__':
    export_to_json()
