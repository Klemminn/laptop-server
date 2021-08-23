import io
import uuid
from PIL import Image
from django.core.files.storage import default_storage

def create_thumbnail(image_file, filename, height):
    image_buffer = io.BytesIO()

    image = Image.open(image_file)
    
    width = height * image.size[0] / image.size[1]
    image.thumbnail((width, height), Image.ANTIALIAS)
    image.save(image_buffer, format=image.format)
    
    thumbnail = default_storage.open(filename, 'wb')
    thumbnail.write(image_buffer.getvalue())
    thumbnail.close()
    return image_buffer

def handle_upload(instance, filename):
    small_height = 100
    uid = uuid.uuid4()
    file_type = filename.split('.')[-1]
    placement_key = 'components/%s' % (uid,)
    if instance.image is not None:
        create_thumbnail(
            instance.image.file.file,
            '%s-small.%s' % (placement_key, file_type,),
            small_height
        )
    return '%s.%s' % (placement_key, file_type,)
