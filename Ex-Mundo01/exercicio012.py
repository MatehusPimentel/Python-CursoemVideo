preco = float(input('Informe o preço do produto R$'))

novo = preco - (preco * 5 / 100)

print('O produto que custava R${:.2f} na promoção de 5% vai custar R${:.2f}'.format(preco, novo))