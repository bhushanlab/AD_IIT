# threading module
import threading
import time

def sleep(n , name = "default"):
    print("Hello -- {}, spleeping for 5sec\n".format(name))
    time.sleep(n)
    print("waking up -- {}".format(name))

def counter(n = 5):
    counter = 0
    while counter < n:
        time.sleep(1) # just so this finish fisrt
        print("Sleeping -> {} second".format(counter))
        counter += 1

def main():
    t = threading.Thread(target=sleep, name = "thread 1", args= (5, "thread 1"))
    threads_list = []
    start_time = time.time()
    for i in range(5):
        naming = "thread-"+str(i)
        threads_list.append(threading.Thread(target= sleep, name = naming, \
        args = (5,naming)))
        threads_list[-1].start()
        print("{}  - > started".format(threads_list[i].name))

    for thread in threads_list:
        thread.join()
    end_time = time.time() - start_time
    print("all thread finished, main thead proceed {}".format(end_time))



if __name__ == "__main__":
    main()
