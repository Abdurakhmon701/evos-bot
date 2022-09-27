import logging 
from aiogram import Bot, Dispatcher, executor, types
from buttons import *
from aiogram.types import Message,CallbackQuery
from sql import *

API_TOKEN = '5674089305:AAEqiSeWX4gtNvQnB9E2mItZJp9-iWExlp4'

#=========================================================================================================

 # Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

tablitsa()
admin = 615003781
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    idisi= message.from_user.id
    name = message.from_user.first_name
    nik = message.from_user.username
    x = selekt_id(idisi)
    if x == []:
        qushish(idisi,name,nik)
        await message.reply("Assalomu alaykum, ro'yxatdan o'tishingiz mumkin",reply_markup = raqam)
    else:
        await message.reply("Siz ro'yxatdan o'tkansiz",reply_markup = inline_javob)
    
    # types.ReplyKeyboardRemove()


@dp.message_handler(content_types = ["contact"])
async def echo(message: types.Message):
    raqam = message.contact["phone_number"]
    idisi= message.from_user.id
    raqam_qushish(raqam,idisi)
    await message.answer("Joylashuv yuboring ",reply_markup = geo)

@dp.message_handler(content_types = ["location"])
async def echo1(message: types.Message):
    x = message.location["latitude"]
    y = message.location["longitude"]
    idisi= message.from_user.id
    location_qushish(x,y,idisi)
    z = info(idisi)
    # await message.answer("Ma'lumotlaringiz qabul qilindi.",reply_markup = inline_javob)
    await message.answer("Ma'lumotlaringiz qabul qilindi.",reply_markup = javob)
    await bot.send_message(admin,z,parse_mode = "HTML")
    await bot.send_location(admin,x, y)

def info(idisi):
    s = selekt_id(idisi) 
    info1 = f"<b>Yangi foydalanuvchi ro'yxatdan o'tdi:\n</b>"
    info1 += f"<b>ID: {s[0][1]}\nIsmi: {s[0][2]}\nUsername: @{s[0][3]}\nRaqam: +{s[0][4]}\n\n 🔽🔽🔽</b>"
    return info1



#=========================================================================================================
# # Configure logging
# logging.basicConfig(level=logging.INFO)

# # Initialize bot and dispatche
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)


# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#     await message.reply("Tilni tanlang",reply_markup=til)

# #=========================================================================================================
# bu O'zbek tili uchun
@dp.message_handler(text = "🇺🇿 O'zbekcha")
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer('Assalomu alaykum!',reply_markup = javob)

# Buyurtma uchun
@dp.message_handler(text = '🥗 Buyurtma berish:')
async def echo(message: types.Message):
    await message.answer('✅ Marhamat menu:',reply_markup = inline_javob)
# Inline knopkalar:
#=============================================================================================================
#=============================================================================================================
#=============================================================================================================

# Lavash bosilganda chiqadigan knopkalar
@dp.callback_query_handler(text = 'lavash')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Lavashlar menyusi: ",reply_markup = lavash_menu)

# lavash bosilganda birinchi ortga
@dp.callback_query_handler(text = 'ortga')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Marhamat menu:',reply_markup = inline_javob)
#=========================================================================================================
# Lavash Mol go'shtlik uchun
@dp.callback_query_handler(text = 'mol-goshtlik')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = lavash_mol_gushtlik_menu)

# lavashni mol goshti bosilganda ortga qaytish
@dp.callback_query_handler(text = 'ortga_2')
async def echo(call: CallbackQuery):
    await call.message.answer("✅ Marhamat Lavashlar menyusi: ",reply_markup = lavash_menu)

# lavashni mini bosganda raqamlar chiqazish
@dp.callback_query_handler(text = 'mini')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/1.jpg","rb"),
        caption = '''Narxi:18000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang:''',reply_markup = lavash_mol_gushtli_mini)

# Minidan chiqib ketish uchun
@dp.callback_query_handler(text = 'ortga_3')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = lavash_mol_gushtlik_menu)

# lavashni mol go'sht klassik uchun
@dp.callback_query_handler(text = 'klassik')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/1.jpg","rb"),
        caption = '''Narxi:20000 ming so'm 
Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang:''',reply_markup = lavash_mol_gushtli_klassik)

# Klassikdan chiqib ketish
@dp.callback_query_handler(text = 'ortga_4')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = lavash_mol_gushtlik_menu)

#=========================================================================================================

