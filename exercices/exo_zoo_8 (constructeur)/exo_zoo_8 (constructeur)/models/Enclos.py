import time

class Enclos:
    #region Constructeurs
    def __init__(self ,nom ,capacite_max ,taille):
        self._nom = nom
        self._capacite_max = capacite_max
        self._taille = taille
        self._liste_animaux = []
    #region Prop's
    @property
    def nom(self):
        return self._nom
    
    @property
    def capacite_max(self):
        return self._capacite_max
    
    @property
    def taille(self):
        """
        Correspond a la surface de la zone d'enclos en m²
        """
        return self._taille
    
    @property
    def liste_animaux(self):
        return self._liste_animaux
    #endregion
    
    #region Méthodes
    def ajouter_animal(self, animal):
        if animal in self._liste_animaux:
            print(f"{animal.nom} se trouve déjà dans l'enclos ❌")
        elif len(self._liste_animaux) >=  self._capacite_max:
            print("L'enclos est plein, impossible d'ajouter un nouvel animal ❌")
        else:
            self._liste_animaux.append(animal)
            print(f"{animal.nom} ajouté à la liste ✅")
    
    def enlever_animal(self, animal):
        if animal in self._liste_animaux:
            self._liste_animaux.remove(animal)
            print(f"{animal.nom} retiré de l'enclos 👋")
        else:
            print(f"{animal.nom} n'est pas présent dans l'enclos ❌")
    
    def afficher_animaux(self):
        if len(self._liste_animaux) > 0:
            print("Animaux dans l'enclos :")
            for animal in self._liste_animaux:
                if animal.en_vie:
                    print(f"---------- {animal.apparence} ------------")
                    print(f"Nom             : {animal.nom}")
                    print(f"Satisfaction    : {animal.bonheur} / 100")
                    print(f"Appétit         : {animal.rassasier} /100")
                    print("--------------------------")
                else:
                    print("--------------------------")
                    print(f"{animal.apparence} {animal.nom} est mort 💀")
                    print("--------------------------")
        else:
            print("----------------------")
            print("❗ L'enclos est vide ❗")
            print("----------------------")
    
    def passer_un_jour(self):
        print("Passage d'une journée... 🌞")
        time.sleep(2)
        for animal in self._liste_animaux:
            animal.diminuer_rassasier()
            animal.diminuer_bonheur()
            if not animal.en_vie:
                self.enlever_animal(animal)
                time.sleep(2)
        print("Journée terminée 🌙")
        time.sleep(1)
    #endregion