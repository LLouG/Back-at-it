from threading import Thread, Lock, current_thread
from queue import Queue
def worker(q, lock):
    while True:
        value = q.get()
        with lock:
            print("in {} got {}".format(current_thread().name, value))
        q.task_done()
if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    num_threads = 4
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon=True
        thread.start()
    for i in range(1, 21):
        q.put(i)
    q.join()
    print('end main')
