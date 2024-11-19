# Fonction pour générer le calendrier
def generer_calendrier(nombre_jours, jour_debut):
    jours_semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

    print("Calendrier:")
    for jour in jours_semaine:
        print(f"{jour[:3]}", end='\t')
    print()

    # Espaces avant le premier jour du mois
    for _ in range(jour_debut - 1):
        print("\t", end='')

    # Afficher les jours du mois
    jour_actuel = 1
    for _ in range(jour_debut - 1, 7):
        if jour_actuel <= nombre_jours:
            print(f"{jour_actuel}", end='\t')
            jour_actuel += 1
        else:
            break
    print()

    # Afficher les jours restants
    while jour_actuel <= nombre_jours:
        for _ in range(7):
            if jour_actuel <= nombre_jours:
                print(f"{jour_actuel}", end='\t')
                jour_actuel += 1
            else:
                break
        print()


# Exemple d'utilisation
nombre_jours = int(input("Entrez le nombre de jours dans le mois: "))
jour_debut = int(input("Entrez le numéro du jour démarrant le mois (1 pour Lundi, ..., 7 pour Dimanche): "))

generer_calendrier(nombre_jours, jour_debut)
