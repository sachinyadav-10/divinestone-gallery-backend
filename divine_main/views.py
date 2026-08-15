from django.http import JsonResponse

def health(request):
    return JsonResponse({
        "status": "ok",
        "message": "V1 Backend is successfully configured and running!"
    })
