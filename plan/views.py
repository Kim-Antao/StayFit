from django.shortcuts import render


# Create your views here.
def all_plan(request):
    """ A view that renders all the plans """
    return render(request, 'plan/plan.html')
