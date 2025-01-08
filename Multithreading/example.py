import time
import threading
def boys():
    for num in range(1,6):
        print(num)
        time.sleep(1)
def girls():
    for num in range(11,16):
        print(num)
        time.sleep(1)
T1 = threading.Thread(target=boys)
T2 = threading.Thread(target=girls)
T1.start()
T2.start()
T2.join()