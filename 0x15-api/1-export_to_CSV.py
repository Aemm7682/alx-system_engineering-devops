#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
script to export data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""

import csv
from requests import get
from sys import argv


if __name__ == "__main__":
    result_1 = get('https://jsonplaceholder.typicode.com/todos/')
    data = result_1.json()
    result_2 = get('https://jsonplaceholder.typicode.com/users/')
    data2 = result_2.json()

    for i in data2:
        if i.get('id') == int(argv[1]):
            employee = i.get('username')
    csvfile = argv[1] + ".csv"
    with open(csvfile, "w", newline="") as file:
        csv_file = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in data:
            if i.get("userId") == int(argv[1]):
                csv_file.writerow([i.get("userId"), employee,
                                   i.get("completed"), i.get("title")])
