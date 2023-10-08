#Se inicia colocando las dos acciones que vamos a utilizar

from readchar import readkey,key 
input_str = ""
while True:
    leido = readkey() # Se 
    print("leer tecla", leido)
    (input_str) += leido
    if leido == key.UP: # acá le das la instrucción de que al precionar la tecla arriba que es lo que va realizar
     break