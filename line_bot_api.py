from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, StickerSendMessage, ImageSendMessage, LocationSendMessage,
    FlexSendMessage,TemplateSendMessage,ImageCarouselTemplate,PostbackAction,ImageCarouselColumn,PostbackEvent, QuickReplyButton,QuickReply

)

#Channel access token
line_bot_api = LineBotApi ('UgMewg7JZ2k2AIOmQpUtjZmPFpcUXcZKlCGrpnFeZCSI0qksZ/emxXHPXpRNhMA1oW+yxTlgf/vbRGW9UwIQ1Zfz6vn08MhwMy4SPZ6IIm7er1fXswofmsN+hZNJDvgDftUeYPIpNA1WuJWqRVTFBgdB04t89/1O/w1cDnyilFU=')
#UgMewg7JZ2k2AIOmQpUtjZmPFpcUXcZKlCGrpnFeZCSI0qksZ/emxXHPXpRNhMA1oW+yxTlgf/vbRGW9UwIQ1Zfz6vn08MhwMy4SPZ6IIm7er1fXswofmsN+hZNJDvgDftUeYPIpNA1WuJWqRVTFBgdB04t89/1O/w1cDnyilFU=
#Channel secret
handler = WebhookHandler ('29b000701b7fd5e56d1c9a0c8241b3f0')
#29b000701b7fd5e56d1c9a0c8241b3f0