contagem = 0

for i in range(0, 20):
    num = int(input("digite um valor: \n"))
    if num % 2 == 0:
        contagem += 1
print("A quantidade de numeros pares digitada foi: ", contagem)