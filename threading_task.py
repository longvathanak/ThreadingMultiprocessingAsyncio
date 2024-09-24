import threading
import time

# Simulate I/O task (e.g., downloading or processing a file)
def simulate_io_task(file_name, duration):
    print(f"Starting I/O task for {file_name}")
    time.sleep(duration)  # Simulate download or file processing time
    print(f"Completed I/O task for {file_name}")

# Run multiple I/O tasks concurrently using threading
def run_io_tasks():
    threads = []
    files = ['file1.txt', 'file2.txt', 'file3.txt']  # Simulating file downloads
    for file_name in files:
        t = threading.Thread(target=simulate_io_task, args=(file_name, 2))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()  # Wait for all threads to complete