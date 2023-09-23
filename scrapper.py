import queue
import json
import time

from src.queue.add_task import add_task
from src.queue.exec_task import exec_task 

# from exec.queue.optimize_function import optimize_function 


priority = 0
tasks= []
url = "queue/tasks.json"



#PROGRAMME
thread_queue = queue.PriorityQueue()
#function_map = {"load_json" : load_json}

#add_task(function_map['load_json'], [], 0,thread_queue,tasks,url,'working')

exec_task(thread_queue,tasks,url)

