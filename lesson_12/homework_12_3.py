""" (3.9)
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
import math

def calculate_page_amount(photo_amount: int):
    if isinstance(photo_amount, int) and not isinstance(photo_amount, bool):
        return math.ceil(photo_amount/8)
    else:
        raise TypeError