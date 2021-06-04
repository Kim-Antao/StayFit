from django.shortcuts import render
from .models import Plan, Plan_category, Plan_pricing


# Create your views here.
def all_plan(request):
    """ A view that renders all the plans """

    plan = Plan.objects.all()
    print(plan)
    plan_category = None

    if request.GET:
        if 'plan_category' in request.GET:
            plan_category = request.GET['plan_category'].split(' ')
            print(plan_category)
            plan = plan.filter(plan_category__name__in=plan_category)
            print(plan)
            plan_category = Plan_category.objects.filter(name__in=plan_category)
            plan_pricing = Plan_pricing.objects.all()

    context = {
        'plan': plan,
        'current_category': plan_category,
        'plan_pricing': plan_pricing,
    }
    return render(request, 'plan/plan.html', context)
