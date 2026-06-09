class Soigneur:
    #region Attributs
    nom = ""
    date_naissance = ""
    experience = 0
    nombre_animaux_responsable = 0
    #endregion
    
    #region Méthodes
    def nourrir(self, animal):
        if animal.en_vie and animal.manger(self.nom):
            print(f"{self.nom} nourrit {animal.nom} 🍽️")
        else:
            print(f"L'animal {animal.nom} est mort, il ne peut pas être nourri.")
    
    def entretenir(self, animal):
        if animal.en_vie:
            animal.bonheur = 100
            print(f"{self.nom} entretiens {animal.nom} 💟")
        else:
            print(f"L'animal {animal.nom} est mort, il ne peut pas être entretenu....")
    #endregion
