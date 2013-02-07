from datetime import datetime, timedelta

from django.http import Http404
from django.core import serializers
from django.http import HttpResponse
from django.utils.timezone import utc

from models import Location

def firedata(request):
    if(request.method == 'GET'):
        locations = Location.objects.filter(
            acq_datetime__gte=(
                datetime.now() - timedelta(hours=48)
            ).replace(tzinfo=utc)
        )

        json_serializer = serializers.get_serializer("json")()
        return HttpResponse(
            json_serializer.serialize(locations), 
            content_type='application/json'
        )
    else:
        raise Http404


