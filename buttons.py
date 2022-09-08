from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
# bu til uchun
til = ReplyKeyboardMarkup(
	keyboard = [
	[
		KeyboardButton(text = "🇺🇿 O'zbekcha"),
		KeyboardButton(text = '🇷🇺 Russkiy'),
		KeyboardButton(text = '🇬🇧 English')
		],
	],
	resize_keyboard = True
)
# Bu pastki menu uchun
javob = ReplyKeyboardMarkup(
	keyboard = [
	[
		KeyboardButton(text = '🥗 Buyurtma berish:')
	],
	[
		
		KeyboardButton(text = '⚙️ Sozlamalar'),
		KeyboardButton(text = '📞 Biz bilan bog\'lanish')

		],
	],
	resize_keyboard = True
)
# inline menu uchun
inline_javob = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🫔 Lavash 🫔',callback_data='lavash'),
		InlineKeyboardButton(text = '🌭 Hot-Dog 🌭',callback_data='hot-dog')
	],
	[
		InlineKeyboardButton(text = '🥪 Sendwich-club 🥪',callback_data='sendwich-club'),
		InlineKeyboardButton(text = '🌮 Shaurma 🌮',callback_data='shaurma')
	],
	[
		InlineKeyboardButton(text = '🍔 Burger 🍔',callback_data='burger'),
		InlineKeyboardButton(text = '🥙 Donar 🥙',callback_data='donar')
	],
	[
		
		InlineKeyboardButton(text = '🍟 Gazaklar 🍟',callback_data='gazaklar'),
		InlineKeyboardButton(text = '🥤☕️ Ichimliklar 🥤☕️',callback_data='ichimliklar')
	],
	[
		
		InlineKeyboardButton(text = '🍰 Desertlar 🍰',callback_data='desert'),
		InlineKeyboardButton(text = '🍕Pizza 🍕',callback_data='pizza')
	],
	],	
)

# lavashni bosganda menyu
#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
lavash_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🥩 Mol go\'shti 🥩',callback_data='mol-goshtlik'),
		InlineKeyboardButton(text = '🥩🌶 Qalampirli mol go\'shti 🥩🌶',callback_data='qmolgoshtlik')
	],
	[
		
		InlineKeyboardButton(text = '🍗 Tovuq go\'shti 🍗',callback_data='tovuqli'),
		InlineKeyboardButton(text = '🍗🌶 Qalampirli Tovuq go\'shti 🍗🌶',callback_data='qtovuqli')

	],
	[
		InlineKeyboardButton(text = '🥬🥚 Fitter 🥬🥚',callback_data = 'fitter')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data = 'ortga')
	],
	],
	
)
#lavash_mol_gushtlik_menu uchun
#=========================================================================================================
lavash_mol_gushtlik_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🤏🤏 Mini 🤏🤏',callback_data='mini'),
		InlineKeyboardButton(text = '🤏🤏 Klassik 🤏🤏',callback_data='klassik')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_2'),
	],
	]
	
)
# mini uchun raqamlar
lavash_mol_gushtli_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_3'),
	],
	],
	
)
# klassik uchun raqamlar
lavash_mol_gushtli_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_4'),
	],
	],
	
)
#=========================================================================================================
#lavash_tovuq_gushtlik_menu uchun
lavash_tovuq_gushtlik_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🤏🤏 Mini 🤏🤏',callback_data='mini1'),
		InlineKeyboardButton(text = '🤏🤏 Klassik 🤏🤏',callback_data='klassik1')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_5'),
	],
	]
	
)
# lavash tovuq go'shtlik mini
lavash_tovuq_gushtli_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_6'),
	],
	],
	
)
# lavash tovuq go'shtlik klassik
lavash_tovuq_gushtli_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_7'),
	],
	],
	
)

#=========================================================================================================
lavash_mol_qalampir_gushtlik_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🤏🤏 Mini 🤏🤏',callback_data='mini2'),
		InlineKeyboardButton(text = '🤏🤏 Klassik 🤏🤏',callback_data='klassik2')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_8'),
	],
	]
	
)

lavash_qalampir_mol_gushtli_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_9'),
	],
	],
	
)
# lavash qalampir mol go'shtlik klassik
lavash_qalampir_mol_gushtli_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_10'),
	],
	],
	
)

