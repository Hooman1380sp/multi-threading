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
