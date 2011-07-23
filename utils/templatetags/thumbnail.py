from PIL import Image
import os
from django import template
from django.conf import settings

register = template.Library()

THUMBNAILS = 'thumbnails'
SCALE_WIDTH = 'w'
SCALE_HEIGHT = 'h'

def scale(max_x, pair):
    x, y = pair
    new_y = (float(max_x) / x) * y
    return (int(max_x), int(new_y))

@register.filter
def thumbnail(original_image_path, arg):
    if not original_image_path:
        return 'none1'

    if not os.path.exists(settings.MEDIA_ROOT + original_image_path):
        return 'none from ' + settings.MEDIA_ROOT + original_image_path

    if arg.find(',') != -1:
        size, upload_path = [a.strip() for a in  arg.split(',')]
    else:
        size = arg
        upload_path = ''
        
    slash = original_image_path.rfind('/')
    if slash != -1:
        upload_path = original_image_path[0:slash] + upload_path



    if (size.lower().endswith('h')):
        mode = 'h'
    else:
        mode = 'w'

    # defining the size
    size = size[:-1]
    max_size = int(size.strip())

    # defining the filename and the miniature filename
    basename, format = original_image_path.rsplit('.', 1)
    basename, name = basename.rsplit('/', 1)

    miniature = name + '_' + str(max_size) + mode + '.' + format
    thumbnail_path = settings.MEDIA_ROOT + os.path.join(basename, THUMBNAILS)
    if not os.path.exists(thumbnail_path):
        os.mkdir(thumbnail_path)

    miniature_filename = os.path.join(thumbnail_path, miniature)
    miniature_url = '/'.join((settings.MEDIA_URL, upload_path, THUMBNAILS, miniature))

    # if the image wasn't already resized, resize it
    if not os.path.exists(miniature_filename) \
        or os.path.getmtime(settings.MEDIA_ROOT + original_image_path) > os.path.getmtime(miniature_filename):
        image = Image.open(settings.MEDIA_ROOT + original_image_path)
        image_x, image_y = image.size

        if mode == SCALE_HEIGHT:
            image_y, image_x = scale(max_size, (image_y, image_x))
        else:
            image_x, image_y = scale(max_size, (image_x, image_y))


        image = image.resize((image_x, image_y), Image.ANTIALIAS)

        image.save(miniature_filename, image.format)

    return miniature_url  
