import io
import random

from PIL import Image, ImageDraw, ImageFont

default_captions = [
    "MAN",
    "Какой ты сегодня?"
    "ДАЙТЕ УД\nДАЙТЕ УД\nДАЙТЕ УД",
    "Are ya winning, son?"
    "Мальчик, водочки нам принеси\nМы МГУ закончили",
    "КАК БРАТА ТЕБЯ ПРОШУ\nВЫПРЯМИ СПИНУ",
    "ум ваче сей(("
]

default_answers = [
    "Раз на раз?",
    "Думаю что нет",
    "sample text",
    "Купи слона",
    "Д",
    "Удачи на сессии",
    "Пожалуй откажусь",
    "Ну привет",
    "Братан, займи сотку"
]


def get_random_answer():
    return random.choice(default_answers)


def create_demotivator(image: bytes, caption: str = None):

    if caption is None:
        caption = random.choice(default_captions)

    image_stream = io.BytesIO(image)
    photo = Image.open(image_stream)
    photo_w, photo_h = photo.size

    bg_w, bg_h = round(1.35*photo_w), round(1.35*photo_h) + 100
    background = Image.new('RGB', (bg_w, bg_h), color=(0, 0, 0))

    paste_w, paste_h = ((bg_w - photo_w) // 2, (bg_h - photo_h) // 2 - 80)
    background.paste(photo, (paste_w, paste_h))

    draw = ImageDraw.Draw(background)
    rectangle_w, rectangle_h = (paste_w + photo_w + 8, paste_h + photo_h + 8)
    draw.rectangle([(paste_w - 8, paste_h - 8), (rectangle_w, rectangle_h)],
                   fill=None, outline=(255, 255, 255), width=3)

    fnt = ImageFont.truetype('/usr/share/fonts/liberation/LiberationSerif-Regular.ttf', 50)
    draw.multiline_text((bg_w // 2, rectangle_h + 20), text=caption, anchor="ma", align="center", font=fnt, fill=None)

    background.save("img.jpg")
    fp = open("img.jpg", 'rb')
    return fp
