from datetime import datetime

nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
data_nasc = datetime.strptime(nascimento, "%d/%m/%Y")
hoje = datetime.now()
dias_vivo = (hoje - data_nasc).days

print("Você está vivo há", dias_vivo, "dias.")
