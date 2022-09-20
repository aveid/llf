from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from announcements.models import Announcement
from announcements.serializers import AnnouncementSerializer


class AnnouncementViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    @action(detail=False, methods=["get"])
    def search(self, request, pk=None):
        title = request.query_params.get('title')
        queryset = self.get_queryset()
        if title:
            queryset = self.get_queryset().filter(title__icontains=title)
        serializer = AnnouncementSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def filter_pr(self, request, pk=None):
        max_p = request.query_params.get('max')
        min_p = request.query_params.get('min')
        queryset = self.get_queryset()
        if max_p and min_p:
            queryset = self.get_queryset().filter(price__gte=min_p,
                                                  price__lte=max_p)
        serializer = AnnouncementSerializer(queryset, many=True)
        return Response(serializer.data)



