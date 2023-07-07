from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.contrib.auth import get_user_model
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


# Registrar Usuarios
@api_view(["POST"])
def register(request):
    if request.method == "POST":
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return JsonResponse(
                {"Message": "Username and password are required"}, status=400
            )
        User = get_user_model()

        try:
            User.objects.get(username=username)
            return JsonResponse({"Message": "Username already exist"}, status=400)
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password)
            return JsonResponse(
                {"Message": "Registration succesfully", "username": user.name}
            )
    else:
        return JsonResponse({"Message": "Method not allowed"}, status=405)
