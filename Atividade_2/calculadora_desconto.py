produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20

valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto

print("Produto:", produto)
print("Preço original: R$", round(preco_original, 2))
print("Desconto: R$", round(valor_desconto, 2))
print("Preço com desconto: R$", round(preco_final, 2))
