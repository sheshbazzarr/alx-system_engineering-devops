## 0x15. API

# 0-gather_data_from_an_API
## TODO List Progress Script

This Python script retrieves and displays the TODO list progress for a given employee using a REST API.

## Requirements

- Use the `requests` module to fetch data from the API.
- Accept an integer as a parameter representing the employee ID.
- Display the progress in the following format:
  - **First line:** Employee `EMPLOYEE_NAME` is done with tasks(`NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS`):
    - `EMPLOYEE_NAME`: name of the employee
    - `NUMBER_OF_DONE_TASKS`: number of completed tasks
    - `TOTAL_NUMBER_OF_TASKS`: total number of tasks, which is the sum of completed and non-completed tasks
  - **Subsequent lines:** Display titles of completed tasks with 1 tabulation and 1 space before the `TASK_TITLE`.

#1-export_to_csv

This script retrieves and displays the TODO list progress for a given employee using a REST API,
and exports the data to a CSV file.

Requirements:
- Use the `requests` module to fetch data from the API.
- Accept an integer as a parameter representing the employee ID.
- Display the progress in the following format:
  - First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    - EMPLOYEE_NAME: name of the employee
    - NUMBER_OF_DONE_TASKS: number of completed tasks
    - TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
  - Subsequent lines: Display titles of completed tasks with 1 tabulation and 1 space before the TASK_TITLE.
- Export data to a CSV file with the following format:
  - "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
  - File name must be: USER_ID.csv

# 2-export_to_csv
This script retrieves and displays the TODO list progress for a given employee using a REST API,
and exports the data to a JSON file.

Requirements:
- Use the `requests` module to fetch data from the API.
- Accept an integer as a parameter representing the employee ID.
- Display the progress in the following format:
  - First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    - EMPLOYEE_NAME: name of the employee
    - NUMBER_OF_DONE_TASKS: number of completed tasks
    - TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
  - Subsequent lines: Display titles of completed tasks with 1 tabulation and 1 space before the TASK_TITLE.
- Export data to a JSON file with the following format:
  - { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
  - File name must be: USER_ID.json
Run the script from the command line with the employee ID as an argument:

```sh
python script.py 1


Date july 30,2024
