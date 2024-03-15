print("Bem vindo a Calculadora de IMC!")
print("Por favor, insira o valor do seu peso (em kg):")
peso = float(input())
print("Por favor, insira o valor da sua altura (em m):")
altura = float(input())
imc = peso / (altura * altura)

if(imc < 18.5):
    print("Seu IMC é:", imc, "e você esta abaixo do peso.")
elif(imc >= 18.5 and imc < 24.9):
    print("Seu IMC é:", imc, "e você esta no peso ideal.")
elif(imc >= 24.9 and imc < 29.9):
    print("Seu IMC é:", imc, "e você esta com sobrepeso.")
elif(imc >= 29.9 and imc < 34.9):
    print("Seu IMC é:", imc, "e você esta com obesidade grau I.")
elif(imc >= 34.9 and imc < 39.9):
    print("Seu IMC é:", imc, "e você esta com obesidade grau II.")
elif(imc >= 40):
    print("Seu IMC é:", imc, "e você esta com obesidade grau III.")

