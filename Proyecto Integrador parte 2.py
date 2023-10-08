from readchar import readkey,key
input_str = ""
while True:
    leido = readkey()
    print("leer la tecla", leido)
    (input_str) += leido
    if leido == key.UP:
     break