from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.vendeur import Vendeur
from django.views import View
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages

from store.models.vendeur import Vendeur

def RegisterVendeur(request):
    return render(request, 'registerVendeur.html')

def RegisterVendeur_save(request):
     if request.method!="POST":
        return HttpResponseRedirect(reverse("RegisterVendeur"))
     else:
        name=request.POST.get("name")
        commercial_name=request.POST.get("commercial_name")
        marque_deposer=request.POST.get("marque_deposer")
        marque_representer=request.POST.get("marque_representer")
        address=request.POST.get("address")
        phone_siege=request.POST.get("phone_siege")
        email=request.POST.get("email")
        num_fiscal=request.POST.get("num_fiscal")
        num_stat=request.POST.get("num_stat")
        num_cin=request.POST.get("num_cin")
        nom_pers=request.POST.get("nom_pers")
        phone_pers=request.POST.get("phone_pers")
        email_pers=request.POST.get("email_pers")
        liste_pays=request.POST.get("liste_pays")
        liste_fournisseur=request.POST.get("liste_fournisseur")
        article_phare=request.POST.get("article_phare")
        secteur_activite=request.POST.get("secteur_activite")
        password=request.POST.get("password")
        cpass=request.POST.get("cpass")
        if password!=cpass:
            messages.error(request,"Confirm Password Doesn't Match")
            return HttpResponseRedirect(reverse('RegisterVendeur'))
        try:
            vendeur=Vendeur(name=name,commercial_name=commercial_name, marque_deposer=marque_deposer, marque_representer=marque_representer, address=address,phone_siege=phone_siege,num_fiscal=num_fiscal,email=email,num_stat=num_stat, num_cin=num_cin, nom_pers=nom_pers, email_pers=email_pers, phone_pers=phone_pers, liste_pays=liste_pays, liste_fournisseur=liste_fournisseur, article_phare=article_phare, secteur_activite=secteur_activite ,password=password)
            vendeur.save() 
            messages.success(request,"Data Save Successfully")
            return HttpResponseRedirect(reverse('RegisterVendeur'))
        except:
            messages.error(request,"Error in Saving Data")
            return HttpResponseRedirect(reverse('RegisterVendeur'))


    
