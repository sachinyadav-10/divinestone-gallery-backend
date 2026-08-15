from framework.core.base_apiviews import OpenAPIView
from framework.core.responses import SuccessResponse, ErrorResponse
from framework.utils import get_response
from rest_framework import status
from app.products.services.customer_service import ProductCustomerService
import logging

logger = logging.getLogger(__name__)

class ProductListingView(OpenAPIView):
    def get(self, request):
        try:
            error, data = ProductCustomerService.get_product_listing(request.query_params)
            
            if error:
                return get_response(ErrorResponse(message=error, status_code=status.HTTP_400_BAD_REQUEST))
            
            return get_response(SuccessResponse(data=data, message="Products fetched successfully"))
        except Exception as e:
            logger.error(f"Error in ProductListingView: {str(e)}", exc_info=True)
            return get_response(ErrorResponse(message="An unexpected error occurred", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR))

class ProductDetailView(OpenAPIView):
    def get(self, request, slug):
        try:
            error, data = ProductCustomerService.get_product_details(slug)
            
            if error:
                status_code = status.HTTP_404_NOT_FOUND if error == "Product not found" else status.HTTP_400_BAD_REQUEST
                return get_response(ErrorResponse(message=error, status_code=status_code))
            
            return get_response(SuccessResponse(data=data, message="Product details fetched successfully"))
        except Exception as e:
            logger.error(f"Error in ProductDetailView: {str(e)}", exc_info=True)
            return get_response(ErrorResponse(message="An unexpected error occurred", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR))
