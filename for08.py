#PRODUTÓRIO
#faça um programa que leia do usuário um número e calcule o produtório de 1 até esse número

num = int(input('Digite um número: '))

product = 1
for i in range (1,num+1):
    product *= i
    #print mostrando cada iteração e o valor multiplicado no final de cada iterada
    print(i, product)

print(f'O valor do produtório de 1 a {num} é de {product}')