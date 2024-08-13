#!/usr/bin/python3
"""Write a Python script that, using this REST API,
      for a given employee ID, returns information
      about his/her TODO list progress.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    comp_job = 0
    total = 0
    task = []
    result_1 = get('https://jsonplaceholder.typicode.com/todos/')
    data = result_1.json()
    result_2 = get('https://jsonplaceholder.typicode.com/users/')
    data2 = result_2.json()
    print(data)
    # for i in data2:
    #     if i.get('id') == int(argv[1]):
    #         employee = i.get('name')

    # for i in data:
    #     if i.get('userId') == int(argv[1]):
    #         total += 1

    #         if i.get('completed') is True:
    #             comp_job += 1
    #             task.append(i.get('title'))

    # print("Employee {} is done with tasks({}/{}):".format(employee, comp_job,
    #                                                       total))

    # for i in task:
    #     print("\t {}".format(i))
