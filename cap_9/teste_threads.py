import threading

THREADS = 10


def printa_hello(tid):
    print(f"ola da thread {tid}")


threads = []

for i in range(THREADS):
    print(f"programa principal criando thread {i}")

    thread = threading.Thread(target=printa_hello, args=(i,))
    threads.append(thread)

    try:
        thread.start()

    except Exception as e:
        print(f"Ops, erro o criar thread: {e}")

    for threand in threads:
        thread.join()

    print("Todasas threads terminaram")
