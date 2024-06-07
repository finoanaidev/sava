from django import template

register = template.Library()


@register.filter(name="currency")
def currency(price, request):
    if hasattr(request, 'currency'):
        currency = request.currency
    else:
        currency = 'Ar'

    if currency == 'EUR':
        # Convertir le prix en Euro
        converted_price = price * 0.0002065 
        return "€ {:.2f}".format(converted_price)  # Affichage avec 2 décimales
    elif currency == 'USD':
        # Convertir le prix en Dollar
        converted_price = price * 0.0002249 
        return "$ {:.2f}".format(converted_price)  # Affichage avec 2 décimales
    elif currency == 'Ar':
        return "Ar {:.2f}".format(price)  # Affichage avec 2 décimales
    else:
        return "{:.2f} {}".format(price, currency)  # Affichage avec 2 décimales


@register.filter(name="multiply")
def multiply(number, number1):
    return number * number1
