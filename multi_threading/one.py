from time import sleep, perf_counter
from threading import Thread, active_count, current_thread, enumerate

start = perf_counter()


def show(somethink):
    print(f"start with {somethink}...")
    sleep(4)
    print(f"finish with {somethink}...")


# show("ali")
# show("kevin")


thread1 = Thread(target=show, args=("ali",), name="first")
thread2 = Thread(target=show, args=("kevin",), name="second")
# thread1.setName("first 1")

# thread1.setDaemon(True)
# thread2.setDaemon(True)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# print(thread1.getName())
end = perf_counter()

res = end - start

print(res.__round__())
# print(res)
