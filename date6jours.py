from datetime import datetime, timedelta

# D'une manière générale on préfère coder an anglais (sauf si spécifié)
class GestionDate:
    def __init__(self):
        # Un peu dangereux car cela force le code appelant à faire
        # attention à bien instancier une GestionDate à chaque fois
        # Typiquement si on lance le code à 23h59 et 59 secondes
        # gestion_date = GestionDate()
        # ... 1 seconde passe pour x ou y raison ...
        # gestion_date.date_il_y_a_6_jours() sera faux
        self.maintenant = datetime.now()

    def date_il_y_a_6_jours(self):
        il_y_a_6_jours = self.maintenant - timedelta(days=6)
        return il_y_a_6_jours.strftime('%Y-%m-%d')

gestion_date = GestionDate()
print(gestion_date.date_il_y_a_6_jours())
