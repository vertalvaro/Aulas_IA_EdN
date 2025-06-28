valor = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C/F/K): ").upper()
destino = input("Digite a unidade de destino (C/F/K): ").upper()

if origem == "C" and destino == "F":
    resultado = (valor * 9/5) + 32
elif origem == "C" and destino == "K":
    resultado = valor + 273.15
elif origem == "F" and destino == "C":
    resultado = (valor - 32) * 5/9
elif origem == "F" and destino == "K":
    resultado = (valor - 32) * 5/9 + 273.15
elif origem == "K" and destino == "C":
    resultado = valor - 273.15
elif origem == "K" and destino == "F":
    resultado = (valor - 273.15) * 9/5 + 32
else:
    resultado = valor

print("Temperatura convertida:", round(resultado, 2), destino)
