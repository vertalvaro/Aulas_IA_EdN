pares = 0
impares = 0

quant = int(input("Quantos números quer digitar? "))

for i in range(quant):
    num = int(input("Digite o número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)
