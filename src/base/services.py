from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """Построение пути к файлу (media/avatar/user_id/photo.jpg)"""
    return f'avatar/{instance.id}/{file}'


def validate_size_image(file_obj):
    """Проверка размера файла"""
    mb_limit = 2
    if file_obj > mb_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла {mb_limit}MB")
