#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int choix = 0;
    printf("MENU\n");
    printf("--------\n");
    printf("1.BIC MAC\n");
    printf("2.FISH\n");
    printf("3.CHEESE\n");
    printf("--------\n");
    printf("VOTRE CHOIX ? :");
    scanf("%d",&choix);
    if (choix == 1)
    {
        printf("Votre choix est BIC MAC !!!");
    }
    else if (choix == 2)
    {
        printf("Votre choix est FISH !!!");
    }
    else if (choix == 3)
    {
        printf("Votre choix est CHEESE !!!");
    }
    else
    {
        printf("NOUS AVONS PAS COMPRIS VOTRE COMMANDE !\n");
        printf("Taper votre choix (1,2,3)");
    }
    while (choix != 1 || choix != 2 || choix != 3)
    {
        printf("NOUS AVONS PAS COMPRIS VOTRE COMMANDE !\n");
        printf("Taper votre choix (1,2,3) :");
        scanf("%d",choix);
    }
    while (choix != 1 || choix != 2 || choix != 3)
    {
        printf("NOUS AVONS PAS COMPRIS VOTRE COMMANDE !\n");
        printf("Taper votre choix (1,2,3) :");
        scanf("%d",choix);
    }
    
    return 0;
}