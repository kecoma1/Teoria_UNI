import threading
import time
import random

dentro = 0
barca_a_elegir = 'A'

mutex = threading.Semaphore(1)

barca_A = threading.Semaphore(4)
barca_B = threading.Semaphore(4)

def automovil():
    global barca_a_elegir, dentro
    
    # Consultar
    mutex.acquire()
    if (dentro < 4):
        if (barca_a_elegir == 'A'):
            dentro += 1
            barca_A.acquire()
            print("Entro en A")
        else:
            dentro += 1
            barca_B.acquire()
            print("Entro en B")
    mutex.release()


def barcaza():
    global barca_a_elegir, dentro
    i = 0
    while i < 30:
        mutex.acquire()
        if dentro == 4:
            dentro = 0
            if barca_a_elegir == 'A':
                print("A lleno, redirigimos a B")
                barca_a_elegir = 'B'
                barca_A.release()
                barca_A.release()
                barca_A.release()
                barca_A.release()
            else:
                print("B lleno, redirigimos a A")
                barca_B.release()
                barca_B.release()
                barca_B.release()
                barca_B.release()
                barca_a_elegir = 'A'
        mutex.release()
        i+=1
        time.sleep(1)

# Inicializamos los threads 
threading.Thread(target=barcaza).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))
threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

threading.Thread(target=automovil).start()
time.sleep(random.uniform(0.1, 2))

