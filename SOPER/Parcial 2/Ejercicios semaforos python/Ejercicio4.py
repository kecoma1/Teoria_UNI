import threading
import time
import random

# El problema esta simplificado, solo se puede ir hacia delante, no se puede girar

# Semáforos para cada celda
Z1 = threading.Semaphore(1)
Z2 = threading.Semaphore(1)
Z3 = threading.Semaphore(1)
Z4 = threading.Semaphore(1)

mutex = threading.Semaphore(1)

# Valor de las celdas
_1 = 0
_2 = 0
_3 = 0
_4 = 0

def coche(origen, destino):
    global _1, _2, _3, _4
    if origen == 1 and destino == 3:
        while True:
            mutex.acquire()
            if (_2, _3) == (0, 0):
                _2 = 1
                _3 = 1
                Z2.acquire()
                Z3.acquire()
                mutex.release()
                break
            else:
                mutex.release()

        # El coche cruza
        print("1---->3, utilizo Z2, y Z3")
        time.sleep(random.randint(1, 5))

        mutex.acquire()
        _2 = 0
        _3 = 0
        Z2.release()
        Z3.release()
        mutex.release()
    elif origen == 3 and destino == 1:
        while True:
            mutex.acquire()
            if (_4, _1) == (0, 0):
                _4 = 1
                _1 = 1
                Z4.acquire()
                Z1.acquire()
                mutex.release()
                break
            else:
                mutex.release()

        # El coche cruza
        print("3---->1, utilizo Z4, y Z1")
        time.sleep(random.randint(1, 5))

        mutex.acquire()
        _4 = 0
        _1 = 0
        Z4.release()
        Z1.release()
        mutex.release()
    elif origen == 2 and destino == 4:
        while True:
            mutex.acquire()
            if (_3, _4) == (0, 0):
                _3 = 1
                _4 = 1
                Z3.acquire()
                Z4.acquire()
                mutex.release()
                break
            else:
                mutex.release()

        # El coche cruza
        print("2---->4, utilizo Z3, y Z4")
        time.sleep(random.randint(1, 5))

        mutex.acquire()
        _3 = 0
        _4 = 0
        Z3.release()
        Z4.release()
        mutex.release()
    elif origen == 4 and destino == 2:
        while True:
            mutex.acquire()
            if (_1, _2) == (0, 0):
                _1 = 1
                _2 = 1
                Z1.acquire()
                Z2.acquire()
                mutex.release()
                break
            else:
                mutex.release()

        # El coche cruza
        print("4---->2, utilizo Z1, y Z2")
        time.sleep(random.randint(1, 5))

        mutex.acquire()
        _1 = 0
        _2 = 0
        Z1.release()
        Z2.release()
        mutex.release()

# Inicializamos los threads 
threading.Thread(target=coche, args=(1, 3,)).start()
threading.Thread(target=coche, args=(3, 1,)).start()
threading.Thread(target=coche, args=(4, 2,)).start()
threading.Thread(target=coche, args=(4, 2,)).start()
threading.Thread(target=coche, args=(2, 4,)).start()
threading.Thread(target=coche, args=(2, 4,)).start()
threading.Thread(target=coche, args=(1, 3,)).start()
threading.Thread(target=coche, args=(2, 4,)).start()
threading.Thread(target=coche, args=(4, 2,)).start()
threading.Thread(target=coche, args=(3, 1,)).start()
