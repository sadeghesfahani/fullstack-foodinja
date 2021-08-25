import PIL
from django.core.exceptions import ValidationError


def validate_file_size(file):
    filesize = file.size

    if filesize > 500000:
        raise ValidationError("The maximum file size that can be uploaded is 500kb")
    else:
        return file


def validate_square_shape(file):
    image = PIL.Image.open(file)
    width, height = image.size

    if width == height:
        return file
    else:
        raise ValidationError("picture must be square")