import requests
import json

url = 'http://localhost:8000/tasks'

def bulk_create_tasks(num_task=5):
    for i in range(num_task):
        task_data = {
            "title": f"Auto task {i+1}",
            "description": f"Automated task number {i+1}",
            "status": "pending",
            "duedate": f"2025-07-{20 + i:02d}"
        }
        try:
            resp = requests.post(url, json=task_data)
            resp.raise_for_status()
            created_task = resp.json()
            print(f"Created task {i+1}: {created_task['title']}")
        except requests.exceptions.RequestException as e:
            print(f"Error in task {i+1}: {e}")
    print("Tasks creation completed\n")

def read_tasks():
    res = requests.get(url)
    data = res.json()
    i=0
    print("......Reading tasks.......")
    print(data)
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

def get_pending_task(taskid):
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

# bulk_create_tasks()
read_tasks()
# get_specific_task('task123')