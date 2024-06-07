from django import template

register = template.Library()

@register.filter(name="currency")
def currency(number, request):
    if hasattr(request, 'currency'):
        currency = request.currency
    else:
        currency = 'USD'

    if currency == 'EUR':
        return "€ " + str(number)
    elif currency == 'USD':
        return "$ " + str(number)
    elif currency == 'Ar':
        return "Ar " + str(number)
    else:
        return str(number) + " " + currency