from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(10):
        print(i * i)
        time.sleep(0.1)


processes = []
num_processes = os.cpu_count()


# Create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

if __name__ == '__main__':
    # Start
    for p in processes:
        p.start()

    # join - means to wait for a process to finish and block the main thread
    for p in processes:
        p.join()

print(os.cpu_count())
print('end main')
#########

from multiprocessing import Process
import os
import time

from threading import Thread
def square_numbers():
    for i in range(10):
        print(i * i)
        time.sleep(0.1)


threads = []
num_threads = 10


# Create threads
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

if __name__ == '__main__':
    # Start
    for t in threads:
        t.start()

    # join 
    for t in threads:
        t.join()

#print(os.cpu_count())
print('end main')
