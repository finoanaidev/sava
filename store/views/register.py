from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.person import Person
from django.views import View

from store.models.person import Person


class Register (View):
    def get(self, request):
        return render (request, 'register.html')

    def post(self, request):
        postData = request.POST
        name = postData.get ('name')
        commercial_name = postData.get ('commercial_name')
        address = postData.get ('address')
        phone_siege = postData.get ('phone_siege')
        email = postData.get ('email')
        num_fiscal = postData.get ('num_fiscal')
        num_stat = postData.get ('num_stat')
        num_cin = postData.get ('num_cin')
        nom_pers = postData.get ('nom_pers')
        phone_pers = postData.get ('phone_pers')
        email_pers = postData.get ('email_pers')
        password = postData.get ('password')
        # validation
        value = {
            'name': name,
            'commercial_name': commercial_name,
            'address': address,
            'phone_siege': phone_siege,
            'email': email,
            'num_fiscal': num_fiscal,
            'num_stat': num_stat,
            'num_cin': num_cin,
            'nom_pers': nom_pers,
            'phone_pers': phone_pers,
            'email_pers': email_pers,
        }
        error_message = None

        person = Person (name=name,
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
                             password=password)
        error_message = self.validatePerson (person)

        if not error_message:
            print (name, commercial_name, address, phone_siege, email, num_fiscal, num_stat, num_cin, nom_pers, phone_pers, email_pers, password)
            person.password = make_password (person.password)
            person.register ()
            return redirect ('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render (request, 'register.html', data)

   
        error_message = None
      
