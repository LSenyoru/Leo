from audioop import add
from typing import Text
from linebot.models import TemplateSendMessage, ButtonsTemplate, LocationAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('{action_location}')
def get(message_request: MessageRequest):

    location = TemplateSendMessage(
        alt_text='Actions',
        template=ButtonsTemplate(
            title='Menu',
            text='please select',
            actions=[
                LocationAction(label='請選擇地址')
            ]
        )
    )
    return [
        location
    ]
