from rest_framework.generics import ListAPIView

from events.models import Event

from .serializers import EventSerializer


class EventListView(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(acq_datetime__gt=arrow.utcnow().replace(days=-2))
