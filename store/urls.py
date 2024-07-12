from django.contrib import admin
from django.urls import path
from .views.home import Index, store
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.accueil import Accueil
from .views.simulation import simulation_menu, enregistrer_boite
from .views.detail import Detail
from .views.faq import Faq
from .views.register import Register, Register_save
from .views.registerVendeur import RegisterVendeur, RegisterVendeur_save
from .views.searchPage import SearchPage
from .views.change_language import change_language
from .views.csv import ExportOrdersCSV
from .views.order_list import order_list, update_order_status, delete_order
from .middlewares.auth import auth_middleware
<<<<<<< HEAD
from .views.registerseller import register_seller
from .views.loginseller import loginseller
=======

>>>>>>> 90a45fe9b0da982e183c27100a40501d1e5a1555

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store, name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
<<<<<<< HEAD
    path('check-out/', CheckOut.as_view(), name='checkout'),
    path('orders/', auth_middleware(OrderView.as_view()), name='orders'),
    path('accueil', Accueil, name='accueil'),
    path('faq/', Faq, name='Faq'),
    path('register/', Register, name='Register'),
    path('register_save/', Register_save, name='Register_save'),
    path('registerVendeur/', RegisterVendeur, name='RegisterVendeur'),
    path('registerVendeur_save/', RegisterVendeur_save, name='RegisterVendeur_save'),
    path('search/', SearchPage, name='SearchPage'),
    path('product/<int:id>/', Detail, name='Detail'),
    path('change-language/<str:language_code>/', change_language, name='change_language'),
    path('seller/', order_list, name='order_list'),
    path('seller/update/<int:order_id>/', update_order_status, name='update_order_status'),
    path('seller/delete/<int:order_id>/', delete_order, name='delete_order'),
    path('export-csv/', ExportOrdersCSV.as_view(), name='export_orders_csv'),
    path('simulation/', simulation_menu, name='simulation_menu'),
    path('enregistrer-boite/', enregistrer_boite, name='enregistrer_boite'),
    path('registerseller', register_seller, name='register_seller'),
    path('loginseller', loginseller, name='loginseller')
=======
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('accueil', Accueil, name='accueil'),
    path('faq', Faq, name='Faq'),
    path('register', Register, name='Register'),
    path('register_save', Register_save, name='Register_save'),
    path('registerVendeur', RegisterVendeur, name='RegisterVendeur'),
    path('registerVendeur_save', RegisterVendeur_save, name='RegisterVendeur_save'),
    path('search', SearchPage, name='SearchPage'),
    path('product/<int:id>', Detail, name='Detail'),
    path('change-language/<str:language_code>/', change_language, name='change_language'),
    path('seller', order_list, name='order_list'),  # URL pour la liste des commandes des vendeurs
    path('seller/update/<int:order_id>/', update_order_status, name='update_order_status'),    # Vendeur
    path('seller/delete/<int:order_id>/', delete_order, name='delete_order'),  # Vue pour supprimer une commande
    path('export-csv', ExportOrdersCSV.as_view(), name='export_orders_csv'),
    path('simulation', simulation_menu, name='simulation_menu'),
    path('enregistrer-boite', enregistrer_boite, name='enregistrer_boite'),

>>>>>>> 90a45fe9b0da982e183c27100a40501d1e5a1555
]
