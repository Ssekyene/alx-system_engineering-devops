#!/usr/bin/python3
"""
Script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress
export data in the CSV format
Example usage: python3 2-export_to_JSON.py 2
"""

import json
import requests
from sys import argv


def toJson(dictList):
    """
    converts dictionary to json string
    """
    if dictList is None or dictList == {}:
        return "{}"
    return json.dumps(dictList)


def saveToJson(dictList, userId):
    """
    writes the json string to a json file
    """
    with open(userId + ".json", "w") as file:
        file.write(toJson(dictList))


def getEmployeeProgress(employeeId):
    """
    process employee's todo tasks
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
        usersDetails = {"task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": userName}
        data.append(usersDetails)
    return data


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: script <employee id>")
    else:
        data = getEmployeeProgress(argv[1])
        saveToJson({argv[1]: data}, argv[1])
