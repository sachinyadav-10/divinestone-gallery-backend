from app.products.repositories.product_repository import ProductRepository
from app.products.serializers.admin import ProductAdminSerializer

class ProductAdminService:
    @staticmethod
    def list_products():
        try:
            products = ProductRepository.get_all_products()
            serializer = ProductAdminSerializer(products, many=True)
            return None, serializer.data
        except Exception as e:
            return str(e), None

    @staticmethod
    def get_product(product_id):
        try:
            product = ProductRepository.get_product_by_id(product_id)
            if not product:
                return "Product not found", None
            serializer = ProductAdminSerializer(product)
            return None, serializer.data
        except Exception as e:
            return str(e), None

    @staticmethod
    def create_product(data):
        try:
            serializer = ProductAdminSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return None, serializer.data
            return serializer.errors, None
        except Exception as e:
            return str(e), None

    @staticmethod
    def update_product(product_id, data):
        try:
            product = ProductRepository.get_product_by_id(product_id)
            if not product:
                return "Product not found", None
            
            serializer = ProductAdminSerializer(product, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return None, serializer.data
            return serializer.errors, None
        except Exception as e:
            return str(e), None

    @staticmethod
    def soft_delete_product(product_id):
        try:
            success = ProductRepository.soft_delete_product(product_id)
            if not success:
                return "Product not found", None
            return None, {"deleted": True}
        except Exception as e:
            return str(e), None
