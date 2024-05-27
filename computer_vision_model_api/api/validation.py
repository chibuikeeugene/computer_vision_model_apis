from api.config import ALLOWED_EXTENSIONS

def allowed_img_format(file: str):
    return '.' in file and file.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 