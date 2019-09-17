import multiprocessing
import time


def withdraw(balance):
    for _ in range(10000):
        balance.value = balance.value - 1


def deposit(balance):
    for _ in range(10000):
        balance.value = balance.value + 1


def perform_transactions():
    balance = multiprocessing.Value('i', 100)

    p1 = multiprocessing.Process(target=withdraw, args=(balance,))
    p2 = multiprocessing.Process(target=deposit, args=(balance,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final balance = {}".format(balance.value))


if __name__ == "__main__":
    t = time.time()
    for _ in range(10):
        perform_transactions()
    print(time.time() - t)
