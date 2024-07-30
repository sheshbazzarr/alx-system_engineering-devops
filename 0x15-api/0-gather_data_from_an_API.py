#!/usr/bin/python3
""" 
This script retrieves and displays the TODO list progress for a given employee using a REST API.

Requirements:
- Use the `requests` module to fetch data from the API.
- Accept an integer as a parameter representing the employee ID.
- Display the progress in the following format:
  - First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    - EMPLOYEE_NAME: name of the employee
    - NUMBER_OF_DONE_TASKS: number of completed tasks
    - TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
  - Subsequent lines: Display titles of completed tasks with 1 tabulation and 1 space before the TASK_TITLE.

"""
import requests
import sys
if __name__=="__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = user = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    username = requests.get(url + "users/{}".format(sys.argv[1])).json()
    completed = [t.get("title") for t in user if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        username.get("name"), len(completed), len(user)))
    [print("\t {}".format(c)) for c in completed]