# Lavash Tovuq go'shtlik uchun menyu:
@dp.callback_query_handler(text = 'tovuqli')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = lavash_tovuq_gushtlik_menu)
# Lavash Tovuq go'shtidan chiqish:
@dp.callback_query_handler(text = 'ortga_5')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Lavashlar menyusi: ",reply_markup = lavash_menu)

# lavashni tovuq mini bosganda raqamlar chiqazish
@dp.callback_query_handler(text = 'mini1')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/2.jpg","rb"),
        caption = '''Narxi:18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang:''',reply_markup = lavash_tovuq_gushtli_mini)

# Minidan chiqib ketish uchun
@dp.callback_query_handler(text = 'ortga_6')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = lavash_tovuq_gushtlik_menu)

# lavashni tovuq go'sht klassik uchun
@dp.callback_query_handler(text = 'klassik1')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/2.jpg","rb"),
        caption = '''Narxi: 20000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang:''',reply_markup = lavash_tovuq_gushtli_klassik)

# Klassikdan chiqib ketish
@dp.callback_query_handler(text = 'ortga_7')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = lavash_tovuq_gushtlik_menu)

#=========================================================================================================

# Lavash qalampirli mol go'shti:

@dp.callback_query_handler(text = 'qmolgoshtlik')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = lavash_mol_qalampir_gushtlik_menu)
# Lavash qalampirli mol go'shtidan chiqish:
@dp.callback_query_handler(text = 'ortga_8')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Lavashlar menyusi: ",reply_markup = lavash_menu)

# lavashni qalampirli mol mini bosganda raqamlar chiqazish
@dp.callback_query_handler(text = 'mini2')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/3.jpg","rb"),
        caption = '''Narxi: 18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang:''',reply_markup = lavash_qalampir_mol_gushtli_mini)

# Minidan chiqib ketish uchun
@dp.callback_query_handler(text = 'ortga_9')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = lavash_mol_qalampir_gushtlik_menu)

# lavashni qalampirli mol klassik uchun
@dp.callback_query_handler(text = 'klassik2')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/3.jpg","rb"),
        caption = '''Narxi: 20000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang:''',reply_markup = lavash_qalampir_mol_gushtli_klassik)

# Klassikdan chiqib ketish
@dp.callback_query_handler(text = 'ortga_10')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = lavash_mol_qalampir_gushtlik_menu)
#=============================================================================================================
# Lavash qalampir tovuqli
@dp.callback_query_handler(text = 'qtovuqli')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = lavash_qalampir_tovuq_gushtlik_menu)

# Lavash Tovuq-qalampir go'shtidan chiqish:
@dp.callback_query_handler(text = 'ortga_11')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Lavashlar menyusi: ",reply_markup = lavash_menu)

# lavashni qalampirli tovuq mini bosganda raqamlar chiqazish
@dp.callback_query_handler(text = 'mini3')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/4.jpg","rb"),
        caption = '''Narxi: 18000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang:''',reply_markup = lavash_qalampir_tovuq_gushtli_mini)

# Minidan chiqib ketish uchun
@dp.callback_query_handler(text = 'ortga_12')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = lavash_qalampir_tovuq_gushtlik_menu)

# lavashni qalampirli tovuq klassik uchun
@dp.callback_query_handler(text = 'klassik3')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/4.jpg","rb"),
        caption = '''Narxi: 20000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang:''',reply_markup = lavash_qalampir_tovuq_gushtli_klassik)

# Klassikdan chiqib ketish
@dp.callback_query_handler(text = 'ortga_13')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = lavash_qalampir_tovuq_gushtlik_menu)

# Lavash Fitter
@dp.callback_query_handler(text = 'fitter')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/5.jpg","rb"),
        caption = '''Narxi: 20000 ming so'm 
Tarkibi:Xamir,tovuq go'sht,chips,pomidor,bodring,sous,moyonez
Miqdorini tanlang:''',reply_markup = fitter)

# Lavash Fitterdan chiqish:
@dp.callback_query_handler(text = 'ortga_19')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Lavashlar menyusi: ",reply_markup = lavash_menu)





#=============================================================================================================
#=============================================================================================================
#=============================================================================================================

# Hot - dog uchun menyu:
@dp.callback_query_handler(text = 'hot-dog')
async def echo(call: CallbackQuery):
    await call.message.answer("✅✅Marhamat Hot-dog lar menyusi: ",reply_markup = hot_dog_menu)

# hot-dog bosilganda birinchi ortga
@dp.callback_query_handler(text = 'ortga')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Marhamat menu:',reply_markup = inline_javob)
#=============================================================================================================

