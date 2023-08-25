"""
    Resets the date of my todoist tasks.
    Because I like it that way.
"""


import os
from dotenv import load_dotenv
from todoist_api_python.api import TodoistAPI
# Service
import services.telegram_apprise as telmes


load_dotenv()

api = TodoistAPI(os.getenv("TODOIST_API_KEY"))
task_ids = []


def main():
    try:
        tasks = api.get_tasks()
        task_ids = [task.id for task in tasks]
    except Exception as error:
        print(error)

    for task_id in task_ids:
        try:
            update = api.update_task(task_id=task_id, due_string="Today")
            print(f"Task: {task_id} is updated")
        except Exception as error:
            print(error)
    telmes.message("All the tasks have been updated!")


if __name__ == "__main__":
    main()
