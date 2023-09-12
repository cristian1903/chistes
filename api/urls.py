from rest_framework.routers import DefaultRouter

from .views import ChisteViwset

router = DefaultRouter()

router.register(r'chistes', ChisteViwset, basename='chistes')

urlpatterns = router.urls