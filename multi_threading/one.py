from time import sleep, perf_counter
from threading import Thread, active_count, current_thread, enumerate

# start = perf_counter()


# def show(somethink):
#     print(f"start with {somethink}...")
#     sleep(4)
#     print(f"finish with {somethink}...")


# show("ali")
# show("kevin")


# thread1 = Thread(target=show, args=("ali",), name="first")
# thread2 = Thread(target=show, args=("kevin",), name="second")
# thread1.setName("first 1")


# thread1.setDaemon(True)
# thread2.setDaemon(True)

# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()

# print(thread1.getName())
# end = perf_counter()
#
# res = end - start
#
# print(res.__round__())
# print(res)

# -----------------------------------------
# ThreadPoolExecutor

"""
  # we can do several operation.
"""

# from concurrent.futures import ThreadPoolExecutor
#
# start = perf_counter()
#
#
# def show(somethink):
#     print(f"start with {somethink}...")
#     sleep(4)
#     print(f"finish with {somethink}...")
#
#
# with ThreadPoolExecutor() as executer:
#     names = ["one", "tow", "three", "four", "five", "six"]
#     executer.map(show, names)
#
# print("Done...")
#
# end = perf_counter()
# res = end - start
#
# print(res.__round__())

# -----------------------------
# Lock, RLock
# Threading Safe

# from threading import Thread, RLock, Lock
#
# num = 0
# lock = Lock()
#
#
# # Normal lock
# def add():
#     global num
#     lock.acquire()
#     for _ in range(100000):
#         num += 1
#     print(num)
#     lock.release()
#
#
# # Dead lock
# def subtract():
#     global num
#     with lock:
#         for _ in range(100000):
#             num -= 1
#         print(num)
#
#
# thread1 = Thread(target=add)
# thread2 = Thread(target=subtract)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print(num)


# Semaphore and BoundedSemaphore

# from threading import BoundedSemaphore, Semaphore
#
# num = 0
#
# lock = Semaphore(3)
#
#
# def add():
#     global num
#     lock.acquire()
#     sleep(2)
#     num += 1
#     print(current_thread().getName())
#     lock.release()
#
#
# t1 = Thread(target=add)
# t2 = Thread(target=add)
# t3 = Thread(target=add)
# t4 = Thread(target=add)
# t5 = Thread(target=add)
# t6 = Thread(target=add)
# t7 = Thread(target=add)
# t8 = Thread(target=add)
# t9 = Thread(target=add)
#
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
# t7.start()
# t8.start()
# t9.start()
#
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
# t6.join()
# t7.join()
# t8.join()
# t9.join()


# timer
# from threading import Timer
#
#
# def show(obj_one):
#     print(f"{obj_one} is a your title object")
#
#
# t1 = Timer(interval=10, function=show, args=("blue",))
#
# t1.start()

# ----------------
# Event

# from threading import Event, Thread
#
#
# def one_show(one, tow):
#     sleep(9)
#     print("one_show ready")
#     one.set()
#     tow.wait()
#     print("one_show is finishing")
#     one.clear()
#
#
# def tow_show(one, tow):
#     print("tow_show ready")
#     tow.set()
#     one.wait()
#     print("tow_show is finishing")
#     tow.clear()
#
#
# one = Event()
# tow = Event()
#
# t1 = Thread(target=one_show, args=(one, tow))
# t2 = Thread(target=tow_show, args=(one, tow))
#
# t1.start()
# t2.start()

