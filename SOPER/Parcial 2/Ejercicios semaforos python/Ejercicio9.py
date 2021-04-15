import threading
import time
import random

coches_esperando = 0
peatones_esperando = 0
quien_cruza = None

esperar = threading.Semaphore(0)
mutex = threading.Semaphore(1)

def peaton():
    global coches_esperando, peatones_esperando, quien_cruza

    # Llego a la acera

    # Miro al cruzar, si hay coches cruzando no cruzo
    # Si hay 10 o más coches espero
    mutex.acquire()
    if quien_cruza == 'peaton':
        if coches_esperando >= 10: # Hay 10 coches esperando
            peatones_esperando += 1
            quien_cruza = 'coche'
            print("Peatones esperando ", peatones_esperando)
            mutex.release()

            esperar.acquire()
            print('PEATON: Cruzo')
            time.sleep(5)
        else: # No hay 10 coches esperando
            print('PEATON: Cruzo')
            mutex.release()
    elif quien_cruza == 'coche':
        peatones_esperando += 1
        print("Peatones esperando ", peatones_esperando)
        mutex.release()

        esperar.acquire()
        print('PEATON: Cruzo')
    else:
        quien_cruza = 'peaton'
        print('PEATON: Cruzo')
        mutex.release()


def coche():
    global cola

    # LLego

    # Hay peatones
    mutex.acquire()
    if quien_cruza == 'coche':
        if peatones_esperando > 0:
            





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