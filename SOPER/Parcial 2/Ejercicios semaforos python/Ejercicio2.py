import threading
import time
import random

problemas = 0 # Número de problemas en la fábrica
elfos_en_espera = 0 # Elfos esperando en la oficina
renos_en_establo = 0 # Renos en el establo

oficina = threading.Semaphore(1) # Semáforo para la oficina
comprobar_problemas = threading.Semaphore(1) # Semáforo para comprobar problemas
elfos_esperando_a_santa = threading.Semaphore(0) # Semáforo para dejar a los elfos esperando
mutex = threading.Semaphore(0) # Semáforo para que santa duerma
establo = threading.Semaphore(1) # Semáforo para acceder al establo

def elfo():
    global problemas, elfos_en_espera
    while True:
        time.sleep(random.randint(1, 4))# Trabajando en la fábrica

        comprobar_problemas.acquire()
        oficina.acquire()
        if problemas >= 3 and elfos_en_espera < 3:
            elfos_en_espera+=1 # Elfo grita ¡Voy a la oficina!
            oficina.release()
            comprobar_problemas.release()

            print("Soy elfo, voy a la oficina. Problemas:", problemas)
            time.sleep(random.uniform(1, 2.5))

            # Comprobamos que este elfo sea el tercero
            oficina.acquire()
            if elfos_en_espera == 3:
                mutex.release() # Despertamos a santa
            oficina.release()

            # Elfos esperan a santa
            elfos_esperando_a_santa.acquire()

        else:
            oficina.release()
            comprobar_problemas.release()


def santa():
    global renos_en_establo, elfos_en_espera, problemas
    while True:
        mutex.acquire()

        # Comprobamos el establo
        establo.acquire()
        if renos_en_establo >= 9:
            renos_en_establo = 0
            print("Soy santa y voy a repartir regalos")
            time.sleep(random.randint(3, 6))
        establo.release()

        comprobar_problemas.acquire()
        if problemas >= 3:
            print("Soy santa, estoy solucionando los problemas")
            time.sleep(random.randint(1, 4))
            problemas = 0
        
        # Despertando a los 3 elfos
        for i in range(3):
            elfos_esperando_a_santa.release()
        elfos_en_espera = 0
        comprobar_problemas.release()



def renos():
    global renos_en_establo
    establo.acquire()
    renos_en_establo += 1
    print("Soy reno, renos en el establo:", renos_en_establo)
    if renos_en_establo == 9:
        mutex.release()
    establo.release()


# Inicializamos los threads 
threading.Thread(target=santa).start()

for i in range(5): # 5 elfos
    threading.Thread(target=elfo).start()

for i in range(50): # 50 renos
    threading.Thread(target=renos).start()
    problemas+=1
    time.sleep(1)