from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from store.models.orders import Order


def order_list(request):
    orders = Order.objects.order_by('-id')  # Fetch orders sorted by date descending
    return render(request, 'order_list.html', {'orders': orders})


def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status == 'Completed':
            order.status = True
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