# Hot - dog Korolevskiy 
@dp.callback_query_handler(text = 'korolevskiy')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/7.jpg","rb"),
        caption = '''Narxi:15000 ming so'm 
Tarkibi:✅Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang:''',reply_markup = Hot_dog_korolevskiy)
# Hot - dog Korolevskiydan chiqish:
@dp.callback_query_handler(text = 'ortga_17')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Hot-dog lar menyusi: ",reply_markup = hot_dog_menu)

#=============================================================================================================

# Hot - dog dabl 
@dp.callback_query_handler(text = 'double')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/6.jpg","rb"),
        caption = '''Narxi:18000 ming so'm 
Tarkibi:✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang:''',reply_markup = Hot_dog_dabl)
# Hot - dog Korolevskiydan chiqish:
@dp.callback_query_handler(text = 'ortga_16')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Hot-dog lar menyusi: ",reply_markup = hot_dog_menu)

#=============================================================================================================

# Hot - dog tovuqli 
@dp.callback_query_handler(text = 'hot_dog_tovuqli')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/8.jpg","rb"),
        caption = '''Narxi:17000 ming so'm 
Tarkibi:✅Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang:''',reply_markup = Hot_dog_tovuqli)
# Hot - dog Korolevskiydan chiqish:
@dp.callback_query_handler(text = 'ortga_18')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Hot-dog lar menyusi: ",reply_markup = hot_dog_menu)

#=============================================================================================================

# Hot - dog klassik 
@dp.callback_query_handler(text = 'classic')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/9.jpg","rb"),
        caption = '''Narxi:8000 ming so'm 
Tarkibi:✅Kulcha,sosiska,ketchup va xantal,qovurilgan piyoz.
Miqdorini tanlang:''',reply_markup = Hot_dog_klassik)
# Hot - dog Korolevskiydan chiqish:
@dp.callback_query_handler(text = 'ortga_15')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Hot-dog lar menyusi: ",reply_markup = hot_dog_menu)

#=============================================================================================================
#=============================================================================================================
#=============================================================================================================
# Donar bosganda menyu
@dp.callback_query_handler(text = 'donar')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Donar menyusi: ",reply_markup = donar_menu)

# Donar bosilganda birinchi ortga
@dp.callback_query_handler(text = 'ortga_20')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Marhamat menu:',reply_markup = inline_javob)
#=============================================================================================================
# Donar mol go'shtlik 
@dp.callback_query_handler(text = 'mdonar')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/10.jpg","rb"),
        caption = '''Narxi:23000 ming so'm 
Miqdorini tanlang:''',reply_markup = Donar_mol_gushtli)
# Donar mol go'shtlikdan chiqish:
@dp.callback_query_handler(text = 'ortga_21')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Donar menyusi: ",reply_markup = donar_menu)
#=============================================================================================================
# Donar tovuq go'shtlik 
@dp.callback_query_handler(text = 'tdonar')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/11.jpg","rb"),
        caption = '''Narxi:20000 ming so'm 
Miqdorini tanlang:''',reply_markup = Donar_tovuqli)
#  Donar tovuq go'shtlikdan chiqish:
@dp.callback_query_handler(text = 'ortga_22')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Donar menyusi: ",reply_markup = donar_menu)
#=============================================================================================================
#=============================================================================================================
#=============================================================================================================

# Club bosganda menyu
@dp.callback_query_handler(text = 'sendwich-club')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Club menyusi: ",reply_markup = club_sendwich_menu)

# Club bosilganda birinchi ortga
@dp.callback_query_handler(text = 'ortga_23')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Marhamat menu:',reply_markup = inline_javob)

#=============================================================================================================

# Club mol go'shtlik 
@dp.callback_query_handler(text = 'club_c')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/12.jpg","rb"),
        caption = '''Narxi:32000 ming so'm 
Tarkibi:✅Toster-non, mol go'shti, pomidor, sous,  piyoz.
Miqdorini tanlang:''',reply_markup = Club_classic)
# Club mol go'shtlikdan chiqish:
@dp.callback_query_handler(text = 'ortga_24')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Club menyusi: ",reply_markup = club_sendwich_menu)

#=============================================================================================================

# Club tovuq go'shtlik 
@dp.callback_query_handler(text = 'club_t')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/12.jpg","rb"),
        caption = '''Narxi:30000 ming so'm 
Miqdorini tanlang:''',reply_markup = Club_tovuqli)
#  Club tovuq go'shtlikdan chiqish:
@dp.callback_query_handler(text = 'ortga_25')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Club menyusi: ",reply_markup = club_sendwich_menu)

