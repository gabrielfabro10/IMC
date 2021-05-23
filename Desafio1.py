import os

altura = float(input("Digite sua altura em metros(ex: 1.85): "))
peso = float(input("Digite seu peso em kg(ex: 85.5): "))

imc = peso / altura**2

print("Seu IMC é: %.4f" % imc)

if imc < 16:
    print("Subpeso severo")
elif (imc >= 16 and imc <= 19.9):
    print("Subpeso")
elif (imc >= 20 and imc <= 24.9):
    print("Normal")
elif (imc >= 25 and imc <= 29.9):
    print("Sobrepeso")
elif (imc >= 30 and imc <= 39.9):
    print("Obeso")
elif imc > 40:
    print("Obeso Mórbido")
else:
    print("IMC não encontrado")

os.system("pause")
