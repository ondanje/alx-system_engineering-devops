#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID,returns information
about his/her TODO list
"""
import requests
import sys


if __name__ == "__main__":
    employee_Id = sys.argv[1]

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_Id)
    response = requests.get(url)
    name = response.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.\
        format(employee_Id)
    response = requests.get(url)
    tasks = response.json()
    done = 0
    completed_tasks = []

    for task in tasks:
        if task.get('completed'):
            completed_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, done, len(tasks)))

    for task in completed_tasks:
        print('\t {}'.format(task.get('title')))
