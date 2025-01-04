produtosLista = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Trasferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Caneta", 22.30, "Livro", 34.90)

print("----------------------------------------")
print("             LISTA DE PREÇOS            ")
print("----------------------------------------")

for i in range(0, len(produtosLista), 2):
    produto = produtosLista[i]       # Nome do produto
    preco = produtosLista[i + 1]     # Preço do produto
    print(f"{produto:<20} R$ {preco:>7.2f}")
    
print("----------------------------------------")