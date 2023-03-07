from django.contrib import admin
from .models import*

# Register your models here.
#admin.site.register(Courses)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'nom', 'prenom', 'genre',)
    ordering = ('matricule',)
    search_fields = ('matricule',)

@admin.register(Personnel)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'nom', 'genre', 'type_poste', 'type_poste','type_personnel')
    ordering = ('matricule',)
    search_fields = ('matricule',)

@admin.register(Adresse)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('telephone', 'email', 'quartier', 'ville',)
    ordering = ('email',)
    search_fields = ('email',)

@admin.register(Commande)
class ClientAdmin(admin.ModelAdmin):
    list_display = ( 'client','voiture', 'quantite','montant','date_commande','type_commande' )
    ordering = ('date_commande', )
    search_fields = ('date_commande', )