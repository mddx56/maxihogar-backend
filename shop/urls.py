from django.urls import include, path
from rest_framework import routers
from shop import views

router = routers.DefaultRouter()
router.register("categorias", views.CategorieView)
router.register("subcategorias", views.Sub_CategorieView)
router.register("productos", views.ProductView)
router.register("produtoatribs", views.Product_AttributeView)
router.register("productoimages", views.Product_ImageView)
router.register("skus", views.Product_SkuView)

urlpatterns = [
    path("/", include(router.urls)),
]
