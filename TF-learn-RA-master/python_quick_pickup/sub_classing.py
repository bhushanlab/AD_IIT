# __init__
# run
# these are the advising method for overriding
import time
import threading

class MyThread(threading.Thread):
    def run(self):
        print("{} has started".format(self.getName()))
        # from the py source code
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs
        print("{} has finished".format(self.getName()))

class MyThreadOther(threading.Thread): # override the __init__ or Thread
    #def __init__(self, group=None, target=None, name = None, args=(), kwarg=None\
    #,*,daemon=None):
    def __init__(self, number, func, args):
        super(MyThreadOther,self).__init__()
        self.number = number
        self.func = func
        self.args = args
    def run(self):
        print("thread {} has started".format(self.number))
        self.func(*self.args)
        print("thread {} has finished".format(self.number))

def double(number, cycles):
    for i in range(cycles):
        number = number*2
    print(number)

def sleeper(n, name):
    print("I have being called, and i will sleep for 5 s --->{}".format(name))
    time.sleep(n)
    print("{} has woke up from sleeping".format(name))

def test_function(name):
    print("Started testfunction {}".format(name))
    time.sleep(3)
    print("testing function finished")

def main():
    thread_list = []
    for i in range(4):
        t_name = "thread:" + str(i)
        thread_list.append(MyThread(target=sleeper,name=t_name, \
                                    args=(5,t_name)))
        thread_list[-1].start()
    for item in thread_list:
        item.join()
    
    t_thread = threading.Thread(target=test_function, name= "testfunction",\
    args=("haha",)) # the |args=("arg1","arg2") must end with "," to indicate tuple
    print("my own test, start a thread without para")
    t_thread.start()
    t_thread.join()

    # class 2
    thread_list_other = []
    for i in range (50):
        thread_list_other.append(MyThreadOther(number = i + 1, func=double,\
        args = [i,15]))
        thread_list_other[-1].start()

    for thread in thread_list_other:
        thread.join()

    print("main finished")
    pass

if __name__ == "__main__":
    main()