#=============================================================================================================
#=============================================================================================================
#=========================================================================================================

# Shaurma bosganda menyu
@dp.callback_query_handler(text = 'shaurma')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Shaurma menyusi: ",reply_markup = shaurma_menu)

# Shaurma bosilganda birinchi ortga
@dp.callback_query_handler(text = 'ortga')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Marhamat menu:',reply_markup = inline_javob)

#=========================================================================================================
# Shaurma Mol go'shtlik uchun
@dp.callback_query_handler(text = 'shaurma_mol-goshtlik')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = shaurma_mol_gushtlik_menu)

# Shaurmani mol goshti bosilganda ortga qaytish
@dp.callback_query_handler(text = 'ortga_26')
async def echo(call: CallbackQuery):
    await call.message.answer("✅ Marhamat Shaurma menyusi: ",reply_markup = shaurma_menu)

# Shaurmani mini bosganda raqamlar chiqazish
@dp.callback_query_handler(text = 'shaurma_mini')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/13.jpg","rb"),
        caption = '''Narxi:19000 ming so'm 
Miqdorini tanlang:''',reply_markup = shaurma_mol_gushtli_mini)

# Minidan chiqib ketish uchun
@dp.callback_query_handler(text = 'ortga_27')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = shaurma_mol_gushtlik_menu)

# Shaurmani mol go'sht klassik uchun
@dp.callback_query_handler(text = 'shaurma_klassik')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/13.jpg","rb"),
        caption = '''Narxi:22000 ming so'm 
Miqdorini tanlang:''',reply_markup = shaurma_mol_gushtli_klassik)

# Klassikdan chiqib ketish
@dp.callback_query_handler(text = 'ortga_28')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = shaurma_mol_gushtlik_menu)

#=========================================================================================================

# Shaurma Tovuq go'shtlik uchun menyu:
@dp.callback_query_handler(text = 'shaurma_tovuqli')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = shaurma_tovuq_gushtlik_menu)
# Shaurma Tovuq go'shtidan chiqish:
@dp.callback_query_handler(text = 'ortga_29')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Shaurma menyusi: ",reply_markup = shaurma_menu)

# Shaurmani tovuq mini bosganda raqamlar chiqazish
@dp.callback_query_handler(text = 'shaurma_mini1')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/15.jpg","rb"),
        caption = '''Narxi:19000 ming so'm 
Miqdorini tanlang:''',reply_markup = lavash_tovuq_gushtli_mini)

# Minidan chiqib ketish uchun
@dp.callback_query_handler(text = 'ortga_30')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = shaurma_tovuq_gushtlik_menu)

# Shaurmani tovuq go'sht klassik uchun
@dp.callback_query_handler(text = 'shaurma_klassik1')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/15.jpg","rb"),
        caption = '''Narxi:22000 ming so'm 
Miqdorini tanlang:''',reply_markup = lavash_tovuq_gushtli_klassik)

# Klassikdan chiqib ketish
@dp.callback_query_handler(text = 'ortga_31')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = lavash_tovuq_gushtlik_menu)

#=========================================================================================================

# Shaurma qalampirli mol go'shti:

@dp.callback_query_handler(text = 'shaurma_qmolgoshtlik')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = shaurma_qalampir_mol_gushtlik_menu)
# Shaurma Tovuq go'shtidan chiqish:
@dp.callback_query_handler(text = 'ortga_33')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Shaurma menyusi: ",reply_markup = shaurma_menu)

# Shaurma qalampirli mol mini bosganda raqamlar chiqazish
@dp.callback_query_handler(text = 'shaurma_mini2')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/14.jpg","rb"),
        caption = '''Narxi:19000 ming so'm 
Miqdorini tanlang:''',reply_markup = shaurma_qalampir_mol_gushtli_mini)

# Minidan chiqib ketish uchun
@dp.callback_query_handler(text = 'ortga_34')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = shaurma_qalampir_mol_gushtlik_menu)

# Shaurma qalampirli mol klassik uchun
@dp.callback_query_handler(text = 'shaurma_klassik2')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/14.jpg","rb"),
        caption = '''Narxi:22000 ming so'm 
Miqdorini tanlang:''',reply_markup = shaurma_qalampir_mol_gushtli_klassik)

