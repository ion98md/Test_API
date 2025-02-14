from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views
from .authentication import CustomTokenObtainClass

router = SimpleRouter(trailing_slash=False)
router.register(prefix="user", viewset=views.MeViewSet, basename="user")

urlpatterns = [
    path("login", CustomTokenObtainClass.as_view(), name="token_obtain"),
] + router.urls
