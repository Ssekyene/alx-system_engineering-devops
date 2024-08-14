#!/usr/bin/python3
"""
Script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress
Example usage: python3 0-gather_data_from_an_API.py 2
"""

import json
import requests
from sys import argv


def getEmployeeProgress(employeeId):
    """function to process employee todo tasks"""

    userId = employeeId
    userUrl = f"https://jsonplaceholder.typicode.com/users/{userId}"
    todoUrl = f"https://jsonplaceholder.typicode.com/todos?userId={userId}"

    userRes = requests.get(userUrl)
    userInfo = userRes.json()
    userName = userInfo.get("name")

    todoRes = requests.get(todoUrl)
    todoData = todoRes.json()

    doneTasks = 0
    totalTasks = 0
    completedTasks = []

    for task in todoData:
        if task.get("completed"):
            doneTasks += 1
            completedTasks.append(task.get("title"))
        totalTasks += 1

    print(f"Employee {userName} is done with tasks({doneTasks}\
/{totalTasks}):")
    for title in completedTasks:
        print(f"\t {title}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: script <employee id>")
    else:
        getEmployeeProgress(argv[1])
