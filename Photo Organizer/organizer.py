import os


def get_photos(source_folder):
    """
    Returns a list of photo files (with full paths) from the source folder.
    """
    photo_extensions = ["jpg", "jpeg", "png", "gif", "bmp"]
    photos = []

    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)

        # Only keep files (not folders)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            ext = ext.lower().replace(".", "")

            if ext in photo_extensions:
                photos.append(file_path)