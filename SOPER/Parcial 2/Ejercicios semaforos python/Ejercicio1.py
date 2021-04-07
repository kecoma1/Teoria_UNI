import threading
import time

NUM_NINOS = 5

# Mutex para la sección crítica
mutex = threading.Semaphore(1)

# Semáforos para cada niño
nino_sem = []
for i in range(NUM_NINOS):
    nino_sem.append(threading.Semaphore(1))

cuenta = 0 # Variable global para contar cuantos han comido

def nino_p_t(n):
    global cuenta
    for i in range(3):
        # Niño va a pedir comida, para que pida solo una vez bajamos su semáforo
        nino_sem[n].acquire()

        # Si todos los niños no han pedido comida comemos
        if cuenta < NUM_NINOS:

            # Entramos en la sección crítica
            mutex.acquire()

            # Come
            print("soy "+str(n)+", estoy comiendo")
            cuenta+=1
            if cuenta == NUM_NINOS:
                # Si todos han comido, sacamos otra tarta
                cuenta = 0

                # Les decimos a todos los niños que pueden comer
                for k in range(NUM_NINOS):
                    nino_sem[k].release()
                time.sleep(2) # Sleep para hacer visible la ejecución
            mutex.release()

# Inicializamos los threads 
for i in range(NUM_NINOS):
    t1 = threading.Thread(target=nino_p_t, args=(i,)).start()