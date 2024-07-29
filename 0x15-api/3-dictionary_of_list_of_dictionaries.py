#!/usr/bin/python3
"""
Script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress
export data in the CSV format
"""

import json
import requests
from sys import argv
from time import sleep


def to_json(dict_list):
    """
    converts dictionary to json string
    """
    if dict_list is None or dict_list == []:
        return "[]"
    return json.dumps(dict_list)


def save_to_file(dict_list, user):
    """
    writes the json string to a json file
    """
    with open(user + ".json", "w") as file:
        file.write(to_json(dict_list))


if __name__ == "__main__":

    user_data = {}

    base_url = "https://jsonplaceholder.typicode.com/"
    users_url = f"https://jsonplaceholder.typicode.com/users"

    users_res = requests.get(users_url)
    users_info = users_res.json()
    uids = [u["id"] for u in users_info]
    for i in uids:
        sleep(1)
        user_url = f"https://jsonplaceholder.typicode.com/users/{i}"
        todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={i}"

        user_res = requests.get(user_url)
        user_info = user_res.json()
        user_name = user_info.get("username")

        todo_res = requests.get(todo_url)
        todo_data = todo_res.json()

        data = []

        for task in todo_data:
            users_info = {"task": task.get("title"),
                          "completed": task.get("completed"),
                          "username": user_name}
            data.append(users_info)

        user_data[i] = data

    save_to_file(user_data, "todo_all_employees")
