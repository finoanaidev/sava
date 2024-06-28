from django import template

register = template.Library()

@register.filter(name="currency")
def currency(price, request=None):
    try:
        if request is None:
            request = template.Variable('request').resolve({})

        if hasattr(request, 'currency'):
            currency = request.currency
        else:
            currency = settings.CURRENCY['options']['ariary']  # Définir une devise par défaut si non définie

        symbol = currency.get('symbol', '')  # Récupérer le symbole de la devise

        if currency['code'] == 'EUR':
            # Convertir le prix en Euro
            converted_price = price * currency['rate']
            return "€ {:.2f}".format(converted_price)  # Affichage avec 2 décimales et symbole Euro
        elif currency['code'] == 'USD':
            # Convertir le prix en Dollar
            converted_price = price * currency['rate']
            return "{} {:.2f}".format(symbol, converted_price)  # Affichage avec 2 décimales et symbole Dollar
        elif currency['code'] == 'MGA':
            return "{} {:.2f}".format(symbol, price)  # Affichage avec 2 décimales et symbole Ariary
        else:
            return "{:.2f} {}".format(price, symbol)  # Affichage avec 2 décimales et symbole par défaut
    except Exception as e:
        return price


@register.filter(name="multiply")
def multiply(number, number1):
    return number * number1

@register.filter
def to_range(value):
    return range(1, value)
