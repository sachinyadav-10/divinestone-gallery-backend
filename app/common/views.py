from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Health


class HealthCheckAPIView(APIView):
    def get(self, request):
        if Health.objects.count() == 0:
            Health(name="MongoDB Connected").save()

        data = Health.objects.first()

        return Response(
            {
                "status": "ok",
                "database": data.name,
            }
        )