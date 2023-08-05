from flask import Flask, request, abort

# from events.basic import*
# from line_bot_api import*



from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, StickerSendMessage, ImageSendMessage, LocationSendMessage
)

#Channel access token
line_bot_api = LineBotApi ('UgMewg7JZ2k2AIOmQpUtjZmPFpcUXcZKlCGrpnFeZCSI0qksZ/emxXHPXpRNhMA1oW+yxTlgf/vbRGW9UwIQ1Zfz6vn08MhwMy4SPZ6IIm7er1fXswofmsN+hZNJDvgDftUeYPIpNA1WuJWqRVTFBgdB04t89/1O/w1cDnyilFU=')

#Channel secret
handler = WebhookHandler ('29b000701b7fd5e56d1c9a0c8241b3f0')

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)

    app.logger.info('Request body:' + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print('Invalid signature. please check your channel access token/channel secret.')
        abort(400)

    return 'OK'