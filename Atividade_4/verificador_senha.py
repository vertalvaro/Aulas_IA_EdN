senha = input("Digite a senha: ")

tem_numero = False
for c in senha:
    if c.isdigit():
        tem_numero = True

if len(senha) >= 8 and tem_numero:
    print("Senha válida")
else:
    print("Senha inválida")
