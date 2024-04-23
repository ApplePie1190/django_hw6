from datetime import timedelta
from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404
from .models import User, Product, Order
from .forms import ProductForm
import logging


logger = logging.getLogger(__name__)


def user_orders(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer_id=user)
    return render(request, "myapp/user_orders.html", {"user": user, "orders": orders})


def sort_products(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    today = timezone.now()
    last_week = today - timedelta(days=7)
    last_month = today - timedelta(days=30)
    last_year = today - timedelta(days=365)

    orders_last_week = Order.objects.filter(
        customer_id=user, date_ordered__gte=last_week
    )
    orders_last_month = Order.objects.filter(
        customer_id=user, date_ordered__gte=last_month
    )
    orders_last_year = Order.objects.filter(
        customer_id=user, date_ordered__gte=last_year
    )

    products_last_week = Product.objects.filter(order__in=orders_last_week).distinct()
    products_last_month = Product.objects.filter(order__in=orders_last_month).distinct()
    products_last_year = Product.objects.filter(order__in=orders_last_year).distinct()

    context = {
        "user": user,
        "products_last_week": products_last_week,
        "products_last_month": products_last_month,
        "products_last_year": products_last_year,
    }

    return render(request, "myapp/sort_products.html", context)


def product_form(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail", product_id=product.id)
    else:
        form = ProductForm(instance=product)

    return render(request, "myapp/product_form.html", {"form": form})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "myapp/product_detail.html", {"product": product})
