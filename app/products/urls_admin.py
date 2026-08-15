from django.urls import path
from .views.admin_views import AdminProductCreateView, AdminProductDetailView

urlpatterns = [
    path('', AdminProductCreateView.as_view(), name='admin-product-create'),
    path('<int:product_id>/', AdminProductDetailView.as_view(), name='admin-product-detail'),
]
