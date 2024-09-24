import threading
import time

def simulate_io_task(file_name, duration):
    """Simulates a file download or processing task."""
    print(f"Starting download simulation for {file_name}...")
    time.sleep(duration)  # Simulate I/O delay
    print(f"Finished downloading {file_name}.")

def run_io_tasks():
    """Runs multiple I/O tasks using threading."""
    threads = []
    # Simulate downloading multiple files
    for i in range(5):
        thread = threading.Thread(target=simulate_io_task, args=(f"data_chunk_{i}.txt", 2))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()