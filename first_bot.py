import os

from config import TOKEN
from telebot import TeleBot, types
from PIL import Image, ImageDraw, ImageFont

bot = TeleBot(TOKEN, parse_mode="MarkdownV2")


@bot.message_handler(commands=["start"])
def start_command(msg: types.Message):
    bot.send_message(msg.chat.id, f"```\nПриветствую, {msg.from_user.first_name}, я пока на стадии разработки!\n" +
                     "Большинство функций будут доступны позже, а пока можешь создать демотиватор\n```/demotivator")


@bot.message_handler(commands=["help"])
def help_command(msg: types.Message):
    commands = ""
    for x in bot.get_my_commands(scope=None, language_code=None):
        commands += '/' + x.command + ' \\- ' + x.description + '\n'
    commands += ""
    bot.send_message(msg.chat.id, commands)


@bot.message_handler(commands=["demotivator"])
def meme_command(msg: types.Message):
    bot.send_message(msg.chat.id, "Кидай фото и подпись\\)")
    bot.register_next_step_handler_by_chat_id(msg.chat.id, receive_image_and_caption)


def receive_image_and_caption(msg: types.Message):
    if msg.photo is None:
        bot.send_message(msg.chat.id, "Ты не отправил фото, а зря! Попробуй еще раз")
        bot.register_next_step_handler_by_chat_id(msg.chat.id, receive_image_and_caption)
    elif msg.caption is None:
        bot.send_message(msg.chat.id, "Ты не отправил подпись, а зря! Попробуй еще раз")
        bot.register_next_step_handler_by_chat_id(msg.chat.id, receive_image_and_caption)
    else:
        file_info = bot.get_file(msg.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open("img.jpg", 'wb') as fp:
            fp.write(downloaded_file)
        create_demotivator(msg.chat.id, msg.caption)


def create_demotivator(chat_id: int, caption: str):
    photo = Image.open("img.jpg", "r")
    photo_w, photo_h = photo.size
    bg_w, bg_h = round(1.35*photo_w), round(1.35*photo_h) + 100
    background = Image.new('RGB', (bg_w, bg_h), color=(0, 0, 0))
    paste_w, paste_h = ((bg_w - photo_w) // 2, (bg_h - photo_h) // 2 - 80)
    background.paste(photo, (paste_w, paste_h))
    draw = ImageDraw.Draw(background)
    rectangle_w, rectangle_h = (paste_w + photo_w + 8, paste_h + photo_h + 8)
    draw.rectangle([(paste_w - 8, paste_h - 8), (rectangle_w, rectangle_h)], fill=None, outline=(255, 255, 255), width=3)
    fnt = ImageFont.truetype('/usr/share/fonts/liberation/LiberationSerif-Regular.ttf', 50)
    draw.text((bg_w // 2, rectangle_h + 20), text=caption, anchor="ma", font=fnt, fill=None)
    background.save('img.jpg')
    with open("img.jpg", 'rb') as fp:
        bot.send_photo(chat_id, fp)
        os.unlink("img.jpg")


if __name__ == '__main__':
    while True:
        try:
            bot.infinity_polling()
        except Exception as e:
            print(e.with_traceback(e.__traceback__))
