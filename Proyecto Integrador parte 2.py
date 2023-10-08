from readchar import readkey,key
input_str = ""
while True:
    leido = readkey()
    (input_str) += leido
    if leido == key.UP:
        break


