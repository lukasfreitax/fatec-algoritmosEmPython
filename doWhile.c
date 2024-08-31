#include <stdio.h>

int main(){
    int contador = 0;

    do {
        printf("%d", contador);
        contador+= 2;
    } while (contador <= 10);

    return 0;
}
