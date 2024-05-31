while True:
    numero1 = input('Digite um numero: ')
    sinal = input('Digite um sinal de +, -, * ou /: ')
    numero2 = input('Digite outro numero: ')
    
    numero1 = int(numero1)
    numero2 = int(numero2)

    if sinal == '+':
        print(numero1 + numero2)
    elif sinal == '-':
        print(numero1 - numero2)
    elif sinal == '*':
        print(numero1 * numero2)
    elif sinal == '/':
        if numero2 != 0:
            print(numero1 // numero2)
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Sinal inválido. Tente novamente.")

        
