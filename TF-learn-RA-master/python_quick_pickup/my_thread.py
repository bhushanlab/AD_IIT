import threading
import time

class Thread(threading.Thread):
    def __init__(self, thread_name, function_name, function_para):
        super(Thread, self).__init__()
        self.thread_name = thread_name
        self.function_name = function_name
        self.function_para = function_para
    # override the original __init__ for the threading.Thread

    def run(self):
        # after called run, next line run
        print("thread {} has started".format(self.thread_name)) 
        self.function_name(*self.function_para)
        # after the execution of testfunction,execting the next line
        print("thread {} has finished".format(self.thread_name))
        # function done next step is the join in main

def test_function(name):
    print("Hi my name is {}".format(name))
    time.sleep(5)
    print("{} is waking up".format(name))


my_thread= Thread("test thread", test_function, ("JJ",))
my_thread.start()
