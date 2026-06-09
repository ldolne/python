import datetime

class Soigneur:
    #region Constructeurs
    def __init__(self ,nom ,date_naissance ,exprerience = 0, nombre_animaux_responsable = 0):
        self._nom = nom
        self._date_naissance = date_naissance
        self._experience = exprerience
        self._nombre_animaux_responsable = nombre_animaux_responsable
    
    #endregion
    
    #region Prop's
    @property
    def nom(self):
        return self._nom

    @property
    def date_naissance(self):
        return self._date_naissance

    @property
    def experience(self):
        """
        Returns:
            int: nombre de jours d'activité du soigneur
        """
        return self._experience

    @property
    def nombre_animaux_responsable(self):
        return self._nombre_animaux_responsable
    
    @property
    def age(self):
        date_actuelle = datetime.date.today()
        difference =date_actuelle - self.date_naissance
        return difference // 365

    #endregion
    
    #region Méthodes
    def nourrir(self, animal):
        if animal.en_vie and animal.manger(self._nom):
            print(f"{self._nom} nourrit {animal.nom} 🍽️")
        else:
            print(f"{animal.nom} est mort, il ne peut pas être nourris 😭")
    
    def entretenir(self, animal):
        if animal.en_vie and animal.entretiens(self.nom):
            print(f"{self._nom} entretiens {animal.nom} 💟")
        else:
            print(f"{animal.nom} est mort, il ne peut pas être entretenus 😭")

    #endregion