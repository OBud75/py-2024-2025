from datetime import datetime, timedelta

class GestionDate:
    def __init__(self):
        self.maintenant = datetime.now()

    def date_il_y_a_6_jours(self):
        il_y_a_6_jours = self.maintenant - timedelta(days=6)
        return il_y_a_6_jours.strftime('%Y-%m-%d')

gestion_date = GestionDate()
print(gestion_date.date_il_y_a_6_jours())
