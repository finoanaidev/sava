from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View

from store.models.vendeur import Vendeur


class RegisterVendeur(View):
    def get(self, request):
        return render(request, "registerVendeur.html")

    def post(self, request):
        postData = request.POST
        name = postData.get("name")
        commercial_name = postData.get("commercial_name")
        address = postData.get("address")
        phone_siege = postData.get("phone_siege")
        email = postData.get("email")
        num_fiscal = postData.get("num_fiscal")
        num_stat = postData.get("num_stat")
        num_cin = postData.get("num_cin")
        nom_pers = postData.get("nom_pers")
        phone_pers = postData.get("phone_pers")
        email_pers = postData.get("email_pers")
        password = postData.get("password")
        # validation
        value = {
            "name": name,
            "commercial_name": commercial_name,
            "address": address,
            "phone_siege": phone_siege,
            "email": email,
            "num_fiscal": num_fiscal,
            "num_stat": num_stat,
            "num_cin": num_cin,
            "nom_pers": nom_pers,
            "phone_pers": phone_pers,
            "email_pers": email_pers,
            "liste_pays": liste_pays,
            "liste_fournisseur": liste_fournisseur,
            "article_phare": article_phare,
            "secteur_activite": secteur_activite,
        }
        error_message = None

        vendeur = Vendeur(
            name=name,
            commercial_name=commercial_name,
            address=address,
            phone_siege=phone_siege,
            email=email,
            num_fiscal=num_fiscal,
            num_stat=num_stat,
            num_cin=num_cin,
            nom_pers=nom_pers,
            phone_pers=phone_pers,
            email_pers=email_pers,
            liste_pays=liste_pays,
            liste_fournisseur=liste_fournisseur,
            article_phare=article_phare,
            secteur_activite=secteur_activite,
            password=password,
        )
        error_message = self.validateVendeur(vendeur)

        if not error_message:
            print(
                name,
                commercial_name,
                address,
                phone_siege,
                email,
                num_fiscal,
                num_stat,
                num_cin,
                nom_pers,
                phone_pers,
                email_pers,
                liste_pays,
                liste_fournissseur,
                article_phare,
                secteur_activite,
                password,
            )
            vendeur.password = make_password(vendeur.password)
            vendeur.register()
            return redirect("acceuil.html")
        else:
            data = {"error": error_message, "values": value}
            return render(request, "register.html", data)

    def validateVendeur(self, vendeur):
        error_message = None
        if not vendeur.name:
            error_message = "Please Enter your Name !!"
        elif len(vendeur.name) < 3:
            error_message = "Name must be 3 char long or more"
        elif not vendeur.commercial_name:
            error_message = "Please Enter your Commercial Name"
        elif len(vendeur.commercial_name) < 3:
            error_message = "Commercial Name must be 3 char long or more"
        elif not vendeur.address:
            error_message = "Enter your Address"
        elif len(vendeur.address) < 10:
            error_message = "Address must be 10 char Long"
        elif not vendeur.phone_siege:
            error_message = "Enter your Phone siege"
        elif len(vendeur.phone_siege) < 10:
            error_message = "Phone siege must be 10 char Long"
        elif len(vendeur.password) < 5:
            error_message = "Password must be 5 char long"
        elif len(vendeur.email) < 5:
            error_message = "Email must be 5 char long"
        elif Vendeur.isExists():
            error_message = "Email Address Already Registered.."
        # saving

        error_message = None
