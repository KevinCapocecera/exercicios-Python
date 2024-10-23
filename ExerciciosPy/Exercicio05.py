#5) Escreva um algoritmo que leia 10 números do usuário e calcule a soma desses números.

lista_soma = []

for i in range(0, 10):
    lista_soma.append(int(input("Digite o numero que voce deseja somar: \n")))
print("a soma dos numeros e: " + str(sum(lista_soma)))




