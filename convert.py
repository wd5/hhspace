from django.core.management import setup_environ
import settings
setup_environ(settings)
from hhspace.account.models import Video

try:
    video = Video.objects.filter(converted=0)[0]
    video.convert()
except IndexError:
    print 'no file to convert';
