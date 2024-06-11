while True:
    altura = float(input('Digite sua altura em cm: '))
    peso = int(input('Digite seu peso: '))
    # Convertendo altura de cm para metros

    altura_metros = altura / 100
    
    # Calculando o IMC
    imc = peso / (altura_metros * altura_metros)
    imc = int(imc)

    if imc < 18.5:
        categoria = 'Abaixo do peso'
    elif 18.5 <= imc < 24.9:
        categoria = 'Peso normal'
    elif 25 <= imc < 29.9:
        categoria = 'Sobrepeso'
    elif 30 <= imc < 34.9:
        categoria = 'Obesidade grau 1'
    elif 35 <= imc < 39.9:
        categoria = 'Obesidade grau 2'
    else:
        categoria = 'Obesidade grau 3'

    print(f'Seu IMC é de {imc:.2f} e você está na categoria: {categoria}')