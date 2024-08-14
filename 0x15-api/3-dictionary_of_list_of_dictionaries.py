#!/usr/bin/python3
"""
Script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress
export data in the json format for all the employees
Example usage: python3 3-dictionary_of_list_of_dictionaries.py
"""

import json
import requests
from sys import argv
from time import sleep


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


def getEmployeesProgress():
    """
    process all the employees' todo tasks
    """

    usersData = {}
    usersUrl = f"https://jsonplaceholder.typicode.com/users"
    usersRes = requests.get(usersUrl)
    usersInfo = usersRes.json()

    userIds = [u.get("id") for u in usersInfo]

    for uid in userIds:
        # sleep(1)
        userUrl = f"https://jsonplaceholder.typicode.com/users/{uid}"
        todoUrl = f"https://jsonplaceholder.typicode.com/todos?userId={uid}"

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

        usersData[uid] = data
    return usersData


if __name__ == "__main__":
    usersData = getEmployeesProgress()
    saveToJson(usersData, "todo_all_employees")