#=========================================================================================================
# Lavash qalampir tovuq go'shtlik menu
lavash_qalampir_tovuq_gushtlik_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🤏🤏 Mini 🤏🤏',callback_data='mini3'),
		InlineKeyboardButton(text = '🤏🤏 Klassik 🤏🤏',callback_data='klassik3')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_11'),
	],
	]
	
)
# Lavash qalampir tovuq mini
lavash_qalampir_tovuq_gushtli_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_12'),
	],
	],
	
)
# lavash qalampir mol go'shtlik klassik
lavash_qalampir_tovuq_gushtli_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_13'),
	],
	],
	
)

fitter = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_19'),
	],
	],
	
)










#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
# Hot-Dog Menu
hot_dog_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🌭 Hot-dog baget dabl 🌭',callback_data='double'),
		InlineKeyboardButton(text = '🌭 Classic Hot-dog 🌭',callback_data='classic')
	],
	[
		
		InlineKeyboardButton(text = '🍗 Tovuqli Hot-dog 🍗',callback_data='hot_dog_tovuqli'),
		InlineKeyboardButton(text = '🔱🌭 Korolevskiy Hot-dog 🔱🌭',callback_data='korolevskiy')

	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data = 'ortga')
	],
	],
)
# Hot-Dog Classic
Hot_dog_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_15'),
	],
	],
	
)
# Hot-Dog Dabl
Hot_dog_dabl = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_16'),
	],
	],
	
)
# Hot-Dog Korolevskiy
Hot_dog_korolevskiy = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_17'),
	],
	],
	
)
# Hot-Dog Tovuqli
Hot_dog_tovuqli = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_18'),
	],
	],
	
)
#=========================================================================================================
#=========================================================================================================
#=========================================================================================================

donar_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🍗 Tovuq-go\'shtlik 🍗',callback_data='tdonar'),
		InlineKeyboardButton(text = '🥩 Mol-goshtlik 🥩',callback_data='mdonar')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_20'),
	],
	]
	
)
# Donar tovuq go'shtli
Donar_tovuqli = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_21'),
	],
	],
	
)
# Donar mol go'shtli
Donar_mol_gushtli = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_22'),
	],
	],
	
)

#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
# Club sendwich uchun menyu
club_sendwich_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🍗 Tovuqli Club-Sendwich 🍗',callback_data='club_t'),
		InlineKeyboardButton(text = '🥩 Classic Club-Sendwich 🥩',callback_data='club_c')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_23'),
	],
	]
	
)
# Club tovuq go'shtli
Club_tovuqli = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_24'),
	],
	],
	
)
# Club mol go'shtli
Club_classic = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_25'),
	],
	],
	
)
#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
# Shaurma bosganda menyu:
shaurma_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🥩 Mol go\'shti 🥩',callback_data='shaurma_mol-goshtlik'),
		InlineKeyboardButton(text = '🥩🌶 Qalampirli mol go\'shti 🥩🌶',callback_data='shaurma_qmolgoshtlik')
	],
	[
		
		InlineKeyboardButton(text = '🍗 Tovuq go\'shti 🍗',callback_data='shaurma_tovuqli'),
		InlineKeyboardButton(text = '🍗🌶 Qalampirli Tovuq go\'shti 🍗🌶',callback_data='shaurma_qtovuqli')

	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data = 'ortga')
	],
	],
	
)
#shaurma_mol_gushtlik_menu uchun
#=========================================================================================================
shaurma_mol_gushtlik_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🤏🤏 Mini 🤏🤏',callback_data='shaurma_mini'),
		InlineKeyboardButton(text = '🤏🤏 Klassik 🤏🤏',callback_data='shaurma_klassik')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_26'),
	],
	]
	
)
# mini uchun raqamlar
shaurma_mol_gushtli_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_27'),
	],
	],
	
)
# klassik uchun raqamlar
shaurma_mol_gushtli_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_28'),
	],
	],
	
)
#=========================================================================================================
#shaurma_tovuq_gushtlik_menu uchun
shaurma_tovuq_gushtlik_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🤏🤏 Mini 🤏🤏',callback_data='shaurma_mini1'),
		InlineKeyboardButton(text = '🤏🤏 Klassik 🤏🤏',callback_data='shaurma_klassik1')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_29'),
	],
	]
	
)
# Shaurma tovuq go'shtlik mini
shaurma_tovuq_gushtli_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga ↩️',callback_data='ortga_30'),
	],
	],
	
)
# Shaurma tovuq go'shtlik klassik
shaurma_tovuq_gushtli_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_31'),
	],
	],
	
)

