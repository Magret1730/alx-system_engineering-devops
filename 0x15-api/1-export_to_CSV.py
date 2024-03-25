#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import csv
import requests
import sys


def export_to_csv(user_id):
    # URL
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

    # Fetching data from API
    response = requests.get(url)
    todos = response.json()

    # Getting employee data
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data['username']

    # Writing data to CSV file
    filename = f'{user_id}.csv'
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user_id, username, todo['completed'],
                            todo['title']])


if __name__ == '__main__':
    # Gets user ID
    if len(sys.argv) != 2:
        print("Usage: python3 {}  <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = int(sys.argv[1])

    export_to_csv(user_id)
