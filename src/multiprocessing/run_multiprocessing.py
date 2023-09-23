import multiprocessing
import time

def run_multiprocessing(max_processes, num_processes, worker_func):
    semaphore = multiprocessing.Semaphore(max_processes)

    processes = []
    for i in range(num_processes):
        process = multiprocessing.Process(target=worker_func, args=(semaphore, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

def worker(semaphore, process_num):
    semaphore.acquire()
    print(f'Starting process {process_num}')
    time.sleep(5)
    print(f'Finishing process {process_num}')
    semaphore.release()

# if __name__ == '__main__':
#     run_multiprocessing(2, 5, worker)