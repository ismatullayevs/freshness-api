from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from .models import Item, Category
from .permissions import ReadOnly
from .serializers import ItemSerializer, CategorySerializer


class ItemListCreateAPIView(ListCreateAPIView):
    queryset = Item.objects.all()
    permission_classes = [IsAdminUser | ReadOnly]
    serializer_class = ItemSerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser | ReadOnly]
    pagination_class = None
