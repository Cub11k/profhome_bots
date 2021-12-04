from config import TOKEN
from telebot import TeleBot, types
from utils import create_demotivator, get_random_answer

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
        bot.send_message(msg.chat.id, "Ты не отправил фото, а зря\\! Попробуй еще раз")
        bot.register_next_step_handler_by_chat_id(msg.chat.id, receive_image_and_caption)
    else:
        if msg.caption is None:
            bot.send_message(msg.chat.id, "Ты не отправил подпись, а зря\\! Придётся придумать её за тебя")
        file_info = bot.get_file(msg.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        bot.send_photo(msg.chat.id, create_demotivator(downloaded_file, msg.caption))


@bot.message_handler(content_types=["text", "photo", "document", "audio", "video",
                                    "contact", "sticker", "video_note", "location"])
def random_answer(msg: types.Message):
    if msg.text is not None and msg.text.startswith("/"):
        bot.send_message(msg.chat.id, "Я такой команды не знаю, лучше попробуй /demotivator")
    else:
        bot.send_message(msg.chat.id, get_random_answer())


if __name__ == '__main__':
    while True:
        try:
            bot.infinity_polling()
        except Exception as e:
            print(e.with_traceback(e.__traceback__))
