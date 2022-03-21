from ctypes.wintypes import MSG
from typing import Text
from linebot.models import TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('{action_message}')
def get(message_request: MessageRequest):

    msg = TemplateSendMessage(
        alt_text='Actions',
        template=ButtonsTemplate(
            title='Menu',
            text='please select',
            actions=[
                MessageAction(
                    label='點我看貼圖',
                    text='{sticker}'
                )
            ]
        )
    )

    return [
        msg
    ]