#=========================================================================================================
shaurma_qalampir_mol_gushtlik_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🤏🤏 Mini 🤏🤏',callback_data='shaurma_mini2'),
		InlineKeyboardButton(text = '🤏🤏 Klassik 🤏🤏',callback_data='shaurma_klassik2')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_33'),
	],
	]
	
)

shaurma_qalampir_mol_gushtli_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_34'),
	],
	],
	
)
# Shaurma qalampir mol go'shtlik klassik
shaurma_qalampir_mol_gushtli_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_35'),
	],
	],
	
)

#=========================================================================================================
# Shaurma_ qalampir tovuq go'shtlik menu
shaurma_qalampir_tovuq_gushtlik_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🤏🤏 Mini 🤏🤏',callback_data='shaurma_mini3'),
		InlineKeyboardButton(text = '🤏🤏 Klassik 🤏🤏',callback_data='shaurma_klassik3')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_36'),
	],
	]
	
)
# Shaurma qalampir tovuq mini
shaurma_qalampir_tovuq_gushtli_mini = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_37'),
	],
	],
	
)
# shaurma qalampir mol go'shtlik klassik
shaurma_qalampir_tovuq_gushtli_klassik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_38'),
	],
	],
	
)

#=========================================================================================================
#=========================================================================================================
#=========================================================================================================

# Burger sendwich uchun menyu
burger_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🍔🧈 Gamburger 🍔🧈',callback_data='gamburger'),
		InlineKeyboardButton(text = '🧀🍔 Chizburger 🧀🍔',callback_data='chizburger')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga'),
	],
	]
	
)
# Burger tovuq go'shtli
gamburger = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_40'),
	],
	],
	
)
# Burger mol go'shtli
chizburger = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_41'),
	],
	],
	
)
#=========================================================================================================
#=========================================================================================================
#=========================================================================================================

ichimliklar_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🍮 Choy va kofe 🍮',callback_data='choy_kofe'),
		InlineKeyboardButton(text = '🥤🧊 Yaxna ichimliklar 🥤🧊',callback_data='y_ichimliklar')
	],
	[
		
		InlineKeyboardButton(text = '🍹 Fresh va tabiiy soklar 🍹',callback_data='fresh_soklar')

	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data = 'ortga')

	],
	]
)
#=========================================================================================================
# Choy kofe menu:
choy_kofe_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🍮 Choy 🍮',callback_data='choy'),
		InlineKeyboardButton(text = '🍮 Kofe 🍮',callback_data='kofe')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_42'),
	],
	]
	
)
#=========================================================================================================
kofe_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🍮 Americano',callback_data='americano'),
		InlineKeyboardButton(text = ' 🍮 Latte 🍮',callback_data='latte')
	],
	[
		InlineKeyboardButton(text = '🍮 Cappuccino 🍮',callback_data='cappuccino'),
		InlineKeyboardButton(text = '🍮 Kofe 3 v 1 🍮',callback_data='cofe_3_in_1')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_43'),
	],
	]
	
)
#=========================================================================================================
# Americano
americano = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_44'),
	],
	],
	
)
#=========================================================================================================
# Latte
latte = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_45'),
	],
	],
	
)
#=========================================================================================================
# Cofe 3 v 1 
cofe_3_in_1 = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_46'),
	],
	],
	
)
#=========================================================================================================
# Cappuccino 
cappuccino = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_47'),
	],
	],
	
)
#=========================================================================================================
choy_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = "👍 Ko'k choy 👍",callback_data='kuk'),
		InlineKeyboardButton(text = '👍 Qora choy 👍',callback_data='qora')
	],
	[
		InlineKeyboardButton(text = '👍 Limon choy 👍',callback_data='limon'),
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_48'),
	],
	]
	
)
#=========================================================================================================
qora_choy = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_49'),
	],
	],
	
)
#=========================================================================================================
kuk_choy = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_50'),
	],
	],
	
)
#=========================================================================================================
limon_choy = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_51'),
	],
	],
	
)

