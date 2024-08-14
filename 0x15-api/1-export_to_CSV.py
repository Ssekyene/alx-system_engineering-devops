#!/usr/bin/python3
"""
Script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress
export data in the CSV format
Example usage: python3 1-export_to_CSV.py 2
"""

from csv import DictWriter, QUOTE_ALL
import json
import requests
from sys import argv


def writeToCSV(data, userId):
    """
    exports json data to csv
    """
    with open(f"{userId}.csv", "w") as file:
        fields = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                  "TASK_TITLE"]
        csvWriter = DictWriter(file, fieldnames=fields, quoting=QUOTE_ALL)
        for d in data:
            csvWriter.writerow(d)
    return


def getEmployeeProgress(employeeId):
    """
    process employee's todo task progress
    """

    userId = employeeId

    userUrl = f"https://jsonplaceholder.typicode.com/users/{userId}"
    todoUrl = f"https://jsonplaceholder.typicode.com/todos?userId={userId}"

    userRes = requests.get(userUrl)
    userInfo = userRes.json()
    userName = userInfo.get("username")

    todoRes = requests.get(todoUrl)
    todoData = todoRes.json()

    data = []

    for task in todoData:
        usersDetails = {"USER_ID": userId,
                        "USERNAME": userName,
                        "TASK_COMPLETED_STATUS": task.get("completed"),
                        "TASK_TITLE": task.get("title")}
        data.append(usersDetails)
    return data


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: script <employee id>")
    else:
        data = getEmployeeProgress(argv[1])
        writeToCSV(data, argv[1])
