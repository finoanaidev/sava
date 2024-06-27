from django_countries.fields import Country
from django.conf import settings
from django.utils import translation


class CurrencyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Request headers: ", request.META)  # Afficher les en-têtes de la requête

        user_country_code = request.META.get('HTTP_CF_IPCOUNTRY', 'MG')
        print(f"Raw country code from request: {user_country_code}")  # Débogage

        if user_country_code:
            user_country = Country(user_country_code)
        else:
            user_country = Country('')

        print(f"Country code from request: {user_country.code}")  # Débogage
        default_currency = settings.CURRENCY['default']

        if user_country.code == 'MG':  # Madagascar
            request.currency = settings.CURRENCY['options']['ariary']
        elif user_country.code in ('AF', 'EU'):  # Africa and Europe
            request.currency = settings.CURRENCY['options']['euro']
        else:  # Default to USD for other countries
            request.currency = settings.CURRENCY['options']['usd']

        print(f"Currency set to: {request.currency}")  # Débogage

        response = self.get_response(request)
        return response
