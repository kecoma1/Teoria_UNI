import threading
import time
import random

# Carteles 0 libre, >0 hombre, <0 mujer
A = 0
B = 0

# Mutex para la sección crítica
mutex = threading.Semaphore(1)

# Semáforos para los baños
room_A = threading.Semaphore(10)
room_B = threading.Semaphore(10)

def hombre():
    global A, B
    while True:
        mutex.acquire()
        if A >= 0 and A < 10:
            # Entrando al baño
            A += 1
            mutex.release()
            room_A.acquire()

            print('Hombre meando en A,', A, 'personas dentro')
            time.sleep(random.randint(1, 5))

            mutex.acquire()
            A -= 1
            room_A.release()
            mutex.release()
        elif B >= 0 and B < 10:
            B += 1
            mutex.release()
            room_B.acquire()

            print('Hombre meando en B,', B, 'personas dentro')
            time.sleep(random.randint(1, 5))

            mutex.acquire()
            B -= 1
            room_B.release()
            mutex.release()
        else:
            mutex.release()
        time.sleep(50)

def mujer():
    global A, B
    while True:
        mutex.acquire()
        if A <= 0 and A > -10:
            # Entrando al baño
            A -= 1
            mutex.release()
            room_A.acquire()

            print('Mujer meando en A,', A*-1, 'personas dentro')
            time.sleep(random.randint(1, 20))

            mutex.acquire()
            A += 1
            room_A.release()
            mutex.release()
        elif B <= 0 and B > -10:
            B -= 1
            mutex.release()
            room_B.acquire()

            print('Mujer meando en B,', B*-1, 'personas dentro')
            time.sleep(random.randint(1, 20))

            mutex.acquire()
            B += 1
            room_B.release()
            mutex.release()
        else:
            mutex.release()
        time.sleep(50)
        

# Inicializamos los threads 
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=mujer).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=hombre).start()
time.sleep(random.uniform(0.1, 5))