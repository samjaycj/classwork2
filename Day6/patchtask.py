import requests
import json

url = 'http://localhost:8000/tasks'

def patch_tasks(taskid, status='pending'):
    apiurl = f"{url}/{taskid}"
    task_data = {
            "status": status,
        }
    try:
        resp = requests.patch(apiurl, json=task_data)
        resp.raise_for_status()
        Updated_task = resp.json()
        print(f"Updated task {taskid}: {json.dumps(Updated_task, indent=2)}")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Error: Task with Id: '{taskid}' is not found")
        else:
            print(f"Error in updating task id {taskid}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error updating task {taskid}: {e}")

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
# get_pending_task()
patch_tasks('no_task','test_status')