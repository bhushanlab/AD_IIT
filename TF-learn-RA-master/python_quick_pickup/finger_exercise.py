import threading
import queue
import time as t

def time_it(function):
    def wrapper(*args, **kwargs):
        start = t.time()
        result = function(*args, **kwargs)
        end = t.time()
        print("wapper called and ran " + str((end - start)) + "sec")
        return result
    return wrapper


@time_it
def double_numbers(arr):
    rt_arr = []
    for i in arr:
        rt_arr.append(i*2)
    return rt_arr


@time_it
def triple_numbers(arr):
    rt_arr = []
    for i in arr:
        rt_arr.append(i*3)
    return rt_arr


def enthread(target, args):
    q = queue.Queue()

    def wrapper():
        q.put(target(*args))
    t = threading.Thread(target=wrapper)
    t.start()
    return q

def main():
    arr = [1, 2, 3, 4, 1, 3, 4, 12, 4, 41, 213, 1, 4]
    #resultarr_1 = double_numbers(arr)
    #resultarr_2 = triple_numbers(arr)

    #print(resultarr_1)
    #print(resultarr_2)


    q1 = enthread(target=double_numbers,  args=(arr,))
    q2 = enthread(target=triple_numbers,  args=(arr,))

    print(q2.get())
    print(q1.get())

if __name__ == "__main__":
    main()
