#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import csv
import requests
import sys


def export_to_csv(user_id):
    # url
    url = 'https://jsonplaceholder.typicode.com/users/'

    # Fetching data from API
    response = requests.get(url + '{}/todos'.format(user_id))
    todos = response.json()

    # Getting employee name
    user_response = requests.get(url + '{}'.format(user_id))
    user_data = user_response.json()
    username = user_data['name']

    # Calculating progress
    total_tasks = len(todos)
    completed_tasks = sum(todo['completed'] for todo in todos)

    # Writing data to csv file
    filename = '{}.csv'.format(user_id)
    with open(filename, 'w', newline='') as csv_file:
        for todo in todos:
            csv_file.write('"{}","{}","{}","{}"\n'
                           .format(user_id, username, todo.get('completed'),
                                   todo.get('title')))


if __name__ == '__main__':
    # Gets user ID
    if len(sys.argv) != 2:
        print("Usage: python3 {}  <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = int(sys.argv[1])

    export_to_csv(user_id)
