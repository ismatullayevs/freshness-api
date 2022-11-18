from rest_framework import serializers
from .models import Item, Category, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Item
        fields = ('title', 'description', 'category', 'image', 'created_at', 'modified_at',
                  'price', 'discount', 'slug', 'tags', 'get_price', 'get_average_rating',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
