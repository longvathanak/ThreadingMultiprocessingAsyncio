import threading
import time

def simulate_io_task(file_name, duration):
    print(f"Starting I/O task for {file_name}")
    time.sleep(duration)  
    print(f"Completed I/O task for {file_name}")

def run_io_tasks():
    threads = []
    files = ['file1.txt', 'file2.txt', 'file3.txt']  
    for file_name in files:
        t = threading.Thread(target=simulate_io_task, args=(file_name, 2))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()  