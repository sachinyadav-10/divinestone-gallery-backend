from app.products.models import Product
from django.db.models import Q

class ProductRepository:
    @staticmethod
    def get_all_products():
        return Product.objects.all().order_by('-created_at')

    @staticmethod
    def get_active_products():
        return Product.objects.filter(is_active=True).select_related('category', 'material', 'diety').prefetch_related('images')

    @staticmethod
    def search_products(filters=None, sort_by=None, search_query=None):
        queryset = ProductRepository.get_active_products()

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(keywords__icontains=search_query) |
                Q(short_description__icontains=search_query)
            )

        if filters:
            if 'category' in filters and filters['category']:
                queryset = queryset.filter(category__slug=filters['category'])
            if 'diety' in filters and filters['diety']:
                queryset = queryset.filter(diety__name__icontains=filters['diety'])
            if 'height' in filters and filters['height']:
                queryset = queryset.filter(height__icontains=filters['height'])

        if sort_by:
            if sort_by == 'featured':
                queryset = queryset.order_by('-is_featured', '-created_at')
            elif sort_by == 'height':
                queryset = queryset.order_by('height')
            elif sort_by == 'price':
                queryset = queryset.order_by('selling_price')
            elif sort_by == '-price':
                queryset = queryset.order_by('-selling_price')
            else:
                queryset = queryset.order_by('-created_at')
        else:
            queryset = queryset.order_by('-created_at')

        return queryset

    @staticmethod
    def get_product_by_slug(slug):
        return ProductRepository.get_active_products().filter(slug=slug).first()

    @staticmethod
    def get_product_by_id(product_id):
        return Product.objects.filter(id=product_id).first()

    @staticmethod
    def soft_delete_product(product_id):
        product = ProductRepository.get_product_by_id(product_id)
        if product:
            product.is_active = False
            product.save()
            return True
        return False

    @staticmethod
    def get_active_categories():
        from app.products.models import Category
        return Category.objects.filter(is_active=True).order_by('name')

    @staticmethod
    def get_top_products_by_diety(limit_per_diety=5):
        from app.products.models import Diety
        dieties = Diety.objects.filter(is_active=True)
        result = []
        for diety in dieties:
            products = ProductRepository.get_active_products().filter(diety=diety).order_by('-is_featured', '-created_at')[:limit_per_diety]
            if products.exists():
                result.append({
                    "diety_id": diety.id,
                    "diety_name": diety.name,
                    "diety_slug": diety.slug,
                    "products": products
                })
        return result
