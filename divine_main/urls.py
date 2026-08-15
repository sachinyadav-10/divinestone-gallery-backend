from django.urls import path, include
from divine_main.views import health

urlpatterns = [
    # Global endpoints
    path('api/v1/health/', health),
    
    # Customer APIs (v1)
    path('api/v1/products/', include('app.products.urls_customer')),
    path('api/v1/reviews/', include('app.reviews.urls_customer')),
    path('api/v1/contact/', include('app.contactus.urls_customer')),
    path('api/v1/faqs/', include('app.faq.urls_customer')),

    # Admin APIs
    path('api/admin/products/', include('app.products.urls_admin')),
    path('api/admin/reviews/', include('app.reviews.urls_admin')),
    path('api/admin/contact/', include('app.contactus.urls_admin')),
    path('api/admin/faqs/', include('app.faq.urls_admin')),
]