import time


class Enclos:
    #region Attributs
    nom = ""
    capacite_max = 0
    taille = 0
    liste_animaux = []
    #endregion
    
    #region Méthodes
    def ajouter_animal(self, animal):
        if animal in self.liste_animaux:
            print(f"{animal.nom} se trouve déjà dans l'enclos ❌")
        elif len(self.liste_animaux) >=  self.capacite_max:
            print("L'enclos est plein, impossible d'ajouter un nouvel animal ❌")
        else:
            self.liste_animaux.append(animal)
            print(f"{animal.nom} ajouté à la liste ✅")
    
    def enlever_animal(self, animal):
        if animal in self.liste_animaux:
            self.liste_animaux.remove(animal)
            print(f"{animal.nom} retiré de l'enclos 👋")
        else:
            print(f"{animal.nom} n'est pas présent dans l'enclos ❌")
    
    def afficher_animaux(self):
        if len(self.liste_animaux) > 0:
            print("Animaux dans l'enclos :")
            for animal in self.liste_animaux:
                if animal.en_vie:
                    print("--------------------------")
                    print(f"Nom             : {animal.nom}")
                    print(f"Satisfaction    : {animal.bonheur} / 100")
                    print(f"Appétit         : {animal.rassasier} /100")
                    print("--------------------------")
                else:
                    print("--------------------------")
                    print(f"💀 {animal.nom} est mort 💀")
                    print("--------------------------")
        else:
            print("--------------------------")
            print("L'enclos est vide...")
            print("--------------------------")
    
    def passer_un_jour(self):
        print("Passage d'une journée... 🌞")
        time.sleep(2)
        for animal in self.liste_animaux:
            animal.diminuer_rassasier()
            animal.diminuer_bonheur()
            if not animal.en_vie:
                self.enlever_animal(animal)
                time.sleep(2)
        print("Journée terminée 🌙")
        time.sleep(1)
    #endregion