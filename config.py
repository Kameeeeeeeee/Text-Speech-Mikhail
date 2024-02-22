edenai_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjBhNDY1MzYtNjBkZi00OWExLWIxOTQtMWU1M2FiODU4MzMxIiwidHlwZSI6ImFwaV90b2tlbiJ9.9i5jusFuJkMNnsJNJHfc5IUZyqv4ylXNFEKos0bjShA'

edenai_url = 'https://api.edenai.run/v2/audio/text_to_speech'

tg_token = '6542444338:AAHUREUNnol_-pKp21phAL2ZSfKy0RKujjQ'

messages = {'start': 'Привет! Этот бот поможет тебе синтезировать текст в речь',
            'help' : 'Команды:\n/start - начальное сообщение',
            'input' : 'Введите текст, который хотите синтезировать',
            'tts' : ['Синтезируем, пожалуйста подождите', 'Готово!', 'Что-то пошло не так, повторите попытку позже, или смените голос'],
            'ready' : 'Начать синтез речи?',
            'change_provider' : ['Выберите провайдер', 'Провайдер изменен, учтите, что для каждого провайдера есть свои голоса озвучки'],
            'change_voice' : ['Выберите голос озвучки', 'Голос установлен'],
            'set_voice' : 'Голос изменен',
            'error' : 'НЕОПОЗНАННАЯ КОМАНДА! Пожалуйста пользуйтесь кнопками навигации'
}

default_voices = {'microsoft' : 'ru-RU-DmitryNeural',
                  'lovoai' : 'ru-RU_Lia Abakumov',
                  'ibm' : 'en-US_AllisonExpressive',
                  'amazon' : 'ru-RU_Maxim_Standard',
                  'elevanlabs' : 'en-US_Monolingual_Clyde',
                  'google' : 'ru-RU-Standard-B'}