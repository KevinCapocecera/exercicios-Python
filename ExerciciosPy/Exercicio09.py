nome = ""
idade = 0
idade_min = 999999999
nome_mais_novo = ""

for i in range (0, 3):
    nome = str(input("Digite seu nome: \n"))
    idade = int(input("Digite sua idade: \n"))
    if idade < idade_min:
        idade_min = idade
        nome_mais_novo = nome
print("O nome do mais novo é: " + nome_mais_novo)