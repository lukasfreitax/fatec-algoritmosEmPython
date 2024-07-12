numero = int(input('Digite um número de 0 a 10:'))

for num in range(0,11):
    #o laço de repetição irá de 0 a 10
    #vamos declarar uma variável tabuada que é igual ao número digitado pelo usuário,
    #e ele será multiplicado no looping de 0 a 10
    tabuada = num * numero
    #o print formatado irá mostrar o número solicitado * o tanto de repetições (de 0 a 10),
    #que resultará na tabuada do número informato pelo usuario
    print(f'{numero} x {num} = {tabuada}')