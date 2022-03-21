from email.mime import audio
from typing import Text
from linebot.models import TextSendMessage, AudioSendMessage, VideoSendMessage
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('{media}')
def get(message_request: MessageRequest):
    audio = AudioSendMessage(
        original_content_url='https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3',
        duration=60000
    )

    video = VideoSendMessage(
        original_content_url = 'https://image-cdn.hypb.st/https%3A%2F%2Fhk.hypebeast.com%2Ffiles%2F2021%2F08%2Fnever-gonna-give-you-up-passes-one-billion-views-01.jpg?w=960&cbr=1&q=90&fit=max',
        preview_image_url='https://image-cdn.hypb.st/https%3A%2F%2Fhk.hypebeast.com%2Ffiles%2F2021%2F08%2Fnever-gonna-give-you-up-passes-one-billion-views-01.jpg?w=960&cbr=1&q=90&fit=max'
    )


    return [
        audio,
        video
    ]
