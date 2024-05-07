from django.urls import include, path
from rest_framework import routers
from account import views

router = routers.DefaultRouter()
router.register("users", views.UserView)
router.register("profiles", views.ProfileView)
router.register("wshlists", views.WishlistView)

urlpatterns = [
    path("/", include(router.urls)),
]
