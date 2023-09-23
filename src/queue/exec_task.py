import time
import json

def exec_task(thread_queue, tasks, url):
    while not thread_queue.empty():
        start_time = time.time()
        (priority, task, function) = thread_queue.get()
        for task_old in tasks:
             if task['uuid'] == task_old['uuid'] :
                if task_old['status'] == 'completed':
                    return
        return_value = function()
        for task_old in tasks:
             if task['uuid'] == task_old['uuid'] :
                task_old['status'] = 'completed'
                task_old['execution_time'] = time.time() - start_time
        with open(url, 'w') as f:
            json.dump(tasks, f, indent=4)
        return  return_value


