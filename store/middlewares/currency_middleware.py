from django.utils import translation

class CurrencyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Exemple simplifié utilisant la langue pour déterminer la devise
        user_language = translation.get_language()
        if user_language == 'fr':
            request.currency = 'EUR'
        else:
            request.currency = 'USD'

        response = self.get_response(request)
        return response