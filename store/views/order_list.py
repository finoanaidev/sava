from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from store.models.orders import Order
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string



def order_list(request):
    orders = Order.objects.order_by('-id')  # Fetch orders sorted by date descending
    return render(request, 'order_list.html', {'orders': orders})


def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status == 'Completed':
            order.status = True
            order.save()
            
            # Envoyer l'email au client
            subject_customer = 'Commande chez SAVA Chocolat compléter'
            message_customer = render_to_string('order_completed_customer.html', {'order': order, 'customer': order.customer})
            email_customer = EmailMultiAlternatives(subject_customer, message_customer, 'darcia.anona@gmail.com', [order.customer.email], reply_to=['sava.chocolat@gmail.com'])
            email_customer.attach_alternative(message_customer, "text/html")
            email_customer.send()

            # Envoyer l'email au vendeur
            subject_seller = 'Commande client compléter'
            message_seller = render_to_string('order_completed_seller.html', {'order': order})
            email_seller = EmailMultiAlternatives(subject_seller, message_seller, 'darcia.anona@gmail.com', ['sava.chocolat@gmail.com'])
            email_seller.attach_alternative(message_seller, "text/html")
            email_seller.send()
            
        else:
            order.status = False
            order.save()
        return redirect('order_list')
    return render(request, 'update_order_status.html', {'order': order})

def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')  # Redirection vers la liste des commandes après suppression
    # Si la méthode HTTP n'est pas POST, vous pouvez rediriger ou afficher un message d'erreur
    return redirect('order_list')