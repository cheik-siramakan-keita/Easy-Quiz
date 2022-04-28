import random
from Classe.CLASSE_Utilisateur import Utilisateur
from DAO.DAO_Utilisateur import DataAccessObjectUser

from Classe.CLASSE_Type import Type
from Classe.CLASSE_Quiz import Quiz
from DAO.DAO_Type import DataAccessObjectType
from DAO.DAO_Quiz import DataAccessObjectQuiz
from Repository.REPOSITORY_Quiz import RepositoryQuiz

#utilisateur=Utilisateur(0, 'Test2', 'Test2', '')
#DataAccessObjectUser.create(utilisateur)
#donnees = DataAccessObjectUser().read('Test2')
#print(len(donnees))
#for ligne in donnees:
    #DataAccessObjectUser.delete(ligne)
#    print(ligne.to_string())

# -- Gestion des quiz --

# On récupère un type de quiz.
#type=DataAccessObjectType().read(1)[0]

# Création d'une instance de la classe Quiz.
quiz = Quiz(0, type, "La Tour Eiffel a été construite en l'an ____ à Paris.", '1887', '')
quiz = Quiz(0, type, "____ est le premier président de la république française.", 'Louis-Napoléon Bonaparte', '')
quiz = Quiz(0, type, "Wolfgang Amadeus Mozart est né le 27 janvier ____.", '1756', '')
quiz = Quiz(0, type, "____ est le dernier roi de France.", 'Louis-Philippe', '')
quiz = Quiz(0, type, "L'Empereur Napoléon I a perdu la bataille de Waterloo en l'an ____.", '1815', '')
quiz = Quiz(0, type, "La première guerre mondiale a commencé le 28 juillet ____.", '1914', '')
quiz = Quiz(0, type, "La seconde guerre mondiale a commencé le 1 spetembre ____.", '1939', '')
quiz = Quiz(0, type, "La Tour Eiffel a été construite en ____ à Paris.", '1887', '')
quiz = Quiz(0, type, "La Tour Eiffel a été construite en ____ à Paris.", '1887', '')
quiz = Quiz(0, type, "La Tour Eiffel a été construite en ____ à Paris.", '1887', '')


# Insertion de l'instance créé avant dans la base de données
# via la méthode create de la classe DAO_Quiz en donnant l'instance
# pour paramètre de la méthode.
#donnees_1 = DataAccessObjectQuiz().create(quiz)

# Lecture de la base de données, on récupère toute les lignes
# qui sont dans la table 'quiz' via la méthode read de la
# classe DAO en ne passant aucun paramètre.
#donnees_2 = DataAccessObjectQuiz().read()
#donnees_2 = RepositoryQuiz.recuperer()

# On affiche le nombre d'élément dans la liste retournée par la
# méthode read de la classe DAO.
#print(len(donnees_2))

# On parcours la liste récupéré auparavant pour afficher son contenu.
#for ligne in donnees_2:
#    print(ligne.to_string())
    #DataAccessObjectQuiz.delete(ligne)


# -- Gestion des types de quiz --

# Création d'une instance de la classe Type.
#type=Type(0, 'Test #1', '')

# Insertion de l'instance créé avant dans la base de données
# via la méthode create de la classe DAO_Type en donnant l'instance
# pour paramètre de la méthode.
#donnees_1 = DataAccessObjectType().create(type)

# Lecture de la base de données, on récupère toute les lignes
# qui sont dans la table 'type_quiz' via la méthode read de la
# classe DAO en ne passant aucun paramètre.
#donnees_2 = DataAccessObjectType().read()

# On affiche le nombre d'élément dans la liste retournée par la
# méthode read de la classe DAO.
#print(len(donnees_2))

# On parcours la liste récupéré auparavant pour afficher son contenu.
#for ligne in donnees_2:
#    print(ligne.to_string())

print('=======================================')
choix=int(input('Veuillez choisir un type de quiz: \n1. Questions à Trou \n2. Questions Vrai ou Faux \n'
            '3. Questions customisé\n'))

if choix == 1:
    print(choix)
    donnees_2 = RepositoryQuiz.recuperer(choix)

    for e in donnees_2:
        print(e.to_string())
elif choix == 2:
    print(choix)
    donnees_2 = RepositoryQuiz.recuperer(choix)

    for e in donnees_2:
        print(e.to_string())
elif choix ==3:
    print(choix)
    donnees_2 = RepositoryQuiz.recuperer(choix)

    for e in donnees_2:
        print(e.to_string())