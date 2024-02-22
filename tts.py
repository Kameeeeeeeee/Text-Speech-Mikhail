import json
import requests
import config


headers = {"Authorization": f"Bearer {config.edenai_token}"}


def text_to_speech(provider, voice, text, chat_id=-19):
    payload = {"providers": provider,
           "language": voice[:5],
           "option": "MALE",
           provider: voice,
           "text": text}   

    response = requests.post(config.edenai_url, json=payload, headers=headers)
    result = json.loads(response.text)

    audio_url = result.get(provider).get('audio_resource_url')
    r = requests.get(audio_url)
    with open(f'{chat_id}.wav', 'wb') as f:
        f.write(r.content)