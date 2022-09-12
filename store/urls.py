from django.contrib import admin
from django.urls import path
from .views.home import Index, store
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.accueil import Accueil
from .views.detail import Detail
from .views.faq import Faq
from .views.register import Register
from .views.register import Register_save
from .views.registerVendeur import RegisterVendeur
from .views.registerVendeur import RegisterVendeur_save
from .views.searchPage import SearchPage
from .middlewares.auth import auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('accueil', Accueil, name='accueil'),
    path('faq', Faq, name='Faq'),
    path('register', Register, name='Register'),
    path('register_save', Register_save, name='Register_save'),
    path('registerVendeur', RegisterVendeur , name='RegisterVendeur'),
    path('registerVendeur_save', RegisterVendeur_save, name='RegisterVendeur_save'),
    path('search', SearchPage, name='SearchPage'),
    path('product/<int:id>', Detail, name='Detail'),
]
