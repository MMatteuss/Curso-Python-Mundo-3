a = int(input("Digite o 1 numero: "))
b = int(input("Digite o 2 numero: "))
c = int(input("Digite o 3 numero: "))
d = int(input("Digite o 4 numero: "))

listaDeTupla = (a, b, c, d)
listaDeValoresParTupla = []
aparicaoNove = 0
posisaoTres = 0

for pos, numero in enumerate(listaDeTupla):
    if numero == 9:
        aparicaoNove=+1
    if numero == 3:
        posisaoTres = pos

for numero in listaDeTupla:
    if numero%2==0:
        listaDeValoresParTupla.append(numero)

print(" ")

print("Você Digitou os Valores",listaDeTupla)
print("O valor 9, apareceu", aparicaoNove, "Vezes")

if posisaoTres ==0:
    print("O valor 3, apareceu em nenhuma posição")    
else:
    print("O valor 3, apareceu na", posisaoTres+1, "ª posição")

print("Os valores pares diigtados foram", listaDeValoresParTupla)