# plastisummer (c)

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
from data import datab as db

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот онлайн')
    db.sql_start()


@dp.message_handler(commands='start')
async def start(msg: types.Message):
    if (not db.sas(msg.from_user.id)):
        await db.add(msg.from_user.id, msg.from_user.username)
    else:
        await msg.reply('Вы уже запустили бота')


@dp.message_handler(commands='helpru')
async def unfollows(msg: types.Message):
    await msg.reply('/follow - получать рассылку\n/unfollow - отмена подписки')


@dp.message_handler(commands='help')
async def unfollows(msg: types.Message):
    await msg.reply('/follow - receive newsletter\n/ unfollow - unsubscribe')


@dp.message_handler(commands='unfollow')
async def unfollows(msg: types.Message):
    await db.unfollow(msg.from_user.id)
    await msg.reply('Вы успешно отписались от рассылки')


@dp.message_handler(commands='follow')
async def follows(msg: types.Message):
    await db.follow(msg.from_user.id)
    await msg.reply('Вы успешно подписались на рассылку')


@dp.message_handler()
async def echo(msg: types.Message):
    x = db.get_ids()
    users = len(db.get_ids())
    await msg.reply(f'Твоё сообщение будет отправлено {users} пользователям.')
    print(f'{msg.from_user.username}:{msg.text}')
    for i in x:
        zc = (db.chek(i[0]))
        if zc[0][0] == 1:
            try:
                await bot.send_message(text=msg.text, chat_id=i[0])
                if (not db.sas(msg.from_user.id)):
                    await db.add(msg.from_user.id, msg.from_user.username)
            except:
                print(f'error {i[0]} забанил бота')
                await db.del_user(i[0])
                print(f'{i[0]} удален')


@dp.message_handler(content_types=[types.ContentType.ANIMATION])
async def echo_anim(msg: types.Message):
    x = db.get_ids()
    users = len(db.get_ids())
    await msg.reply(f'Твоё сообщение будет отправлено {users} пользователям')
    print(f'{msg.from_user.username}')
    for i in x:
        zc = (db.chek(i[0]))
        if zc[0][0] == 1:
            try:
                await bot.send_animation(chat_id=i[0], animation=msg.animation.file_id, caption=msg.caption)
                if (not db.sas(msg.from_user.id)):
                    await db.add(msg.from_user.id, msg.from_user.username)
            except:
                print(f'error {i[0]} забанил бота')
                await db.del_user(i[0])
                print(f'{i[0]} удален')


@dp.message_handler(content_types=[types.ContentType.PHOTO])
async def echo_anim(msg: types.Message):
    x = db.get_ids()
    users = len(db.get_ids())
    await msg.reply(f'Твоё сообщение будет отправлено {users} пользователям')
    print(f'{msg.from_user.username}')
    for i in x:
        zc = (db.chek(i[0]))
        if zc[0][0] == 1:
            try:
                await bot.send_photo(chat_id=i[0], photo=msg.photo[-1].file_id, caption=msg.caption)
                if (not db.sas(msg.from_user.id)):
                    await db.add(msg.from_user.id, msg.from_user.username)
            except:
                print(f'error {i[0]} забанил бота')
                await db.del_user(i[0])
                print(f'{i[0]} удален')


@dp.message_handler(content_types=[types.ContentType.AUDIO])
async def echo_anim(msg: types.Message):
    x = db.get_ids()
    users = len(db.get_ids())
    await msg.reply(f'Твоё сообщение будет отправлено {users} пользователям')
    print(f'{msg.from_user.username}')
    for i in x:
        zc = (db.chek(i[0]))
        if zc[0][0] == 1:
            try:
                await bot.send_audio(chat_id=i[0], audio=msg.audio.file_id, caption=msg.caption)
                if (not db.sas(msg.from_user.id)):
                    await db.add(msg.from_user.id, msg.from_user.username)
            except:
                print(f'error {i[0]} забанил бота')
                await db.del_user(i[0])
                print(f'{i[0]} удален')


@dp.message_handler(content_types=[types.ContentType.DOCUMENT])
async def echo_anim(msg: types.Message):
    x = db.get_ids()
    users = len(db.get_ids())
    await msg.reply(f'Твоё сообщение будет отправлено {users} пользователям')
    print(f'{msg.from_user.username}')
    for i in x:
        zc = (db.chek(i[0]))
        if zc[0][0] == 1:
            try:
                await bot.send_document(chat_id=i[0], document=msg.document.file_id, caption=msg.caption)
                if (not db.sas(msg.from_user.id)):
                    await db.add(msg.from_user.id, msg.from_user.username)
            except:
                print(f'error {i[0]} забанил бота')
                await db.del_user(i[0])
                print(f'{i[0]} удален')


@dp.message_handler(content_types=[types.ContentType.VIDEO])
async def echo_anim(msg: types.Message):
    x = db.get_ids()
    users = len(db.get_ids())
    await msg.reply(f'Твоё сообщение будет отправлено {users} пользователям')
    print(f'{msg.from_user.username}')
    for i in x:
        zc = (db.chek(i[0]))
        if zc[0][0] == 1:
            try:
                await bot.send_video(chat_id=i[0], video=msg.video.file_id, caption=msg.caption)
                if (not db.sas(msg.from_user.id)):
                    await db.add(msg.from_user.id, msg.from_user.username)
            except:
                print(f'error {i[0]} забанил бота')
                await db.del_user(i[0])
                print(f'{i[0]} удален')


@dp.message_handler(content_types=[types.ContentType.VOICE])
async def echo_anim(msg: types.Message):
    x = db.get_ids()
    users = len(db.get_ids())
    await msg.reply(f'Твоё сообщение будет отправлено {users} пользователям')
    print(f'{msg.from_user.username}')
    for i in x:
        zc = (db.chek(i[0]))
        if zc[0][0] == 1:
            try:
                await bot.send_voice(chat_id=i[0], voice=msg.voice.file_id, caption=msg.caption)
                if (not db.sas(msg.from_user.id)):
                    await db.add(msg.from_user.id, msg.from_user.username)
            except:
                print(f'error {i[0]} забанил бота')
                await db.del_user(i[0])
                print(f'{i[0]} удален')


@dp.message_handler(content_types=[types.ContentType.VIDEO_NOTE])
async def echo_anim(msg: types.Message):
    x = db.get_ids()
    users = len(db.get_ids())
    await msg.reply(f'Твоё сообщение будет отправлено {users} пользователям')
    print(f'{msg.from_user.username}')
    for i in x:
        zc = (db.chek(i[0]))
        if zc[0][0] == 1:
            try:
                await bot.send_video_note(chat_id=i[0], video_note=msg.video_note.file_id)
                if (not db.sas(msg.from_user.id)):
                    await db.add(msg.from_user.id, msg.from_user.username)
            except:
                print(f'error {i[0]} забанил бота')
                await db.del_user(i[0])
                print(f'{i[0]} удален')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
