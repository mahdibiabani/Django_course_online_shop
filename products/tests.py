# myapp/tests.py
from django.urls import reverse
from django.test import TestCase, client
from django.contrib.admin.sites import AdminSite
from .models import Product, Comment
from .admin import ProductAdmin, CommentAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .forms import CommentForm


class ProductAdminTestCase(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.product_admin = ProductAdmin(model=Product, admin_site=self.site)

    def test_list_display(self):
        # Test if list_display fields are correctly displayed
        self.assertEqual(self.product_admin.list_display, ['title', 'price', 'active'])

    # Add more test methods for ProductAdmin as needed


class CommentAdminTestCase(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.comment_admin = CommentAdmin(model=Comment, admin_site=self.site)

    def test_list_display(self):
        # Test if list_display fields are correctly displayed
        expected_fields = ['product', 'author', 'body', 'stars', 'active']
        self.assertEqual(self.comment_admin.list_display, expected_fields)


class ProductModelTestCase(TestCase):
    def setUp(self):
        # Create a sample Product instance for testing
        self.product = Product.objects.create(
            title="Sample Product",
            description="Test description",
            price=100,
            active=True
        )

    def test_product_str_representation(self):
        """Test the __str__ method of Product."""
        self.assertEqual(str(self.product), "Sample Product")

    def test_product_absolute_url(self):
        """Test the get_absolute_url method of Product."""
        expected_url = f"/products/{self.product.id}/"  # Replace with your actual URL pattern
        self.assertEqual(self.product.get_absolute_url(), expected_url)

    # Add more test methods for Product model as needed


class CommentModelTestCase(TestCase):
    def setUp(self):
        # Create a sample User instance for testing
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")

        # Create a sample Product instance for testing
        self.product = Product.objects.create(
            title="Sample Product",
            description="Test description",
            price=100,
            active=True
        )

        # Create a sample Comment instance for testing
        self.comment = Comment.objects.create(
            product=self.product,
            author=self.user,
            body="Test comment body",
            stars="4",
            active=True
        )


class ProductURLTestCase(TestCase):
    def setUp(self):
        # Create a sample Product instance for testing
        self.product = Product.objects.create(
            title="Sample Product",
            description="Test description",
            price=100,
            active=True
        )

    def test_product_list_url(self):
        """Test the product list view URL."""
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """Test the product detail view URL."""
        url = reverse('product_detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ProductListViewTestCase(TestCase):
    def test_product_list_view(self):
        """Test if the product list view returns a successful response."""
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, 200)

    # Add more test methods for ProductListView as needed


class ProductDetailViewTestCase(TestCase):
    def setUp(self):
        # Create a sample Product instance for testing
        self.product = Product.objects.create(
            title="Sample Product",
            description="Test description",
            price=100,
            active=True
        )

    def test_product_detail_view(self):
        """Test if the product detail view returns a successful response."""
        url = reverse('product_detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)






