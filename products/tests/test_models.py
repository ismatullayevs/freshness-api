from django.test import TestCase
from ..models import Item, Category


class ItemTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            title="Fruits and vegetables",
        )
        cls.item = Item.objects.create(
            title="Tomato",
            description="Tomato is good for your health",
            category=cls.category,
            image='some image',
            price=123.45
        )

    def test_category_content(self):
        self.assertEqual(self.category.title, "Fruits and vegetables")
        self.assertEqual(self.category.slug, "fruits-and-vegetables")

    def test_item_content(self):
        self.assertEqual(self.item.title, "Tomato")
        self.assertEqual(self.item.description,
                         "Tomato is good for your health")
        self.assertEqual(self.item.slug, "tomato")
        self.assertEqual(self.item.category, self.category)
        self.assertEqual(self.item.price, 123.45)
        self.assertEqual(self.item.get_price(), 123.45)

    def test_item_discount(self):
        self.item.discount = 10
        self.assertEqual(self.item.get_price(), 111.105)
