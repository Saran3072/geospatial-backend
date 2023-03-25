from .views import imageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register( r'geo', imageViewSet)
urlpatterns = router.urls
