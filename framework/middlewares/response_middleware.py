from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response
from framework.core.responses import SuccessResponse, ErrorResponse

class ResponseMiddleware(MiddlewareMixin):
    """
    Middleware to standardize API responses
    """
    def process_template_response(self, request, response):
        if hasattr(response, 'data'):
            if isinstance(response.data, (SuccessResponse, ErrorResponse)):
                response.data = {
                    'error': response.data.error,
                    'message': response.data.message,
                    'data': response.data.data
                }
                response.status_code = response.data.status_code if hasattr(response.data, 'status_code') else response.status_code
        return response

