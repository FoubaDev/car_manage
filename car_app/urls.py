from django.urls import path

from car_app.models import Client
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('commandes_list', views.commandes_list, name='commandes_list'),
    path('add_commande', views.add_commande, name='add_commande'),
    path('show_commande/<commande_id>', views.show_commande, name='show_commande'),
    path('delete_commande/<commande_id>', views.delete_commande , name='delete_commande'),
	path('update_commande/<commande_id>', views.update_commande,name='update_commande'),
    path('search_commande', views.search_commande, name='search_commande'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)