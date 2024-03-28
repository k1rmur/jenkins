import threading
import time
 
screwdriver = [threading.Semaphore(1) for i in range(5)]

def philosopher(index):
    time.sleep(2)

    left_screwdriver_index = index
    right_screwdriver_index = (index + 1) % 5
     
    if index == 4:
        screwdriver[right_screwdriver_index].acquire()
        screwdriver[left_screwdriver_index].acquire()    
    else:
        screwdriver[left_screwdriver_index].acquire()
        screwdriver[right_screwdriver_index].acquire()
    
    print(f"DOCTOR {index+9}: BLAST!")
    time.sleep(2)
     
    screwdriver[left_screwdriver_index].release()
    screwdriver[right_screwdriver_index].release()
 
philosopher_threads = []
for i in range(5):
    philosopher_threads.append(threading.Thread(target=philosopher, args=(i,)))
     
for thread in philosopher_threads:
    thread.start()

for thread in philosopher_threads:
    thread.join()