# Thème 1 : Exercices numériques simples
# EXO 1

# QUESTION 1.1
# Définition de la fonction pour la question 1 : moyenne de 3 nombres
def moyenne_3_nb(a, b, c):
    return (a + b + c) / 3

# Tests pour la fonction moyenne_3_nb
tests_moyenne_3 = [
    (3, 6, -3),
    (-3, 0, 3),
    (1.5, 2.5, 1.0)
]

# Calcul des moyennes
resultats_moyenne_3 = [moyenne_3_nb(*test) for test in tests_moyenne_3]

# Affichage des résultats
print("Résultats des moyennes simples (3 nombres) :", resultats_moyenne_3)

# Définition de la fonction pour la moyenne de 4 nombres
def moyenne_quatre_nb(a, b, c, d):
    return (a + b + c + d) / 4

# Tests pour la fonction moyenne_quatre_nb
tests_moyenne_4 = [
    (3, 6, -3, 1),
    (-3, 0, 3, 1),
    (1.5, 2.5, 1.0, 1.0),
]

# Calcul des moyennes
resultats_moyenne_4 = [moyenne_quatre_nb(*test) for test in tests_moyenne_4]

# Affichage des résultats
print("Résultats des moyennes simples (4 nombres) :", resultats_moyenne_4)