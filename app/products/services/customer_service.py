from app.products.repositories.product_repository import ProductRepository
from app.products.serializers.customer import ProductCardSerializer, ProductDetailSerializer

class ProductCustomerService:
    @staticmethod
    def get_product_listing(query_params):
        try:
            search_query = query_params.get('search')
            sort_by = query_params.get('sort')
            filters = {
                'category': query_params.get('category'),
                'diety': query_params.get('diety'),
                'height': query_params.get('height')
            }

            products = ProductRepository.search_products(filters=filters, sort_by=sort_by, search_query=search_query)
            data = ProductCardSerializer(products, many=True).data
            return None, data
        except Exception as e:
            return str(e), None

    @staticmethod
    def get_product_details(slug):
        try:
            product = ProductRepository.get_product_by_slug(slug)
            if not product:
                return "Product not found", None
            data = ProductDetailSerializer(product).data
            return None, data
        except Exception as e:
            return str(e), None

class CategoryCustomerService:
    @staticmethod
    def list_active():
        from app.products.repositories.product_repository import CategoryRepository
        from app.products.serializers.customer import CategoryCustomerSerializer
        items = CategoryRepository.get_active()
        return None, CategoryCustomerSerializer(items, many=True).data

class MaterialCustomerService:
    @staticmethod
    def list_active():
        from app.products.repositories.product_repository import MaterialRepository
        from app.products.serializers.customer import MaterialCustomerSerializer
        items = MaterialRepository.get_active()
        return None, MaterialCustomerSerializer(items, many=True).data

class DietyCustomerService:
    @staticmethod
    def list_active():
        from app.products.repositories.product_repository import DietyRepository
        from app.products.serializers.customer import DietyCustomerSerializer
        items = DietyRepository.get_active()
        return None, DietyCustomerSerializer(items, many=True).data
