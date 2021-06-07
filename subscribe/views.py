from django.shortcuts import render
from .forms import SubscriberForm

# Create your views here.


def subscribe(request):
    subscriber_form = SubscriberForm()
    template = 'subscribe/subscribe.html'

    context = {
        'subscribe_form': subscriber_form,
    }

    return render(request, template, context)
