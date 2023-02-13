#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    const int min = 0; 
    const int max = 10;
    int nbrtrouve = 5;
    int nbr = 0;
    int trouver = 0;
    int nbrcoup = 0;
    int fin = 0;

    while (fin == 0)
    {
    printf("Arreter taper 1 sinon 0");
    scanf("%d", &fin);
    printf("Deviner le chiffre \n");
    printf("Choisir chiffre : \n");
    scanf("%d", &nbr);
    while (nbr > max || nbr < min)
    {
        printf("Choisir chiffre : \n");
        scanf("%d", &nbr);
    }

    while (trouver == 0)
    {
        if(nbrcoup<=10)
        {
        if (nbr > nbrtrouve)
        {
            printf("Trop grand :");
            scanf("%d", &nbr);
            nbrcoup ++;
        }
        else if (nbr < nbrtrouve)
        {
            printf("Trop petit :");
            scanf("%d", &nbr);
            nbrcoup++;
        }
        else
        {
            printf("Trouvé");
            trouver = 1;
        }
        }
        else
        {
            printf("PERDU");
            break;
        }
        
    }  
    break;
    } 
    
    return 0;
}
