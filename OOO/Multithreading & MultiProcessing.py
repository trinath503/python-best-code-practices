# multiprocessing (ideal for CPU-bound tasks) and threading (suited for IO-bound tasks). 



import threading
import multiprocessing
import time

# Function to simulate a CPU-bound task
def cpu_bound_task(n):
    result = 0
    for i in range(n):
        result += i
    return result

# Function to simulate an IO-bound task
def io_bound_task(n):
    time.sleep(n)  # Simulate IO-bound operation
    return "Task completed after {} seconds".format(n)

if __name__ == "__main__":
    # Multithreading example for CPU-bound task
    start_time = time.time()
    threads = []
    for _ in range(5):
        thread = threading.Thread(target=cpu_bound_task, args=(10**7,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    end_time = time.time()
    print("Multithreading (CPU-bound) took {:.2f} seconds".format(end_time - start_time))

    # Multiprocessing example for CPU-bound task
    start_time = time.time()
    processes = []
    for _ in range(5):
        process = multiprocessing.Process(target=cpu_bound_task, args=(10**7,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()
    end_time = time.time()
    print("Multiprocessing (CPU-bound) took {:.2f} seconds".format(end_time - start_time))

    # Multithreading example for IO-bound task
    start_time = time.time()
    threads = []
    for _ in range(5):
        thread = threading.Thread(target=io_bound_task, args=(2,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    end_time = time.time()
    print("Multithreading (IO-bound) took {:.2f} seconds".format(end_time - start_time))

    # Multiprocessing example for IO-bound task
    start_time = time.time()
    processes = []
    for _ in range(5):
        process = multiprocessing.Process(target=io_bound_task, args=(2,))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()
    end_time = time.time()
    print("Multiprocessing (IO-bound) took {:.2f} seconds".format(end_time - start_time))


"""

In the code, we define two types of tasks: cpu_bound_task and io_bound_task.

  cpu_bound_task performs a CPU-bound computation by adding numbers in a loop.
  io_bound_task simulates an IO-bound task by sleeping for a specified amount of time.

We then demonstrate the use of multithreading and multiprocessing for both types of tasks.

For CPU-bound tasks:

   Multithreading: We create multiple threads, each executing the cpu_bound_task. However, due to Python's Global Interpreter Lock (GIL), multithreading in Python doesn't provide true parallelism for CPU-bound tasks.
   Multiprocessing: We create multiple processes, each executing the cpu_bound_task. Multiprocessing allows true parallelism as each process runs in a separate memory space.
For IO-bound tasks:

  Multithreading: We create multiple threads, each executing the io_bound_task. Multithreading is suitable for IO-bound tasks because threads can overlap IO operations, allowing for better utilization of CPU time.
  Multiprocessing: We create multiple processes, each executing the io_bound_task. Although multiprocessing can also handle IO-bound tasks, it incurs additional overhead compared to multithreading due to the creation of separate processes. However, it can still be beneficial for IO-bound tasks that release the GIL.

Finally, we measure and print the execution times for each approach.

"""
