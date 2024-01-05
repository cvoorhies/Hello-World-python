from multiprocessing import Process, Value, Array, Lock
import time

def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.1)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1
        
if __name__ == '__main__':
    lock =Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    #shared_number = Value('i', 0)
    print('Array at beginning is', shared_array[:])#shared_number.value)

    p1 = Process(target=add_100, args=(shared_array, lock))# shared_number, the args is a tuble so it needs the ',' to indicate to python that it is one.
    p2 = Process(target=add_100, args=(shared_array, lock))
    p3 = Process(target=add_100, args=(shared_array, lock))
    p4 = Process(target=add_100, args=(shared_array, lock))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join() #waits for process to stop.
    p2.join()
    p3.join() #waits for process to stop.
    p4.join()


    print('Number at end is', shared_array[:])









"""    processes = []
    num_processes = os.cpu_count()


# Create processes
    for i in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p)


    # Start
    for p in processes:
        p.start()

    # join - means to wait for a process to finish and block the main thread
    for p in processes:
        p.join()

#print(os.cpu_count())
print('end main')"""
#########

"""from threading import Thread

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

if __name__ == '__main__':
    threads = []
    num_threads = 10


# Create threads
    for i in range(num_threads):
        t = Thread(target=square_numbers)
        threads.append(t)
        

    # Start
    for t in threads:
        t.start()

    # join 
    for t in threads:
        t.join()

    #print(os.cpu_count())
    print('end main')
"""

from multiprocessing import Pool
import time

def cube(number):
    return number * number * number
        
if __name__ == '__main__':
    
    numbers = range(10)
    pool = Pool()

    #map, apply, join, close 
    result = pool.map(cube, numbers)

    pool.close()
    pool.join()
    

    print(result)
