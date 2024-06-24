from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from django.utils.translation import gettext as _
from django.utils.translation import activate

class Login(View):
    return_url = None

    def get(self, request):
        # Activer la langue sélectionnée (si stockée en session par exemple)
        if 'django_language' in request.session:
            activate(request.session['django_language'])
        Login.return_url = request.GET.get("return_url")
        return render(request, "login.html")

    def post(self, request):
        # Activer la langue sélectionnée (si stockée en session par exemple)
        if 'django_language' in request.session:
            activate(request.session['django_language'])
        email = request.POST.get("email")
        password = request.POST.get("password")
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session["customer"] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect("homepage")
            else:
                error_message = "Invalid !!"
        else:
            error_message = "Invalid !!"

        print(email, password)
        return render(request, "login.html", {"error": error_message})


def logout(request):
    request.session.clear()
    return redirect("login")
