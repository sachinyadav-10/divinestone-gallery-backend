from framework.core.base_apiviews import OpenAPIView
from framework.core.responses import SuccessResponse, ErrorResponse
from framework.utils import get_response
from rest_framework import status
from app.accounts.services.webhook_service import AccountWebhookService
import logging

logger = logging.getLogger(__name__)

class ClerkWebhookView(OpenAPIView):
    """
    Public webhook endpoint for Clerk to sync users.
    In production, this should verify Svix headers.
    """
    def post(self, request):
        try:
            # TODO: Verify Svix headers here for security
            
            payload = request.data
            error, data = AccountWebhookService.process_clerk_webhook(payload)
            
            if error:
                return get_response(ErrorResponse(message=error, status_code=status.HTTP_400_BAD_REQUEST))
            
            return get_response(SuccessResponse(data=data, message="Webhook processed successfully"))
        except Exception as e:
            logger.error(f"Error in ClerkWebhookView POST: {str(e)}", exc_info=True)
            return get_response(ErrorResponse(message="An unexpected error occurred", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR))
