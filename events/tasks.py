from __future__ import absolute_import

import csv
import requests
from io import StringIO

from datetime import datetime
from django.utils.timezone import utc
from django.core.management.base import BaseCommand, CommandError

from events.models import Event

from celery import shared_task


@shared_task
def get_event_data():
    all_locations_response = requests.get(
        "https://firms.modaps.eosdis.nasa.gov/active_fire/text/USA_contiguous_and_Hawaii_24h.csv", verify=False)

    f = StringIO(all_locations_response.text)
    reader = csv.DictReader(f)

    for row in reader:
        row['acq_datetime'] = datetime.strptime(
            "{} {}".format(row['acq_date'], row['acq_time'].strip()),
            "%Y-%m-%d %H%M").replace(tzinfo=utc)
        del row['acq_date']
        del row['acq_time']
        Event.objects.get_or_create(**row)

    f.close()
