from django import forms

from .models import *


class AdresseForm(forms.ModelForm):
    class Meta:
        model = Adresse
        fields = ['telephone', 'email', 'quartier', 'ville']
        telephone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'telephone'}))
        email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Emaisl'}))
        quartier = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'quartier'})),
        ville = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ville'})),


class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['nom', 'prenom', 'genre']

        sexe = (
            ('', 'Choose...'),
            ('Masculin', 'Masculin'),
            ('Feminin', 'Feminin'),
            ('Autre', 'Autre'),
        )

        labels = {
            'nom': 'nom',
            'prenom': 'prenom',
            'genre': 'sexe',
        }

        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', }),
            'prenom': forms.TextInput(attrs={'class': 'form-control', }),
            'genre': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Genre', }),
        }


class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['matricule', 'type_poste', 'type_personnel']
        matricule = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'matricule'}))
        grade = forms.CharField(widget=forms.IntegerField())
        type_poste = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'type_poste'})),


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['matricule']
        labels = {
            'matricule': 'matricule'
        }
        matricule = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'matricule'}))


class VoitureForm(forms.ModelForm):
    class Meta:
        model = Voiture
        fields = ['immatriculation', 'marque', 'modele', 'place', 'price']
        immatriculation = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'immatriculation'})),
        marque = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'marque'})),
        modele = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'modele'})),
        price = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'price'})),


class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        type_c = (
            ('', 'Choose...'),
            ("Achat", ("Achat")),
            ("Locations", ("Locations")),
        )
        fields = ['quantite', 'montant', 'type_commande']
        labels = {
            # 'id_client':'id_client',
            # 'id_voiture':'id_voiture',
            'quantite': 'quantite',
            'montant': 'montant',
            'type_commande': 'type_commande'
        }
        #  id_client = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'matiere'}))
        # id_voiture = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'appreciation'})),
        quantite = forms.CharField(widget=forms.IntegerField()),
        montant = forms.CharField(widget=forms.IntegerField()),
        type_commande = forms.ChoiceField(choices=type_c),


"""
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', }),
            'naissance': forms.TextInput(
                attrs={'class': 'form-control', 'type': 'datetime-local', 'format': 'datetime-local'}),
            'genre': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Genre', }),
            'nationnalite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationnalité', }),
        }"""