#=========================================================================================================
#=========================================================================================================
# Yaxna ichimliklar menyusi:
yaxna_ichimliklar_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🥤🧊 Coca-cola 🥤🧊',callback_data='cola'),
		InlineKeyboardButton(text = '🥤🧊 Fanta 🥤🧊',callback_data='fanta')
	],
	[
		InlineKeyboardButton(text = '🥤🧊 Sprite 🥤🧊',callback_data='sprite'),
		InlineKeyboardButton(text = '🥤🧊 Nestle 🥤🧊',callback_data='nestle')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_52'),
	],
	]
	
)
#=========================================================================================================
cola = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_53'),
	],
	],
	
)

#=========================================================================================================
fanta = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_54'),
	],
	],
	
)

#=========================================================================================================
nestle = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_55'),
	],
	],
	
)

#=========================================================================================================
sprite = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_56'),
	],
	],
	
)
#=========================================================================================================
#=========================================================================================================
# Bliss sok va freshlar uchun menyu
fresh_soklar_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🍊🍏 Bliss 🍊🍏',callback_data='bliss'),
		InlineKeyboardButton(text = '🍋🍇 Fresh 🍋🍇',callback_data='fresh')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_57'),
	],
	]
	
)
#=========================================================================================================
# Bliss
bliss = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_58'),
	],
	],
	
)
#=========================================================================================================
# Fresh soklari
fresh = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_59'),
	],
	],
	
)

#=========================================================================================================
#=========================================================================================================
#=========================================================================================================
# Gazaklar
gazaklar_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🍟 15 gram Fri 🍟',callback_data='fri'),
		InlineKeyboardButton(text = '🥔 Kartoshka po Derevenski 🥔',callback_data='k_p_der')
	],
	[
		InlineKeyboardButton(text = '🍚 Guruch katta 🍚',callback_data='guruch_katta'),
		InlineKeyboardButton(text = '🍚 Guruch kichik 🍚',callback_data='guruch_kichik')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_56'),
	],
	]
	
)
#=========================================================================================================
guruch_kichik = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_57'),
	],
	],
	
)
#=========================================================================================================
guruch_katta = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_58'),
	],
	],
	
)
#=========================================================================================================
fri = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_59'),
	],
	],
	
)
#=========================================================================================================
kartoshka = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_60'),
	],
	],
	
)

#=========================================================================================================
#=========================================================================================================
#=========================================================================================================

desertlar_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🍯 Asal 🍯',callback_data='asal'),
		InlineKeyboardButton(text = '🍫 Shokolad 🍫',callback_data='choko')
	],
	[
		InlineKeyboardButton(text = '🍓 Qulupnay 🍓',callback_data='qulupnay'),
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_61'),
	],
	]
	
)
#=========================================================================================================

qulupnay = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_62'),
	],
	],
	
)
#=========================================================================================================

shokolad = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_63'),
	],
	],
	
)

#=========================================================================================================

asal = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_64'),
	],
	],
	
)

#=========================================================================================================
#=========================================================================================================
#=========================================================================================================

pizzalar_menu = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '🍕🧀 Pepperoni 🧀🍕',callback_data='pepperoni'),
		InlineKeyboardButton(text = '🍕🍍  Ananaslik Pizza  🍍🍕',callback_data='ananas')
	],
	[
		InlineKeyboardButton(text = '🍕🍅 Margarita 🍅🍕',callback_data='margarita'),
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga'),
	],
	]
	
)
#=========================================================================================================

pepperoni = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_65'),
	],
	],
	
)
#=========================================================================================================

ananas = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_66'),
	],
	],
	
)

#=========================================================================================================

margarita = InlineKeyboardMarkup(
	inline_keyboard = [
	[
		InlineKeyboardButton(text = '1️⃣',callback_data='1'),
		InlineKeyboardButton(text = '2️⃣',callback_data='2'),
		InlineKeyboardButton(text = '3️⃣',callback_data='3')
	],
	[
		InlineKeyboardButton(text = '4️⃣',callback_data='4'),
		InlineKeyboardButton(text = '5️⃣',callback_data='5'),
		InlineKeyboardButton(text = '6️⃣',callback_data='6')
	],
	[
		InlineKeyboardButton(text = '7️⃣',callback_data='7'),
		InlineKeyboardButton(text = '8️⃣',callback_data='8'),
		InlineKeyboardButton(text = '9️⃣',callback_data='9')
	],
	[
		InlineKeyboardButton(text = '↩️ Ortga',callback_data='ortga_67'),
	],
	],
	
)