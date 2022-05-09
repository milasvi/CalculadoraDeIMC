#condicional aninhada
print('Bem-vinde à Calculadora de IMC para Adultos! (20 a 60 anos')
#Menor que 18.5 - Abaixo do peso ;
#Entre 18.5 e 24.9 - Peso normal ;
# Entre 25.0 e 29.9 - Pré-obesidade ;
# Entre 30.0 e 40 - Obesidade 
while True:
    altura = float(input('Qual sua altura?'))
    peso = float(input('Qual seu peso?'))
    imc = peso / (altura ** 2)

    print(f'Seu IMC é {imc:,.1f}.')

    if imc < 18.6:
        print('Seu IMC está abaixo do normal, procure um(a) médico(a)!')
    elif imc == 18.5 or imc < 24.9 or imc == 24.9:
        print('Seu IMC está normal, mas procure um médico para fazer um checkup mesmo assim.')
    elif imc > 25 or imc == 25 or imc < 29.9 or imc == 29.9:
        print('Seu IMC está sobrepeso, procure um(a) médico(a) para fazer um checkup!)')
    else:
        print('Seu IMC é obesidade, procure um(a) médico(a) para fazer um checkup.')
    resposta = input('Deseja informar outro IMC? [s/n]')
    if resposta == 'n':
        print('Obrigade por usar a Calculadora de IMC. \nAté mais!')
        break
        