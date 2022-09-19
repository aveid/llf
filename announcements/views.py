from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from announcements.models import Announcement
from announcements.serializers import AnnouncementSerializer


class AnnouncementViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def perform_create(self, serializer):
        print(self.request.user)
        return serializer.save(author=self.request.user)