# Klassikdan chiqib ketish
@dp.callback_query_handler(text = 'ortga_35')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = shaurma_qalampir_mol_gushtlik_menu)
#=============================================================================================================
# Shaurma qalampir tovuqli
@dp.callback_query_handler(text = 'shaurma_qtovuqli')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = shaurma_qalampir_tovuq_gushtlik_menu)

# Shaurma Tovuq-qalampir go'shtidan chiqish:
@dp.callback_query_handler(text = 'ortga_36')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Shaurma menyusi: ",reply_markup = shaurma_menu)

# Shaurma qalampirli tovuq mini bosganda raqamlar chiqazish
@dp.callback_query_handler(text = 'shaurma_mini3')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/16.jpg","rb"),
        caption = '''Narxi:19000 ming so'm 
Miqdorini tanlang:''',reply_markup = shaurma_qalampir_tovuq_gushtli_mini)

# Minidan chiqib ketish uchun
@dp.callback_query_handler(text = 'ortga_37')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = shaurma_qalampir_tovuq_gushtlik_menu)

# Shaurma qalampirli tovuq klassik uchun
@dp.callback_query_handler(text = 'shaurma_klassik3')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/16.jpg","rb"),
        caption = '''Narxi:22000 ming so'm 
Miqdorini tanlang:''',reply_markup = shaurma_qalampir_tovuq_gushtli_klassik)

# Klassikdan chiqib ketish
@dp.callback_query_handler(text = 'ortga_38')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Kategoriyilardan birini tanlang:',reply_markup = shaurma_qalampir_tovuq_gushtlik_menu)
#=============================================================================================================
#=============================================================================================================
#=============================================================================================================

# Burger bosganda menyu
@dp.callback_query_handler(text = 'burger')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Burger menyusi: ",reply_markup = burger_menu)

# Burger bosilganda birinchi ortga
@dp.callback_query_handler(text = 'ortga')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Marhamat menu:',reply_markup = inline_javob)

#=============================================================================================================

# Burger mol go'shtlik 
@dp.callback_query_handler(text = 'gamburger')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/17.jpg","rb"),
        caption = '''Narxi:22000 ming so'm 
Miqdorini tanlang:''',reply_markup = gamburger)
# Club mol go'shtlikdan chiqish:
@dp.callback_query_handler(text = 'ortga_40')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Burger menyusi: ",reply_markup = burger_menu)

#=============================================================================================================

# Burger tovuq go'shtlik 
@dp.callback_query_handler(text = 'chizburger')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/18.jpg","rb"),
        caption = '''Narxi:22000 ming so'm 
Miqdorini tanlang:''',reply_markup = chizburger)
#  Club tovuq go'shtlikdan chiqish:
@dp.callback_query_handler(text = 'ortga_41')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Burger menyusi: ",reply_markup = burger_menu)

#=============================================================================================================
#=============================================================================================================
#=============================================================================================================

# Ichimliklar uchun menyu:

# Ichimliklar bosganda menyu
@dp.callback_query_handler(text = 'ichimliklar')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Ichimliklar menyusi: ",reply_markup = ichimliklar_menu)

# Ichimliklar bosilganda birinchi ortga
@dp.callback_query_handler(text = 'ortga')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Marhamat menu:',reply_markup = inline_javob)
#=============================================================================================================

# Cofe va Choy menyu:
@dp.callback_query_handler(text = 'choy_kofe')
async def echo(call: CallbackQuery):
    await call.message.answer('''✅Kategoriyalardan birini tanlang!!!: ''',reply_markup = choy_kofe_menu)
# Cofe va Choy menyudan chiqish:
@dp.callback_query_handler(text = 'ortga_42')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Ichimliklar menyusi: ",reply_markup = ichimliklar_menu)

#=============================================================================================================

# Cofe menyu:
@dp.callback_query_handler(text = 'kofe')
async def echo(call: CallbackQuery):
    await call.message.answer('''✅Kategoriyalardan birini tanlang!!!: ''',reply_markup = kofe_menu)
# Cofe menyudan chiqish:
@dp.callback_query_handler(text = 'ortga_43')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Ichimliklar menyusi: ",reply_markup = ichimliklar_menu)

#=============================================================================================================

# Latte:
@dp.callback_query_handler(text = 'latte')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/21.jpg","rb"),
        caption = '''✅Latte 15000ming so'm!!!!''',reply_markup = latte)
