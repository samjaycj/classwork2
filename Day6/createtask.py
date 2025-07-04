import requests
import json

url = 'http://localhost:8000/tasks'

def create_tasks(num_task=5):
    task_data = {
            "id": "task111",
            "title": "Another new Task",
            "description": "Creating a new test task from python",
            "status": "in-progress",
            "dueDate": "2025-07-21"
        }
    try:
        resp = requests.post(url, json=task_data)
        resp.raise_for_status()
        created_task = resp.json()
        print(f"Created task {created_task['id']}: {created_task['title']}")
    except requests.exceptions.RequestException as e:
            print(f"Error in task creation: {e}")

def read_tasks():
    res = requests.get(url)
    data = res.json()
    i=0
    print("......Reading tasks.......")
    print(f"First item details: Title:{data[0]['title']}, Description: {data[0]['description']}")
    print("........All task list........")
    for item in data:
        i = i+1
        print(f"Task {i} : {item['title']}, with status {item['status']}")

def get_specific_task(taskid):
    print(f"Getting task with Id: {taskid}")
    apiurl = f"{url}/{taskid}"
    try:
        res = requests.get(apiurl)
        res.raise_for_status()
        task=res.json()
        print(f"Task {taskid}:")
        print(json.dumps(task, indent=2))
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Error: Task with Id: '{taskid}' is not found")
        else:
            print(f"Error in fetching task id {taskid}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching task {taskid}: {e}")

pending_list = []
def get_pending_task():
    print(f"Getting task with Pending status")
    apiurl = f"{url}"
    try:
        res = requests.get(apiurl)
        res.raise_for_status()
        tasks=res.json()
        for task in tasks:
            if task.get('status') == 'pending':
                pending_list.append(task)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Error: Task with Id:  is not found")
        else:
            print(f"Error in fetching task : {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching tasks: {e}")
    print(json.dumps(pending_list, indent=2))

# create_tasks()
# read_tasks()
# get_specific_task('task123')
get_pending_task()