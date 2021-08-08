from djongo import models
from django.contrib.auth.models import User
from django import forms


class user(models.Model):
    prenom = models.CharField(max_length=300)
    nom = models.CharField(max_length=300)
    email = models.EmailField(max_length=255,null=True)

    def __str__(self) -> str:
        return f"{self.prenom}-----------{self.nom}-----------{self.email}"



class ClasseD(models.Model):
    CATEGORY = (
            ('TC1', 'TC1'),
            ('TC2', 'TC2'),
            ('DIC1', 'DIC1'),
            ('DIC2', 'DIC2'),
            ('DIC3', 'DIC3'),
			) 
    nom_classe =models.CharField(max_length=200, choices=CATEGORY)
    description_classe = models.CharField(max_length=300)
    def __str__(self) -> str:
        return f"{self.nom_classe}"

class Departement(models.Model):
    CATEGORY = (
			('Génie électromécanique', 'Génie électromécanique'),
			('Génie civil', 'Génie civil'),
            ('Génie informatique et telecoms', 'Génie informatique et telecoms'),
            ('Tronc Commun', 'Tronc Commun'),
			) 
    nom_departement = models.CharField(max_length=300,choices=CATEGORY)
    mail_departement = models.EmailField(max_length=255,null=True)
    numero_departement = models.CharField(max_length=300)
    description_dept = models.CharField(max_length=300)
    def __str__(self) -> str:
        return f"{self.nom_departement}"

class Etudiant(user):
    date_de_naissance = models.DateField(blank=False, null=False)
    lieu_de_naissance = models.CharField(max_length=300)
    classe = models.OneToOneField('ClasseD',on_delete=models.PROTECT)
    departement = models.ManyToManyField('Departement')
    def __str__(self) -> str:
        return f"{self.prenom}-----------{self.nom}-----------{self.email}-----------{self.date_de_naissance}-----------{self.lieu_de_naissance}"



class Enseigner(models.Model):
    class Meta:
        pass

    pass

class Professeur(user):
    contact_prof = models.CharField(max_length=300)
    date_d_adhesion = models.DateField(blank=False, null=False)
    departemet=models.ManyToManyField('Departement')
    def __str__(self) -> str:
        return f"{self.prenom}--{self.nom}"


class Chef_departement(models.Model):
    id=models.AutoField(primary_key=True)
    diriger = models.OneToOneField('Departement',on_delete=models.PROTECT)
    chef = models.OneToOneField('Professeur',on_delete=models.PROTECT)
    image = models.ImageField(upload_to='profile')
    def __str__(self) -> str:
        return f"{self.chef.prenom}--{self.chef.nom}--{self.diriger.nom_departement}------{self.image}"

class Matiere(models.Model):
    nom_matiere = models.CharField(max_length=300)
    code_matiere = models.IntegerField()
    coef_matiere = models.IntegerField()
    credit_matiere = models.CharField(max_length=300)
    quota_horaire = models.IntegerField()
    description_matiere = models.CharField(max_length=300)
    departemet=models.ManyToManyField('Departement')