# Lattedan chiqish:
@dp.callback_query_handler(text = 'ortga_45')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Kofe menyusi: ",reply_markup = kofe_menu)
#=============================================================================================================
# Cofe 3 v 1:
@dp.callback_query_handler(text = 'cofe_3_in_1')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/20.jpg","rb"),
        caption = '''✅Kofe 3 v 1☕️ 3000ming so'm!!!!''',reply_markup = cofe_3_in_1)
# Cofe 3 v 1 dan chiqish:
@dp.callback_query_handler(text = 'ortga_46')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Kofe menyusi: ",reply_markup = kofe_menu)
#=============================================================================================================
# Americano:
@dp.callback_query_handler(text = 'americano')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/19.jpg","rb"),
        caption = '''✅Americano narxi 12000 !!!!:''',reply_markup = americano)
# Americanodan chiqish:
@dp.callback_query_handler(text = 'ortga_44')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Kofe menyusi: ",reply_markup = kofe_menu)
#=============================================================================================================
# Cappuccino:
@dp.callback_query_handler(text = 'cappuccino')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/22.jpg","rb"),
        caption = '''✅Americano narxi 11000 !!!!:''',reply_markup = cappuccino)
# Cappuccinodan chiqish:
@dp.callback_query_handler(text = 'ortga_47')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Kofe menyusi: ",reply_markup = kofe_menu)
    
#=============================================================================================================
#=============================================================================================================

# Choy menyu:
@dp.callback_query_handler(text = 'choy')
async def echo(call: CallbackQuery):
    await call.message.answer('''✅Kategoriyalardan birini tanlang!!!: ''',reply_markup = choy_menu)
# Choy menyudan chiqish:
@dp.callback_query_handler(text = 'ortga_48')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Ichimliklar menyusi: ",reply_markup = ichimliklar_menu)

#=============================================================================================================

# Qora choy:
@dp.callback_query_handler(text = 'kuk')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/22.jpg","rb"),
        caption = '''✅Qora choy 3000 so'm !!!!:''',reply_markup = qora_choy)
# Qora choy dan chiqish:
@dp.callback_query_handler(text = 'ortga_49')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Choylar menyusi: ",reply_markup = choy_menu)

#=============================================================================================================

# Ko'k choy:
@dp.callback_query_handler(text = 'limon')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/23.jpg","rb"),
        caption = '''✅Ko'k choy 3000 so'm !!!!:''',reply_markup = kuk_choy)
# Ko'k choy dan chiqish:
@dp.callback_query_handler(text = 'ortga_50')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Choylar menyusi: ",reply_markup = choy_menu)

#=============================================================================================================

# Limon choy:
@dp.callback_query_handler(text = 'qora')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/24.jpg","rb"),
        caption = '''✅Limon choy 5000 so'm !!!!:''',reply_markup = limon_choy)
# Limon choydan chiqish:
@dp.callback_query_handler(text = 'ortga_51')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Choylar menyusi: ",reply_markup = choy_menu)


#=============================================================================================================
#=============================================================================================================

# Yaxna ichimliklar menyusi:
@dp.callback_query_handler(text = 'y_ichimliklar')
async def echo(call: CallbackQuery):
    await call.message.answer('''✅Kategoriyalardan birini tanlang!!!: ''',reply_markup = yaxna_ichimliklar_menu)
# Yaxna ichimliklardan chiqish:
@dp.callback_query_handler(text = 'ortga_52')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Ichimliklar menyusi: ",reply_markup = ichimliklar_menu)

#=============================================================================================================

# Cola:
@dp.callback_query_handler(text = 'cola')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/25.jpg","rb"),
        caption = '''✅Coca-cola: 7000 so'm !!!!:''',reply_markup = cola)
# Coladan chiqish:
@dp.callback_query_handler(text = 'ortga_53')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Yaxna ichimliklar menyusi: ",reply_markup = yaxna_ichimliklar_menu)

#=============================================================================================================

# Fanta choy:
@dp.callback_query_handler(text = 'fanta')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/26.jpg","rb"),
        caption = '''✅Fanta: 7000 so'm !!!!:''',reply_markup = fanta)
# Fantadan chiqish:
@dp.callback_query_handler(text = 'ortga_54')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Yaxna ichimliklar menyusi: ",reply_markup = yaxna_ichimliklar_menu)

#=============================================================================================================

# Sprite menu
@dp.callback_query_handler(text = 'sprite')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/27.jpg","rb"),
        caption = '''✅Sprite: 7000 so'm !!!!:''',reply_markup = sprite)
# Spritedan chiqish:
@dp.callback_query_handler(text = 'ortga_56')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Yaxna ichimliklar menyusi: ",reply_markup = yaxna_ichimliklar_menu)

