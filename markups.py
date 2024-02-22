from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

stbtn = InlineKeyboardButton(text="Начать", callback_data='nachat')
stmenu = InlineKeyboardMarkup(row_width=1)
stmenu.insert(stbtn)

model = KeyboardButton('Сменить провайдер')
voice_type = KeyboardButton('Сменить голос')
done = KeyboardButton('Готово')
change_menu = ReplyKeyboardMarkup()
change_menu.add(model).add(voice_type).add(done)

micorsoft = KeyboardButton('Microsoft')
lovo = KeyboardButton('LovoAI')
ibm = KeyboardButton('IBM')
amazon = KeyboardButton('Amazon')
elevanlabs = KeyboardButton('ElevanLabs')
google = KeyboardButton('Google')
change_provider_menu = ReplyKeyboardMarkup()
change_provider_menu.add(micorsoft, lovo, ibm).add(amazon, elevanlabs, google)

# Голоса майкрософт
DmitryNeural = KeyboardButton('ru-RU-DmitryNeural')
DariyaNeural = KeyboardButton('ru-RU-DariyaNeural')
BrandonNeural = KeyboardButton('en-US-BrandonNeural')
AmberNeural = KeyboardButton('en-US-AmberNeural')
micorsoft_voices = ReplyKeyboardMarkup()
micorsoft_voices.add(DariyaNeural, DmitryNeural).add(BrandonNeural, AmberNeural)

# Голоса лово
LiaAbakumov = KeyboardButton('ru-RU_Lia Abakumov')
AlexeiSyomin = KeyboardButton('ru-RU_Alexei Syomin')
AustinHopkins = KeyboardButton('en-US_Austin Hopkins')
SusanCole = KeyboardButton('en-US_Susan Cole')
lovo_voices = ReplyKeyboardMarkup()
lovo_voices.add(AlexeiSyomin, LiaAbakumov).add(AustinHopkins, SusanCole)

# Голоса ibm
AllisonExpressiv = KeyboardButton('en-US_AllisonExpressive')
MichaelExpressive = KeyboardButton('en-US_MichaelExpressive')
ibm_voices = ReplyKeyboardMarkup()
ibm_voices.add(MichaelExpressive, AllisonExpressiv)

# Голоса амазон
MaximStandard = KeyboardButton('ru-RU_Maxim_Standard')
TatyanaStandard = KeyboardButton('ru-RU_Tatyana_Standard')
JoeyStandard = KeyboardButton('en-US_Joey_Standard')
IvyNeural = KeyboardButton('en-US_Ivy_Neural')
amazon_voices = ReplyKeyboardMarkup()
amazon_voices.add(MaximStandard, TatyanaStandard).add(JoeyStandard, IvyNeural)

# Голоса ElevenLabs
MonolingualClyde = KeyboardButton('en-US_Monolingual_Clyde')
MonolingualRachel = KeyboardButton('en-US_Monolingual_Rachel')
elevanlabs_voices = ReplyKeyboardMarkup()
elevanlabs_voices.add(MonolingualClyde, MonolingualRachel)

# Голоса гугл
StandardB = KeyboardButton('ru-RU-Standard-B')
StandardA = KeyboardButton('ru-RU-Standard-A')
Neural2A = KeyboardButton('en-US-Neural2-A')
Neural2G = KeyboardButton('en-US-Neural2-G')
google_voices = ReplyKeyboardMarkup()
google_voices.add(StandardB, StandardA).add(Neural2A, Neural2G)