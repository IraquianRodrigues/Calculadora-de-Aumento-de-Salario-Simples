#Autor: Iraquian Rodrigues
#Aumento Salarial

print('*'*20)
print('AUMENTO DE SALARIO')
print('*'*20)
print()

print('Dados do Colaborador')

nome= input('digite o seu nome: ')
idade = int(input('digite a sua idade: '))
salario = float(input('digite o seu salario atual: '))

sal15 = salario * 0.15
sal20 = salario * 0.20
sal25 = salario * 0.25

resultado = salario + sal15 or sal20 or sal25

if salario <= 280:
    print('conceber aumento de 15%')

elif salario > 280 and salario <= 700:
    print('Conceber Aumento de 20%')

elif salario > 700 and salario <= 1500:
    print('Conceber aumento de 20%')

print('Calculando Aumento...Por favor Aguarde!')

import time
import sys
#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.6)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print()
print()



print(F'Sr.{nome}, Seu aumento salarial foi de {resultado:.2f}')
