import threading
import time
import random

cola = 0

museo = threading.Semaphore(100)
cola_sem = threading.Semaphore(0)
mutex = threading.Semaphore(1)

def turista():
    global cola

    # Entro al museo
    museo.acquire()

    # Me meto en la cola de la basilica
    mutex.acquire()
    print("Voy a la basílica")
    cola += 1
    mutex.release()
    cola_sem.acquire()
    
    print("Salgo de la basílica")
    museo.release()


def guia():
    global cola
    i = 0
    trabajar = None
    while i < 30:
        trabajar = False

        # Comprobamos cuanta gente hay en la cola
        mutex.acquire()
        if cola >= 10:
            cola -= 10
            # Sacamos a 10 personas de la cola
            cola_sem.release()
            cola_sem.release()
            cola_sem.release()
            cola_sem.release()
            cola_sem.release()
            cola_sem.release()
            cola_sem.release()
            cola_sem.release()
            cola_sem.release()
            cola_sem.release()
            trabajar = True
            print("Soy guía, voy a trabajar, gente en la cola: ", cola)
        mutex.release()

        if trabajar == True:
            time.sleep(20)
        i+=1
        time.sleep(1)

# Inicializamos los threads 
threading.Thread(target=guia).start()
threading.Thread(target=guia).start()
threading.Thread(target=guia).start()
threading.Thread(target=guia).start()
threading.Thread(target=guia).start()
time.sleep(random.uniform(0.1, 2))

for n in range(500):
    threading.Thread(target=turista).start()
    time.sleep(random.uniform(0.1, 2))