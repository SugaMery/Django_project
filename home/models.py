from django.db import models

class Users(models.Model):
    CATEGORY1 = (
            ('TC1', 'TC1'),
            ('TC2', 'TC2'),
            ('DIC1', 'DIC1'),
            ('DIC2', 'DIC2'),
            ('DIC3', 'DIC3'),
			) 
    CATEGORY = (
			('Génie électromécanique', 'Génie électromécanique'),
			('Génie civil', 'Génie civil'),
            ('Génie informatique et telecoms', 'Génie informatique et telecoms'),
            ('Tronc Commun', 'Tronc Commun'),
			) 
    departement = models.CharField(max_length=300,choices=CATEGORY)
    classe =models.CharField(max_length=200, choices=CATEGORY1)
    nom       =  models.CharField(max_length=250)
    prenom      =  models.CharField(max_length=250)
    lieu      =  models.CharField(max_length=250)
    code      =  models.CharField(max_length=250)
    email      =  models.EmailField()
    date  =models.DateField()

    def __str__(self) -> str: 
        return f"{self.nom}----{self.prenom}----{self.email}"