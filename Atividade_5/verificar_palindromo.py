def eh_palindromo(texto):
    texto = ''.join(c for c in texto.lower() if c.isalnum())
    return texto == texto[::-1]

frase = input("Digite uma palavra ou frase: ")
if eh_palindromo(frase):
    print("Sim")
else:
    print("Não")
