import io
from aiogram import types
from aiogram.dispatcher.filters import Command

from data.config import ADMINS
from loader import dp,bot
from filters import IsGroup
from filters.admins import AdminFilter


#guruh rasmini almashtirish
@dp.message_handler(IsGroup(),AdminFilter(),Command(commands='set_photo',prefixes='/!'))
async def set_photo(message:types.Message):
    source_message=message.reply_to_message
    if source_message and source_message.photo:
        photo=source_message.photo[-1]
        photo=await photo.download(destination=io.BytesIO())
        input_file=types.InputFile(photo)

        #guruh rasmini ozgartirish
        await message.chat.set_photo(photo=input_file)
        await message.reply("Guruh rasmi muvaffaqiyatli almashtirildi !")
    else:
        await message.reply("Iltimos  yangi rasmni reply qiling")


#guruh nomini almashtirish title()

@dp.message_handler(IsGroup(),AdminFilter(),Command(commands='set_title',prefixes='!/'))
async def set_group_title(message:types.Message):
    source_message=message.reply_to_message
    if source_message and source_message.text:
        title=source_message.text
        await bot.set_chat_title(message.chat.id,title=title)
        await message.reply("Guruh nomi  muvaffaqiyatli almashtirildi")

    else:
        await message.reply("Iltimos Yangi guruh nomini qaytadan reply qiling")


#guruh descriptionini almashtirish
@dp.message_handler(IsGroup(),AdminFilter(),Command(commands='set_description',prefixes='!/'))
async def set_group_description(message:types.Message):
    source_message=message.reply_to_message

    if source_message and source_message.text:
        description=source_message.text
        await message.chat.set_description(description)
        await message.reply("Guruh ma'lumotlari muvaffaqiyatli almashtirildi")

    else:
        await message.reply("Iltimos yangi guruh ma'lumotlarini reply qiling ")
