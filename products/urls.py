from django.urls import path

from products.views import ProductListView, ProductDetailView, CommentCreateView
from .views import test_translation

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:product_id>/', CommentCreateView.as_view(), name='comment_create'),
    path('hello/', test_translation, )
]