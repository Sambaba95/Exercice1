import random

ivoryCostRegions = {
    "district autonome d'abidjan": "Abidjan",
    "district autonome yamoussoukro": "Yamoussoukro",
    "belier": "Toumodi",
    "ifou": "Daoukro",
    "n'zi": "Dimbokro",
    "sud comoe": "Aboisso",
    "indénie djuablin": "Abengourou",
    "agneby tiassa": "Agboville",
    "la me": "Adzopé",
    "grands ponts": "Dabou",
    "san pedro": "San-pédro",
    "gbokle": "Sassandra",
    "nawa": "Soubré",
    "gontougo": "Bondoukou",
    "bounkani": "Bouna",
    "hambol": "Katiola",
    "gbékê": "Bouaké",
    "worodougou": "Séguéla",
    "bere": "Mankono",
    "bafing": "Touba",
    "tonkpi": "Man",
    "guemon": "Duékoué",
    "cavally": "Guiglo",
    "bagoue": "Boundiali",
    "tchologo": "Ferkessédougou",
    "poro": "Korhogo",
    "kabadougou": "Odienné",
    "folon": "Minignan",
    "goh": "Gagnoa",
    "loh djiboua": "Divo",
    "haut sassandra": "Daloa",
    "marahoue": "Bouaflé"
}

# Liste des meilleurs scores
topScores = []
used_questions = set()  # Ensemble pour suivre les questions déjà posées

def view_top_score():
    print("\n--- Meilleurs Scores ---")
    if not topScores:
        print("Aucun score enregistré pour l'instant.")
    else:
        for i, score in enumerate(sorted(topScores, reverse=True)[:5], start=1):
            print(f"{i}. {score} points")
    print()

def play_game():
    global used_questions  # Utiliser l'ensemble global pour suivre les questions

    print("\nBienvenue au jeu sur les régions de Côte d'Ivoire !")
    view_top_score()

    available_questions = [
        (region, chef_lieu)
        for region, chef_lieu in ivoryCostRegions.items()
        if region not in used_questions
    ]

    # Vérifier si toutes les questions ont été posées
    if len(available_questions) < 10:
        print("\nToutes les questions ont été utilisées ! Réinitialisation...")
        used_questions.clear()
        available_questions = list(ivoryCostRegions.items())

    # Mélanger les questions et sélectionner 10
    questions = random.sample(available_questions, k=10)
    score = 0

    for i, (region, chef_lieu) in enumerate(questions, start=1):
        print(f"Question {i}: Quel est le chef-lieu de la région {region}?")
        reponse = input("Votre réponse: ").strip()

        # Comparaison ignorante de la casse
        if reponse.lower() == chef_lieu.lower():
            print("Bonne réponse !")
            score += 1
        else:
            print(f"Mauvaise réponse. La bonne réponse est: {chef_lieu}.")

        # Marquer cette question comme utilisée
        used_questions.add(region)

    print(f"\nPartie terminée ! Votre score: {score}/10")
    topScores.append(score)

    # Demander si le joueur veut rejouer
    replay = input("\nVeux-tu essayer une autre partie ? (o/n) : ").strip().lower()
    return replay == 'o'  # Retourne True si l'utilisateur veut rejouer, False sinon

def main():
    while True:
        print("\n=== Nouvelle Partie ===")
        if not play_game():
            print("Merci d'avoir joué ! À bientôt !")
            break

if __name__ == "__main__":
    main()
