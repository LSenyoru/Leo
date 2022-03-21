from typing import Text
from linebot.models import TemplateSendMessage, ButtonsTemplate
from linebot.models.actions import PostbackAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('{action_postback}')
def get(message_request: MessageRequest):

    msg = TemplateSendMessage(
        alt_text='Actions',
        template=ButtonsTemplate(
            title='Menu',
            text='please select',
            actions=[
                PostbackAction(label="test", data="1@2@3")
            ]
        )
    )
    return [
        msg
    ]
