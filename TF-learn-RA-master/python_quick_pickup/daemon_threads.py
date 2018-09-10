import threading as th
import time as t

total = 4

def createP1 ():
    global total
    for i in range(10):
        t.sleep(2)
        print('Added Item @ sleep == 2')
        total +=1
    print("all created")

def createP2 ():
    global total
    for i in range(7):
        t.sleep(1)
        print("Added Item @ sleep == 1")
        total +=1
    print("all created")

def totalLimitChecker():
    global total
    total_limit = 5
    switch = True
    while switch:
        if total > total_limit:
            print("exceed total limit {}".format(total_limit))
            total -= 3
            print("substracted 3")
        else:
            t.sleep(1)
            print("waiting ...")

def main():
    create_thread_1 = th.Thread(target=createP1,name="createP1")
    create_thread_2 = th.Thread(target=createP2,name="createP2")
    limit_checker = th.Thread(target=totalLimitChecker,name="limit checker"\
    ,daemon=True) # daemon implemented
    create_thread_1.start(); create_thread_2.start(); limit_checker.start();
    
    create_thread_1.join(); create_thread_2.join(); #limit_checker.join()
    """
    here with only the create_thread_1 and create_thread_2 being join(), and we
    commented out the limit_checker, we are not waiting for the limit_checker
    anymore, thus after create_thread_1 and 2 join(), the main thread went to the
    print statement, then main exited, and since we made the limit_checker a 
    daemon thread, the program exited without waiting for it to responce, since
    there is no join called, and it is marked as daemon = True
    """
    print("total ends at -> {}".format(total))

if __name__ == "__main__":
    main()