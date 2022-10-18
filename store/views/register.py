from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.person import Person
from django.views import View
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages

from store.models.person import Person

def Register(request):
    return render(request, 'register.html')

def Register_save(request):
     if request.method!="POST":
        return HttpResponseRedirect(reverse("Register"))
     else:
        name=request.POST.get("name")
        commercial_name=request.POST.get("commercial_name")
        address=request.POST.get("address")
        phone_siege=request.POST.get("phone_siege")
        email=request.POST.get("email")
        num_fiscal=request.POST.get("num_fiscal")
        num_stat=request.POST.get("num_stat")
        num_cin=request.POST.get("num_cin")
        nom_pers=request.POST.get("nom_pers")
        phone_pers=request.POST.get("phone_pers")
        email_pers=request.POST.get("email_pers")
        password=request.POST.get("password")
        cpass=request.POST.get("cpass")
        if password!=cpass:
            messages.error(request,"Il y a une erreur dans la confirmation du mot de passe")
            return HttpResponseRedirect(reverse('Register'))
        try:
            person=Person(name=name,commercial_name=commercial_name,address=address,phone_siege=phone_siege,num_fiscal=num_fiscal,email=email,num_stat=num_stat, num_cin=num_cin, nom_pers=nom_pers, email_pers=email_pers, phone_pers=phone_pers ,password=password)
            person.save() 
            messages.success(request,"Donnée enregistrer avec succès")
            return HttpResponseRedirect(reverse('Register'))
        except:
            messages.error(request,"Erreur lors de l'enregistrement des données")
            return HttpResponseRedirect(reverse('Register'))


    
