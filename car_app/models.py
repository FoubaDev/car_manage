from django.db import models


class Adresse(models.Model):
    telephone = models.CharField(max_length=120)
    email = models.CharField(max_length=200)
    quartier = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)

    def __str__(self):
        return self.email


class Personne(models.Model):
    Genre = (
        ('Masculin', 'Masculin'),
        ('Feminin', 'Feminin'),
        ('Autre', 'Autre'),
    )
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    genre = models.CharField(max_length=32, choices=Genre)

    def __str__(self):
        return self.nom


class Personnel(Personne):
    matricule = models.CharField(max_length=10)
    type_poste = models.CharField(max_length=300)
    my_choices = (
        ("Gerant", "Gerant"),
        ("Administrateur", "Administrateur"),
    )

    type_personnel = models.CharField(max_length=50, choices=my_choices)

    def __str__(self):
        return self.matricule


class Client(Personne):
    matricule = models.CharField(max_length=10)

    def __str__(self):
        return self.matricule


class Voiture(models.Model):
    immatriculation = models.CharField(max_length=100)
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    place = models.IntegerField(default=4)
    price = models.FloatField(blank=False, null=False)

    def __str__(self):
        return self.immatriculation


class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE)
    quantite = models.IntegerField(blank=False, null=False)
    montant = models.FloatField(blank=False, null=False)
    date_commande = models.DateField(auto_now_add=True)
    type = (
        ("Achat", "Achat"),
        ("Locations", "Locations"),
    )
    type_commande = models.CharField(max_length=50, choices=type)

    def __str__(self):
        return self.client
