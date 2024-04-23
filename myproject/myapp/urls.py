from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import user_orders, sort_products, product_form, product_detail


urlpatterns = [
    path("user_orders/<int:user_id>", user_orders, name="user_orders"),
    path("sort_products/<int:user_id>", sort_products, name="sort_products"),
    path("product_form/<int:product_id>", product_form, name="product_form"),
    path("product_detail/<int:product_id>", product_detail, name="product_detail"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
