from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import Item
from .serializers import ItemSerializer


# Obtener Datos
@api_view(["GET"])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


# Ingresar Datos
@api_view(["POST"])
def createItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
