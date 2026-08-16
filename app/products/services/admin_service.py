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
            if ProductRepository.soft_delete_product(product_id):
                return None, {"id": product_id}
            return "Product not found", None
        except Exception as e:
            return str(e), None

class CategoryAdminService:
    @staticmethod
    def list_categories():
        from app.products.repositories.product_repository import CategoryRepository
        from app.products.serializers.admin import CategoryAdminSerializer
        items = CategoryRepository.get_all()
        return None, CategoryAdminSerializer(items, many=True).data

    @staticmethod
    def create_category(data):
        from app.products.serializers.admin import CategoryAdminSerializer
        serializer = CategoryAdminSerializer(data=data)
        if serializer.is_valid():
            item = serializer.save()
            return None, CategoryAdminSerializer(item).data
        return str(serializer.errors), None

    @staticmethod
    def get_category(id):
        from app.products.repositories.product_repository import CategoryRepository
        from app.products.serializers.admin import CategoryAdminSerializer
        item = CategoryRepository.get_by_id(id)
        if not item: return "Not found", None
        return None, CategoryAdminSerializer(item).data

    @staticmethod
    def update_category(id, data):
        from app.products.repositories.product_repository import CategoryRepository
        from app.products.serializers.admin import CategoryAdminSerializer
        item = CategoryRepository.get_by_id(id)
        if not item: return "Not found", None
        serializer = CategoryAdminSerializer(item, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return None, serializer.data
        return str(serializer.errors), None

    @staticmethod
    def soft_delete_category(id):
        from app.products.repositories.product_repository import CategoryRepository
        if CategoryRepository.soft_delete(id):
            return None, {"id": id}
        return "Not found", None


class MaterialAdminService:
    @staticmethod
    def list_materials():
        from app.products.repositories.product_repository import MaterialRepository
        from app.products.serializers.admin import MaterialAdminSerializer
        items = MaterialRepository.get_all()
        return None, MaterialAdminSerializer(items, many=True).data

    @staticmethod
    def create_material(data):
        from app.products.serializers.admin import MaterialAdminSerializer
        serializer = MaterialAdminSerializer(data=data)
        if serializer.is_valid():
            item = serializer.save()
            return None, MaterialAdminSerializer(item).data
        return str(serializer.errors), None

    @staticmethod
    def get_material(id):
        from app.products.repositories.product_repository import MaterialRepository
        from app.products.serializers.admin import MaterialAdminSerializer
        item = MaterialRepository.get_by_id(id)
        if not item: return "Not found", None
        return None, MaterialAdminSerializer(item).data

    @staticmethod
    def update_material(id, data):
        from app.products.repositories.product_repository import MaterialRepository
        from app.products.serializers.admin import MaterialAdminSerializer
        item = MaterialRepository.get_by_id(id)
        if not item: return "Not found", None
        serializer = MaterialAdminSerializer(item, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return None, serializer.data
        return str(serializer.errors), None

    @staticmethod
    def soft_delete_material(id):
        from app.products.repositories.product_repository import MaterialRepository
        if MaterialRepository.soft_delete(id):
            return None, {"id": id}
        return "Not found", None


class DietyAdminService:
    @staticmethod
    def list_dieties():
        from app.products.repositories.product_repository import DietyRepository
        from app.products.serializers.admin import DietyAdminSerializer
        items = DietyRepository.get_all()
        return None, DietyAdminSerializer(items, many=True).data

    @staticmethod
    def create_diety(data):
        from app.products.serializers.admin import DietyAdminSerializer
        serializer = DietyAdminSerializer(data=data)
        if serializer.is_valid():
            item = serializer.save()
            return None, DietyAdminSerializer(item).data
        return str(serializer.errors), None

    @staticmethod
    def get_diety(id):
        from app.products.repositories.product_repository import DietyRepository
        from app.products.serializers.admin import DietyAdminSerializer
        item = DietyRepository.get_by_id(id)
        if not item: return "Not found", None
        return None, DietyAdminSerializer(item).data

    @staticmethod
    def update_diety(id, data):
        from app.products.repositories.product_repository import DietyRepository
        from app.products.serializers.admin import DietyAdminSerializer
        item = DietyRepository.get_by_id(id)
        if not item: return "Not found", None
        serializer = DietyAdminSerializer(item, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return None, serializer.data
        return str(serializer.errors), None

    @staticmethod
    def soft_delete_diety(id):
        from app.products.repositories.product_repository import DietyRepository
        if DietyRepository.soft_delete(id):
            return None, {"id": id}
        return "Not found", None
