from rest_framework import routers
from django.urls import path

from . import views

router = routers.DefaultRouter(trailing_slash=False)
# Admin urls

# User urls
router.register(prefix="products", viewset=views.ProductViewSet, basename="products")
router.register(prefix="product", viewset=views.AddProductViewSet, basename="product")


urlpatterns = [
    # Admin urls

    # User urls
] + router.urls
