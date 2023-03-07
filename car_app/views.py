from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.template import loader
from .models import Commande
from .forms import *
from django.http import HttpResponseRedirect
from django.db.models import Q


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def commandes_list(request):
    commandes = Commande.objects.all().order_by('date_commande')
    return render(request, 'commandes/commandes_list.html', {'commandes': commandes, })


def add_commande(request):
    submitted = False
    if request.method == "POST":
        form1 = CommandeForm(request.POST, request.FILES)
        form2 = AdresseForm(request.POST, request.FILES)
        form3 = PersonneForm(request.POST, request.FILES)
        form4 = ClientForm(request.POST, request.FILES)
        form5 = VoitureForm(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
            f2=form2.save()
            form5=form5.save()
            form4=form4.save(commit=False)
            form3=form3.save(commit=False)
            form3.adresse_id = f2.id
            #form3.save()
            form4.nom = form3.nom
            form4.prenom = form3.prenom
            form4.genre = form3.genre
            form4.adresse_id = f2.id
            form4.save()
            form1 = form1.save(commit=False)
            form1.client_id = form4.id
            form1.voiture_id = form5.id
            form1.save()
            return HttpResponseRedirect('/add_commande?submitted=True')
        else:
            print(form1.errors, form2.errors, form3.errors, form4.errors, form5.errors)
    else:
        form1 = CommandeForm
        form2 = AdresseForm
        form3 = PersonneForm
        form4 = ClientForm
        form5 = VoitureForm
    if 'submitted' in request.GET:
        submitted = True
    return render(request, 'commandes/add_commande.html', {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5,
        'submitted': submitted,
    })


def show_commande(request, commande_id):
    commande = Commande.objects.get(pk=commande_id)
    return render(request, 'commandes/show_commande.html', {'commande': commande, })


def update_commande(request, commande_id):
    commande = Commande.objects.get(pk=commande_id)
    adresse = commande.adresse
    personne = Personne.objects.get(pk=commande_id)

    form1 = CommandeForm(request.POST or None, instance=commande)
    form2 = AdresseForm(request.POST or None, instance=adresse)
    form3 = PersonneForm(request.POST or None, instance=personne)

    if form1.is_valid() and form2.is_valid and form3.is_valid():
        form2.save()
        form3.save(commit=False)
        form1.adresse_id = form2
        form1.save()
        return redirect('commandes_list')
    return render(request, 'commandes/update_commande.html', {
        'commande': commande,
        'adresse': adresse,
        'personne': personne,
        'form1': form1,
        'form2': form2,
        'form3': form3,
    })


def delete_commande(request, commande_id):
    commande = Commande.objects.get(pk=commande_id)
    commande.delete()
    return redirect('commandes_list')


def search_commande(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            mutiple_q = Q(Q(nom__icontains=query) | Q(matricule__icontains=query))
        commandes = Commande.objects.filter(mutiple_q)
        if commandes:
            return render(request, 'commandes/commandes_list.html', {
                'commandes': commandes
            })
        else:
            print('Not found ...')
            return render(request, 'commandes/not_found.html', {})
