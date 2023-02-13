#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int salaire1=0;
    int salaire2=0;
    int salaireintput=0;
    int i=0;
    for(i = 0; i < 70; i++)
    {
        printf("%dème salaire",&i);
        scanf("Ecrire salaire : %d",&salaireintput);
        if (salaireintput <= 1000)
        {
            salaire1++;
        }
        else
        {
            salaire2++;
        }
        printf("%d salaire 1 ; %d salaire 2",&salaire1,&salaire2);
    }   
    return 0;
}
