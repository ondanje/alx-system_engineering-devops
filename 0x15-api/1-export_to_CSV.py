#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID,returns information
about his/her TODO list
"""
import sys
import requests
import csv

if __name__ == "__main__":
    employee_Id = sys.argv[1]

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_Id)
    response = requests.get(url)
    name = response.json()

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.\
        format(employee_Id)
    response = requests.get(url)
    tasks = response.json()

    file_name = f'{employee_Id}.csv'
    with open(file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        for task in tasks:
            csv_writer.writerow([employee_Id, name.get('name'),
                                 task.get('completed'), task.get('title')])
