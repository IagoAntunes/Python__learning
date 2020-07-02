
#Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto -à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal -3x ou mais no cartão: 20% de juros

produto = float(input("Valor do Produto:"))
opcao = int(input("""[1]A vista/CHEQUE \n[2]A vista/CARTAO 
[3]2x/CARTAO \n[4]3x+/CARTAO\n"""))

if(opcao == 1):
    total = produto - (produto * 10)/100
elif(opcao == 2):
    total = produto - (produto * 5)/100
elif(opcao == 3):
    total  = produto
elif(opcao == 4):
    juros = (produto * 20)/100
    parcela = int(input("Numero de Parcelas:"))
    vparcela = produto / parcela
    print(f"\nJuros:R${juros}   Valor das Parcelas:R${vparcela}")
    total = produto + juros
else:
    print("OPCAO INVALIDADE")
print(f"Valor Total:R${total}")