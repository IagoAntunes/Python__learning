
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preçocom 5% de desconto

produto = float(input("Preço do Produto:"))

desconto = (produto * 5)/100
print(f"Desconto: R$ {desconto} \nValor Produto: R$ {produto - desconto}")