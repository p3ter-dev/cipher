#include <stdio.h>  
#include <stdlib.h>  

#define KEYSIZE 16

void main() {
    long int initial_time, end_time = 1524092929;
    int i;

    for(initial_time = 1523995729; initial_time <= end_time; initial_time++) {  
        char key[KEYSIZE];
        srand(initial_time);
        for (i = 0; i< KEYSIZE; i++){
            key[i] = rand() % 256;
            printf("%.2x", (unsigned char)key[i]);
        }
        printf("\n");
    }
}
