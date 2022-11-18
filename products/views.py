from django_filters import rest_framework as filters
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from .models import Item, Category, Tag
from .permissions import ReadOnly
from .serializers import ItemSerializer, CategorySerializer, TagSerializer
from .filters import ItemFilter


class ItemListCreateAPIView(ListCreateAPIView):
    queryset = Item.objects.all()
    permission_classes = [IsAdminUser | ReadOnly]
    serializer_class = ItemSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ItemFilter


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser | ReadOnly]
    pagination_class = None


class TagListCreateAPIView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUser | ReadOnly]
    pagination_class = None
