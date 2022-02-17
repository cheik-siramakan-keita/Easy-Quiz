import random
from Classe.CLASSE_Utilisateur import Utilisateur
from DAO.DAO_Utilisateur import DataAccessObjectUser

# def DemanderNomPass():
#     nom_saisi = input("quel est votre nom ?")
#     verif_doublon = DataAccessObjectUser().read(nom_saisi)
#     while len(verif_doublon) > 0:
#         nom_saisi = input("EXISTE DEJA!! quel est votre prenom ?")
#         verif_doublon = DataAccessObjectUser().read(nom_saisi)
#     pass_saisi = input("entrez un mot de passe (Pas Crypté donc mettre un truc simple) ?")
#     while len(pass_saisi) == 0:
#         pass_saisi = input("Aucun mot de passe a été saisie, Resaisir un mdp : ")
#     utilisateur = Utilisateur(0, nom_saisi, pass_saisi, '')
#     DataAccessObjectUser.create(utilisateur)
#     return utilisateur

def DemanderNom():
    nom_saisi = input("Choisissez un d'utilisateur")
    verif_doublon = DataAccessObjectUser().read(nom_saisi)
    if len(verif_doublon) > 0:
        print("Utilisateur choisi")
        utilisateur = Utilisateur(0, nom_saisi, '', '')
    else:
        utilisateur = Utilisateur(0, nom_saisi, '', '')
        DataAccessObjectUser.create(utilisateur)
    return utilisateur

Utilisateur = DemanderNom()

choix_jeux = int(input(f"Bienvenue !!!{Utilisateur.get_pseudo()}!!! quel jeu voulez vous jouer ? : "))
if choix_jeux == 1:
    print('question VF')
    list_utilisateur=[]
    donnees = DataAccessObjectUser().read()
    for nom in donnees:
        # print(nom.get_pseudo())
        list_utilisateur.append(nom.get_pseudo())
    print(list_utilisateur)
    print("après Random")

    liste_num=[]
    i = 0
    for i in range(0, len(donnees)):
        liste_num.append(i)
        i=i+1
    print(liste_num)

    liste_num_random = random.sample(liste_num, len(donnees))
    print(liste_num_random)

    index_random=0
    i_bin=1
#    for i in range(0, len(donnees)):
    for i in range(0,5):
        ordre=liste_num_random[index_random]
        print("*** Question " + str(i_bin) + " ***")
        print(str(list_utilisateur[ordre]))
        index_random=index_random+1
        i_bin = i_bin + 1


elif choix_jeux == 2:
    print('question True False')










#
# donnees = DataAccessObjectUser().read()
#
# for ligne in donnees:
#     print(ligne.to_string())
#     # if ligne.get_id() == 4:
#     #     DataAccessObjectUser.delete(ligne)
#
