from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Product, Category
from .forms import ProductForm, ProductReviewForm

from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem


# Create your views here.
def all_products(request):
    """ A view to show all products including sorting and  search queries """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

            if not products:
                messages.error(request,
                               (f'No {query} found!'))
                return redirect(reverse('products'))

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product information """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    template = 'products/add_review.html'
    user = request.user
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductReviewForm(
                                request.POST,
                                initial={
                                    'product': product,
                                    'user': user
                                    },
                                )
        if form.is_valid():
            productReview = form.save()
            messages.success(request, 'Successfully added the review!')
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        profile = get_object_or_404(UserProfile, user=request.user)
        orders = Order.objects.all().filter(user_profile=profile.id)
        if not orders:
            messages.error(request, 'You need to purchase a product to review it')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            product_bought = orders.lineitems(product=product)
            if not product_bought:
                messages.error(request, 'You need to purchase a product to review it')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                form = ProductReviewForm(
                    initial={
                        'product': product.name,
                        'user': user.username
                    }
                )
    context = {
        'product': product,
        'form': form,
    }
    return render(request, template, context)
