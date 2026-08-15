from framework.core.base_apiviews import ServiceAuthenticatedAPIView
from framework.core.responses import SuccessResponse, ErrorResponse
from framework.utils import get_response
from rest_framework import status
from app.products.services.admin_service import ProductAdminService
import logging

logger = logging.getLogger(__name__)

class AdminProductCreateView(ServiceAuthenticatedAPIView):
    def get(self, request):
        try:
            error, data = ProductAdminService.list_products()
            if error:
                return get_response(ErrorResponse(message=error, status_code=status.HTTP_400_BAD_REQUEST))
            return get_response(SuccessResponse(data=data, message="Products fetched successfully"))
        except Exception as e:
            logger.error(f"Error in AdminProductCreateView (GET): {str(e)}", exc_info=True)
            return get_response(ErrorResponse(message="An unexpected error occurred", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR))

    def post(self, request):
        try:
            error, data = ProductAdminService.create_product(request.data)
            if error:
                return get_response(ErrorResponse(message=error, status_code=status.HTTP_400_BAD_REQUEST))
            return get_response(SuccessResponse(data=data, message="Product created successfully", status_code=status.HTTP_201_CREATED))
        except Exception as e:
            logger.error(f"Error in AdminProductCreateView: {str(e)}", exc_info=True)
            return get_response(ErrorResponse(message="An unexpected error occurred", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR))

class AdminProductDetailView(ServiceAuthenticatedAPIView):
    def get(self, request, product_id):
        try:
            error, data = ProductAdminService.get_product(product_id)
            if error:
                status_code = status.HTTP_404_NOT_FOUND if error == "Product not found" else status.HTTP_400_BAD_REQUEST
                return get_response(ErrorResponse(message=error, status_code=status_code))
            return get_response(SuccessResponse(data=data, message="Product details fetched successfully"))
        except Exception as e:
            logger.error(f"Error in AdminProductDetailView (GET): {str(e)}", exc_info=True)
            return get_response(ErrorResponse(message="An unexpected error occurred", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR))

    def put(self, request, product_id):
        try:
            error, data = ProductAdminService.update_product(product_id, request.data)
            if error:
                status_code = status.HTTP_404_NOT_FOUND if error == "Product not found" else status.HTTP_400_BAD_REQUEST
                return get_response(ErrorResponse(message=error, status_code=status_code))
            return get_response(SuccessResponse(data=data, message="Product updated successfully"))
        except Exception as e:
            logger.error(f"Error in AdminProductDetailView (PUT): {str(e)}", exc_info=True)
            return get_response(ErrorResponse(message="An unexpected error occurred", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR))

    def delete(self, request, product_id):
        try:
            error, data = ProductAdminService.soft_delete_product(product_id)
            if error:
                return get_response(ErrorResponse(message=error, status_code=status.HTTP_404_NOT_FOUND))
            return get_response(SuccessResponse(data=data, message="Product soft-deleted successfully"))
        except Exception as e:
            logger.error(f"Error in AdminProductDetailView (DELETE): {str(e)}", exc_info=True)
            return get_response(ErrorResponse(message="An unexpected error occurred", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR))

    patch = put
