import queue
import uuid

from src.json.check_json_file import check_json_file 

import functools

# Définition de la fonction pour ajouter des tâches à la file d'attente avec priorité
def add_task(function, args, priority,thread_queue,tasks,url,status):

    task = {"uuid": 'uuid:' + str(priority) ,"function": function.__qualname__, "priority": priority,"status": status}


    if check_json_file(url) :
        with open(url) as file_temp:
          datas = json.load(file_temp)
        for i in range(len(datas)):
            if datas[i]['status'] != "completed"  and  datas[i]['status'] == 'working':
              if(task['uuid'] == datas[i]['uuid']) :
                thread_queue.put((priority, task, functools.partial(function, *args)))
                tasks.append(task)
            else :
              if(task['uuid'] == datas[i]['uuid']):
                tasks.append(datas[i])

    else :
        thread_queue.put((priority, task, functools.partial(function, *args)))
        tasks.append(task)


