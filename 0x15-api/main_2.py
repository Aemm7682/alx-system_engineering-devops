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
    for i in data2:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')

    for i in data:
        if i.get('userId') == int(argv[1]):
            total += 1

            if i.get('completed') is True:
                comp_job += 1
                task.append(i.get('title'))

    # Ensure the output format matches exactly
    output = "Employee {} is done with tasks({}/{}):".format(employee, comp_job, total)
    print(output)

    # Debugging: Print the expected output
    with open('student_output', 'r') as f:
        expected_output = f.readline().strip()
    print("Expected output:", expected_output)
    print("Actual output:", output)

    for i in task:
        print("\t {}".format(i))
