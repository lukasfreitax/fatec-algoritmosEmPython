#Somatória
#Escreva um algoritmo que calcule a soma dos números de 1 a 15.

#declara se a variavel soma como inicial 0, para ser utilizada no looping
soma = 0
for num in range(1,16):
    soma += num
    #o print abaixo vai mostrar em cada linha o valor da iteração
    print(soma)
#o print vai mostrar fora do looping, o valor final da somatória
print(f'A somatória de 1 a 15 é igual a {soma}')