
distancia = float(input("Distancia da Viagem:"))

if(distancia < 200):
    preco = (0.50 * distancia)
else:
    preco = (0.45 * distancia)
print(f"Preço da Passagem:{preco}")