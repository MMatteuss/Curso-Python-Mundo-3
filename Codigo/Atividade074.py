import random

a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)
d = random.randint(1, 10)
e = random.randint(1, 10)

listaAleatoria = (a, b, c, d, e)
listaDoMaiorNumero = sorted(listaAleatoria)

print("O valor da lista aleatoria é: ",listaAleatoria)
print("O maior numero da lista: ",listaDoMaiorNumero[-1])
print("O menor numero da lista: ",listaDoMaiorNumero[0])