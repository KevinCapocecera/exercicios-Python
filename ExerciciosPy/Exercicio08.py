contagem = 0

for i in range (0, 5):
    idade = int(input("Digite sua idade: \n"))
    if idade >= 18:
        contagem += 1
print("A quantidade de pessoas maiores de idade é: ",contagem)