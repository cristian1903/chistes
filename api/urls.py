from rest_framework.routers import DefaultRouter

from .views import ChisteViwset

router = DefaultRouter()

router.register(r'chiste', ChisteViwset, basename='chiste')

urlpatterns = router.urls