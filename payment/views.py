import requests
import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings

from orders.models import Order


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    zarinpal_request_url = 'https://api.zarinpal.com/pg/v4/payment/request.json'

    request_header = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    request_data = {
        'merchant_id': settings.ZARINPAL_MERCHANT_ID,
        'amount	': rial_total_price,
        'description': f'#{order.id}:{order.user.first_name} {order.user.last_name}',
        'callback_url': 'http://127.0.0.1:8000'

    }

    res = requests.post(zarinpal_request_url, json.dumps(request_data), headers=request_header)

    data = res.json()['data']
    authority = data['authority']
    order.zarinpal_authority = authority
    order.save()
    if 'errors' not in data or len(data['errors']) == 0:
        return redirect('https://www.zarinpal.com/pg/StartPay/{authority}'.format(authority=authority))
    else:
        return HttpResponse('error from zarinpal')





