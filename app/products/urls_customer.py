from django.urls import path
from .views.customer_views import ProductListingView, ProductDetailView

urlpatterns = [
    path('', ProductListingView.as_view(), name='product-list'),
    path('/<slug:slug>', ProductDetailView.as_view(), name='product-detail'),
]
