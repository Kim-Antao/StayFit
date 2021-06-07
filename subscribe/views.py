from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from .forms import SubscriberForm
from plan.models import Plan_pricing

import stripe
# Create your views here.


@require_POST
def cache_subscribe_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': request.POST.get('plan_id'),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def subscribe(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    plan = None
    planId = request.GET['plan']
    plan = Plan_pricing.objects.filter(id=planId)

    for p in plan:
        plan_name = p.plan
        plan_price = p.price
        plan_period = p.payment_period

    stripe.api_key = stripe_secret_key

    if request.POST:
        payment_intent = stripe.PaymentIntent.create(
            amount=plan_price,
            currency=settings.STRIPE_CURRENCY,
            payment_method=['card'],
        ) 

    subscriber_form = SubscriberForm()
    template = 'subscribe/subscribe.html'

    context = {
        'subscribe_form': subscriber_form,
        'plan': plan,
        'stripe_public_key': 'pk_test_51HgvVyJHYp7lY4yyAxFeul2hZaWaTZV7eU5Aau4SJAFfQQHY8TFY9ElcpY73q8pjIg1YqFDFRp1inPevDgHOYmnn00rAzqt7Z1',
        'client_secret': 'test client secret',
        'customer_email': request.user.email,

    }

    return render(request, template, context)
