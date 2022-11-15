from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet
from products.views import ItemListCreateAPIView, CategoryListCreateAPIView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename="users")

urlpatterns = [
    path('', include(router.urls)),
    path('items/', ItemListCreateAPIView.as_view(), name="item_list"),
    path('categories/', CategoryListCreateAPIView.as_view(), name="category_list"),
]
