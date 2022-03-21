from lzma import FORMAT_ALONE
from typing import Text
from anyio import CapacityLimiterStatistics
from linebot.models import TemplateSendMessage, ButtonsTemplate
from linebot.models.actions import CameraAction, CameraRollAction
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('{action_camara}')
def get(message_request: MessageRequest):

    camara = TemplateSendMessage(
        alt_text='Actions',
        template=ButtonsTemplate(
            title='Menu',
            text='相片選擇器',
            actions=[
                CameraAction(label='開啟相機'),
                CameraRollAction(label='開啟相簿')
            ]
        )
    )
    return [
        camara
    ]
