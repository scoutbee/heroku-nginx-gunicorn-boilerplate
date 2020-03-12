from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Counter


class GetView(APIView):
    def get(self, request):
        counter = Counter.objects.first()
        if not counter:
            counter = Counter.objects.create(value=0)

        return Response({"value": counter.value})


class IncreaseView(APIView):
    def post(self, request):
        counter = Counter.objects.first()
        if not counter:
            counter = Counter.objects.create(value=0)
        counter.value = counter.value + 1
        counter.save(update_fields=["value"])

        return Response({"value": counter.value})
