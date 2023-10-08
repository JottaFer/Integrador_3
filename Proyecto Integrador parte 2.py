#Se inicia colocando las dos acciones que vamos a utilizar

from readchar import readkey,key 
input_str = ""
while True:
    leido = readkey() # Se nombra la variable con la accion (en este caso, "presionar una tecla en especifico del teclado")
    print("leer tecla", leido)
    (input_str) += leido
    if leido == key.UP: # Despues de haber dado la tarea a realizar, se le indica qué tecla se debe presionar para finalizar
     break