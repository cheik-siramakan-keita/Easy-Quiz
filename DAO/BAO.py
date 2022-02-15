from BAO.Connexion_BDD import BaseDeDonnee

def ajouter_clause(requete, options: dict):
    i = 0
    cle: dict
    operateur: list
    valeur: str
    liste_cles = options.keys()

    if options is not None:
        requete = requete + ' WHERE '

        for cle in liste_cles:
            if cle in options:
                if cle != 'opérateur':
                    valeur = str(options.get(cle))

                    if valeur.isnumeric() == False:
                        valeur = '\'' + valeur + '\''
                    else:
                        valeur = valeur

                    requete = requete + str(cle) + '=' + valeur + ' '

                    if 'opérateur' in options and len(options.get('opérateur')) > 0:
                        operateur = options.get('opérateur')[0]
                        requete = requete + operateur + ' '
                        options.get('opérateur').pop(0)
    return requete


def creer_requete_select(champs, table):
    i = 1
    requete = "SELECT "

    for champ in champs:
        requete = requete + champ

        if i < len(champs):
            requete = requete + ', '
            i = i + 1

    requete = requete + " FROM " + table
    return requete

def recuperer_champs(nom_table):
    connexion = BDD.connecter()

    requete = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{nom_table}'"
    resultat = connexion.execute(requete)
    resultat = [r for r, in resultat]

    return resultat


def recuperer_donnees(champs, donnees):
    existe = False
    donnee = {}
    liste_donnees = []

    for ligne in donnees:
        for champ in champs:
            donnee.update({champ: ligne[champ]})
        liste_donnees.append(donnee)
    return liste_donnees