#=============================================================================================================

# Nestle menu
@dp.callback_query_handler(text = 'nestle')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/28.jpg","rb"),
        caption = '''✅Nestle suvi 0.5: 4000 so'm !!!!:''',reply_markup = nestle)
# Nestledan chiqish:
@dp.callback_query_handler(text = 'ortga_55')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Yaxna ichimliklar menyusi: ",reply_markup = yaxna_ichimliklar_menu)

#=============================================================================================================
#=============================================================================================================

# Fresh va soklar menyusi:
@dp.callback_query_handler(text = 'fresh_soklar')
async def echo(call: CallbackQuery):
    await call.message.answer('''✅Kategoriyalardan birini tanlang!!!: ''',reply_markup = fresh_soklar_menu)
# Fresh va soklardan chiqish:
@dp.callback_query_handler(text = 'ortga_57')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat  Fresh va soklar menyusi: ",reply_markup = ichimliklar_menu)

#=============================================================================================================

# Bliss sok menu
@dp.callback_query_handler(text = 'bliss')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/29.jpg","rb"),
        caption = '''✅Bliss 1L 12000 so'm !!!!:''',reply_markup = bliss)
# Nestledan chiqish:
@dp.callback_query_handler(text = 'ortga_58')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat  Fresh va soklar menyusi: ",reply_markup = fresh_soklar_menu)

#=============================================================================================================

# Olma va sabzi fresh menu
@dp.callback_query_handler(text = 'fresh')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/30.jpg","rb"),
        caption = '''✅Fresh sabzi va olma 13000 so'm !!!!:''',reply_markup = fresh)
# Nestledan chiqish:
@dp.callback_query_handler(text = 'ortga_59')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat  Fresh va soklar menyusi: ",reply_markup = fresh_soklar_menu)

#=============================================================================================================
#=============================================================================================================
#=============================================================================================================

# Gazaklar menyusi:
@dp.callback_query_handler(text = 'gazaklar')
async def echo(call: CallbackQuery):
    await call.message.answer('''✅Kategoriyalardan birini tanlang!!!: ''',reply_markup = gazaklar_menu)
# Gazaklardan chiqish:
@dp.callback_query_handler(text = 'ortga')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Marhamat menu:',reply_markup = inline_javob)

#=============================================================================================================

# Fri menu
@dp.callback_query_handler(text = 'fri')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/31.jpg","rb"),
        caption = '''✅Kartoshka fri 15 gramm 7000 so'm!!!!:''',reply_markup = fri)
# Fridan chiqish:
@dp.callback_query_handler(text = 'ortga_59')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat  Gazaklar va soklar menyusi: ",reply_markup = gazaklar_menu)
#=============================================================================================================
# Kartoshka  menu
@dp.callback_query_handler(text = 'k_p_der')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/32.jpg","rb"),
        caption = '''✅Kartoshka po Derevenski 6000 so'm!!!!:''',reply_markup = kartoshka)
# Kartoshkadan chiqish:
@dp.callback_query_handler(text = 'ortga_60')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat  Gazaklar va soklar menyusi: ",reply_markup = gazaklar_menu)
#=============================================================================================================
# Guruch katta menu
@dp.callback_query_handler(text = 'guruch_katta')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/33.jpg","rb"),
        caption = '''✅Narxi:8000 ming so'm 
Miqdorini tanlang:''',reply_markup = guruch_katta)
# Guruch kattadan chiqish:
@dp.callback_query_handler(text = 'ortga_58')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat  Gazaklar va soklar menyusi: ",reply_markup = gazaklar_menu)
#=============================================================================================================
# Guruch kichik menu
@dp.callback_query_handler(text = 'guruch_kichik')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/33.jpg","rb"),
        caption = '''✅Narxi:4000 ming so'm 
Miqdorini tanlang:''',reply_markup = guruch_kichik)
# Guruch kichikdan chiqish:
@dp.callback_query_handler(text = 'ortga_57')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat  Gazaklar va soklar menyusi: ",reply_markup = gazaklar_menu)

#=============================================================================================================
#=============================================================================================================
#=============================================================================================================


# Desertlar menyusi:
@dp.callback_query_handler(text = 'gazaklar')
async def echo(call: CallbackQuery):
    await call.message.answer('''✅Kategoriyalardan birini tanlang!!!: ''',reply_markup = desertlar_menu)
# Desertlardan chiqish:
@dp.callback_query_handler(text = 'ortga')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Marhamat menu:',reply_markup = inline_javob)

