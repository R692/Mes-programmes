# On import un module math ce module contient des graphes mathematiques
import matplotlib.pyplot as plt
# Ici on cree la fonction qui prend en parametre x et y (nos listes)
def regresion(x, y):
    # On prend en compte le nombre d'elements de nos listes
    if len(x) == len(y):

        # On calcule la moyenne de nos listes
        moy_x = sum(x) / len(x)
        moy_y = sum(y) / len(y)
        # On affiche les moyennes
        print("Moyenne x :", round(moy_x,5), "\nMoyenne y :", round(moy_y,5))
        # On calcule les xi - moyenne et yi - moyenne
        cov_x = []
        cov_y = []
        for i in x:
            i = round(i - moy_x, 3)
            cov_x.append(i)
        print("xi - moyenne de x : ", cov_x)
        for i in y:
            i = round(i - moy_y, 3)
            cov_y.append(i)
        print("yi - moyenne de y : ", cov_y)
        # On calcule la covariance
        # On boucle sur le nombre d'élèments de nos listes
        cov_xy = []
        for i in range(len(x)):
            cov_xy.append(round(cov_x[i] * cov_y[i], 3))
        print("Somme des produits des covariance x et y : ", cov_xy)
        somme_cov = round((1 / len(x)) * sum(cov_xy), 3)
        print("Covariance(X,Y) : ", somme_cov)
        # La variance de x
        # On boncle sur les elements de x
        var_x = []
        for i in x:
            i = round((i - moy_x) ** 2, 3)
            var_x.append(i)
        somme_var_x = (1 / len(x)) * sum(var_x)
        print("Variance x² : ", round(somme_var_x,5))

        # On calcul nos coefficients de regression
        coef_a = round(somme_cov / somme_var_x, 2)
        print("Coefficient alpha : ", coef_a)
        coef_b = round(moy_y - coef_a * moy_x, 2)
        print("Coefficient beta : ", coef_b)
        print("Droite de regresion : ",coef_a,"X + ",coef_b)
        # On cacul la droite de regression avec nos coefficients de regression
        # On boucle sur les elements de nos listes
        prediction = []
        for i in x:
            prediction.append(round(coef_a * i + coef_b, 2))
        print("Valeur prédite :", prediction)
        # On calcul la somme des erreurs
        residu = []
        for i in range(len(y)):
            residu.append(round(y[i] - prediction[i], 2))
        print("Résidu : ", residu)
        # Somme des résidu au carré
        residu_carre = []
        for i in range(len(y)):
            residu_carre.append(round(pow(residu[i],2),2))
        print("Résidu au carré : ", residu_carre)
        print("Somme des résidu : ", sum(residu_carre))
        print("Variance estimée : ", round((1/(len(y)-2)) * sum(residu_carre),2))
        scr = []
        for i in range(len(prediction)):
            scr.append(round((y[i] - prediction[i]) ** 2, 4))
        # Calcul du SCT
        sct = []
        for i in range(len(y)):
            sct.append(round((y[i] - moy_y) ** 2, 4))
        coef_det = round(1 - (sum(scr) / sum(sct)), 2)
        print("Coefficient de détermination non-ajusté R² : ", coef_det)

        # ax1 = plt.subplot(2, 1, 1)
        # ax2 = plt.subplot(2, 1, 2)

        # ax1.scatter(x, y, marker=".", c="black")
        # ax1.scatter(x, prediction, marker=".", c="red")
        # ax1.errorbar(x, y, residu, fmt="none")
        # ax2.scatter(x, residu)

        # On affiche le graphe
        plt.scatter(x, y, marker=".", c="black")
        plt.scatter(x, prediction, marker=".", c="red")
        plt.errorbar(x, y, residu, fmt="none")
        plt.plot(x, prediction, linewidth=1, color="blue")
        plt.show()
    else:
        print("Erreur le nombre d'éléments des listes est différents")