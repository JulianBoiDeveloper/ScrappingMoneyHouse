import threading
import concurrent.futures

# def example_tache(num):
#     """Tâche longue et fastidieuse"""
#     print(f'Tâche {num} démarrée')
#     # Simulation de l'exécution d'une tâche longue et fastidieuse
#     import time
#     time.sleep(5)
#     print(f'Tâche {num} terminée')

def worker(num,function):
    """Fonction exécutée par chaque thread"""
    print(f'Thread {num} démarré')
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Découper la tâche en sous-tâches plus petites
        results = [executor.submit(function, i) for i in range(5)]
        # Attendre la fin de toutes les sous-tâches
        concurrent.futures.wait(results)
    print(f'Thread {num} terminé')



def multi_thread(num_thread,function):
    threads = []
    for num in range(num_thread):
        t = threading.Thread(target=worker, args=(num,function,))
        t.setDaemon(True)
        threads.append(t)
        t.start()

    # Attendre la fin de tous les threads
    for t in threads:
        t.join()

    print('Tous les threads se sont terminés.')


#multi_thread(12,example_tache)