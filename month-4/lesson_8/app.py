import threading
import time

done = False


def worker(text):
    counter = 0
    while not done:
        if counter == 5:
            break
        counter += 1
        print(f"{counter}: {text}")
        time.sleep(1)


def worker1(text):
    counter = 0
    while not done:
        if counter == 3:
            break
        counter += 1
        print(f"{counter}: {text}")
        time.sleep(1)


th1 = threading.Thread(target=worker, daemon=True, args=("salom",))
th2 = threading.Thread(target=worker, daemon=True, args=("salom",))
th1.start()
th2.start()


input("Enter stop to stop: ")
done = True
