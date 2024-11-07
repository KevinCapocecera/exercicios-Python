num = [2, 2, 3, 5, 8, 8, 9, 10, 11, 11]
contador = 0

for elemento in num:
    for verificacao in num:
        if elemento == verificacao:
         contador+=1
    if contador >= 2:
        print("os numeros repetidos são: ",elemento)
    contador = 0