#=============================================================================================================

# Asal menu
@dp.callback_query_handler(text = 'asal')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/34.jpg","rb"),
        caption = '''Narxi:14000 ming so'm 
✅Аnʼnaviy taʼm - asal asosidagi biskvit va krem
Miqdorini tanlang:''',reply_markup = asal)
# Asaldan chiqish:
@dp.callback_query_handler(text = 'ortga_64')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat  Desertlar menyusi: ",reply_markup = desertlar_menu)
#=============================================================================================================

# Shokoladli muss menu
@dp.callback_query_handler(text = 'choko')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/36.jpg","rb"),
        caption = '''Narxi:14000 ming so'm 
✅Аnʼnaviy taʼm - shokolat asosidagi biskvit va krem.
Miqdorini tanlang:''',reply_markup = shokolad)
# Shokoladli mussdan chiqish:
@dp.callback_query_handler(text = 'ortga_63')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat  Desertlar menyusi: ",reply_markup = desertlar_menu)

#=============================================================================================================

# Qulupnay menu
@dp.callback_query_handler(text = 'qulupnay')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/35.jpg","rb"),
        caption = '''Narxi:14000 ming so'm 
✅Qulupnayli Muss.
Miqdorini tanlang:''',reply_markup = qulupnay)
# Qulupnaydan chiqish:
@dp.callback_query_handler(text = 'ortga_62')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat  Desertlar menyusi: ",reply_markup = desertlar_menu)

#=============================================================================================================
#=============================================================================================================
#=============================================================================================================

# Pizzalar menyusi:
@dp.callback_query_handler(text = 'pizza')
async def echo(call: CallbackQuery):
    await call.message.answer('''✅Kategoriyalardan birini tanlang!!!: ''',reply_markup = pizzalar_menu)
# Pizzalardan chiqish:
@dp.callback_query_handler(text = 'ortga')
async def echo(call: CallbackQuery):
    await call.message.answer('✅ Marhamat menu:',reply_markup = inline_javob)

#=============================================================================================================

# Pepperoni menu
@dp.callback_query_handler(text = 'pepperoni')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/37.jpg","rb"),
        caption = '''Narxi: 65000 ming so'm 
✅Пицца Пепперони
Пицца Пепперони: 33см.
Соус Томатный Для Пиццы
Тонкое тесто.
Сыр 110 гр.
Miqdorini tanlang:''',reply_markup = pepperoni)
# Pepperonidan chiqish:
@dp.callback_query_handler(text = 'ortga_65')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat  Pizzalar menyusi: ",reply_markup = pizzalar_menu)
#=============================================================================================================

# Ananaslik Pizza menu
@dp.callback_query_handler(text = 'ananas')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/38.jpg","rb"),
        caption = '''Narxi:65000 ming so'm 
✅Пицца с Ананасом.
Пицца с Колбасой     33см.
Соус Томатный Для Пиццы
3 вида колбас 130гр.
Тонкое тесто
Кукуруза
Сыр 100гр.
Грибы
Miqdorini tanlang:''',reply_markup = ananas)
# Ananaslik Pizzadan chiqish:
@dp.callback_query_handler(text = 'ortga_66')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Pizzalar menyusi: ",reply_markup = pizzalar_menu)

#=============================================================================================================

# Margaritta menu
@dp.callback_query_handler(text = 'margarita')
async def echo(call: CallbackQuery):
    await call.message.answer_photo(
        photo = open("images/39.jpg","rb"),
        caption = '''Narxi:65000 ming so'm 
✅Пицца Маргарита
Пицца Маргарита  33см.
Соус Томатный Для Пиццы 
Тонкое тесто 
Сыр 100гр.
Помидоры
Miqdorini tanlang:''',reply_markup = margarita)
# Margarittadan chiqish:
@dp.callback_query_handler(text = 'ortga_67')
async def echo(call: CallbackQuery):
    await call.message.answer("✅Marhamat Pizzalar menyusi: ",reply_markup = pizzalar_menu)
#=============================================================================================================
#=============================================================================================================
#=============================================================================================================
# The END !!!

@dp.message_handler(text = '🇷🇺 Russkiy')
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer("Выберите Узбекский язык !!!")

@dp.message_handler(text = '🇬🇧 English')
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer("Choose Uzbek language !!!")

# @dp.message_handler()
# async def echo(message: types.Message):
#     # old style:
#     # await bot.send_message(message.chat.id, message.text)

#     await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
