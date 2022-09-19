from .views import AnnouncementViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('posts', AnnouncementViewSet, basename='posts')

urlpatterns = []

urlpatterns += router.urls