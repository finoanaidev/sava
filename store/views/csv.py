# Dans views.py

import csv
from django.http import HttpResponse
from django.views.generic import View
from store.models.orders import Order

class ExportOrdersCSV(View):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="orders.csv"'

        writer = csv.writer(response)
        writer.writerow(['Order ID', 'Date', 'Customer', 'Delivery Address', 'Phone', 'Email', 'Product', 'Unit Price', 'Quantity', 'Total Price', 'Status'])

        for order in orders:
            writer.writerow([order.id, order.date, f"{order.customer.first_name} {order.customer.last_name}", order.address, order.phone, order.customer.email, order.product.name, order.product.price, order.quantity, order.price, "Completed" if order.status else "Pending"])

        return response
