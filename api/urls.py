from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from .views import ProductView, ProductDetail

# router = DefaultRouter()
# router.register('products', ProductViewSet, 'Product')
# urlpatterns = router.urls
urlpatterns = [
    path('products/', ProductView.as_view(), name='product'),
    path('products_detail/', ProductDetail.as_view(), name='product_detail'),
]