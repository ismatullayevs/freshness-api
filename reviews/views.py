from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from products.permissions import ReadOnly
from .models import Review
from .serializers import ReviewSerializer


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminUser | ReadOnly]
