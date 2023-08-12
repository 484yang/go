from flask import Flask, request, abort
 
 
from events.basic import*
from line_bot_api import*





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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    message_text = str(event.message.text).lower()

    if message_text == '@關於我們':
        about_us_event(event)

    elif message_text == '@營業據點':
        location_event(event)



@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg = """ 你好我是 歡迎你成為 XXX每架俱樂部會員 !
我是XXX美甲俱樂部 的小幫手
-想直接預約 線上美甲服務 可直接點選下方
-[你的小幫手]選單功能
    
-期待你的光臨!"""


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=welcome_msg))
    
@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)
    

if __name__ =='__main__':
    app.run()