import base64
import os
from django.templatetags.static import static
from django.utils.safestring import mark_safe
from django.conf import settings

def encode_image_as_base64(image_relative_path):
    image_path = os.path.join(settings.STATIC_ROOT, image_relative_path)
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode("utf-8")
    return mark_safe(f"data:image/png;base64,{encoded_string}")
