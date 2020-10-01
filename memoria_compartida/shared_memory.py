from multiprocessing.managers import SharedMemoryManager
from multiprocessing.shared_memory import ShareableList
from multiprocessing import Process
import multiprocessing


# Instanciamos un gestor de bloques memoria compartida
smm = SharedMemoryManager()

# iniciamos el proceso
smm.start()

# Creamos una lista compartida con strings
lc = smm.ShareableList(["hola","BlaBlaBlaBla","BlaBlaBlaBLa"])

#Imprimimos la lista para ver su estado actual
print('Este es el estado inicial de la lista: \n' + str(lc))

#Creamos la funcion que realizaran los procesos que consumiran la memoria compartida
#Estas funciones son creadas para cada proceso, cambian un string de la lista y la imprimen
def workerProceso1():
    #Obtenemos la lista por su nombre
    a = ShareableList(name= lc.shm.name)
    #Agregamos a la lista un string
    a[1] = "Proceso 1"
    print('\n hola soy el proceso 1 \n' + 'Imprimiendo la lista compartida \n' + str(a))

def workerProceso2():
    #Obtenemos la lista por su nombre
    b = ShareableList(name= lc.shm.name)
    #Agregamos a la lista un string
    b[2] = "Proceso 2"
    print('\n hola soy el proceso 2 \n' + 'Imprimiendo la lista compartida: \n' + str(b))


#Definimos los procesos
p1 = Process(target=workerProceso1)
p2 = Process(target= workerProceso2)

p1.start()
p2.start()
p1.join()
p2.join()

#Imprimimos la lista para ver si los cambios han sido efectivamente aplicados.

print('\n Imprimiendo la lista para ver si se efectuaron los cambios: \n' + str(lc))

#Damos de baja el gestor de bloques de memoria compartida
smm.shutdown()

