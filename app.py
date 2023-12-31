from flask import Flask, request, abort
 
from events.service import *
from events.basic import*
from line_bot_api import*

from extensions import db,migrate
from models.user import User

import os
from events.admin import *

app = Flask(__name__)


app.config.from_object(os.environ.get('APP_SETTINGS', 'config.DevConfig'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gogo:IvhCW21qkB278n6ReG9Ri7erdnl8Y6rz@dpg-cjg2kr41ja0c739p5udg-a.singapore-postgres.render.com/aiai'
db.app = app
db.init_app(app)
migrate.init_app(app,db)





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
    user = User.query.filter(User.line_id == event.source.user_id).first()
    if not user:
        profile = line_bot_api.get_profile(event.source.user_id)
        print(profile.display_name)
        print(profile.user_id)
        print(profile.picture_url)

        user = User(profile.user_id, profile.display_name, profile.picture_url)
        db.session.add(user)
        db.session.commit()
    
    print(user.id)
    print(user.line_id)
    print(user.display_name)


    if message_text == '@關於我們':
        about_us_event(event)

    elif message_text == '@營業據點':
        location_event(event)

    elif message_text == '@預約服務':
        service_category_event(event)
    elif message_text.startswith('*'):
        if event.source.user_id not in ['Uf391a9922d5c19a5fc1997615f8af01d']:
            return
        if message_text in ['*data','*d']:
            list_reservation_event(event)
    #   elif message_text in ['*group','*g']:
          #  create_audience_group(event)


@handler.add(PostbackEvent)
def handle_postback(event):
    data = dict(parse_qsl(event.postback.data))

    if data.get('action') == 'service':
        service_event(event)
    elif data.get('action') == 'select_date':
        service_select_date_event(event)
    elif data.get('action') == 'select_time':
        service_select_time_event(event)
    elif data.get('action') == 'confirm':
        service_confirm_event(event)
    elif data.get('action') == 'confirmed':
        service_confirmed_event(event)
    elif data.get('action') == 'cancel':
        service_cancel_event(event)


 #   print('action', data.get('action'))
 #   print('category', data.get('category'))
 #   print('service_id', data.get('service_id'))
 #   print('data', data.get('data'))
 #   print('time', data.get('time')) 
  


@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg = """ 你好我是 歡迎你成為 享甲樂俱樂部會員 !
我是享甲樂美甲俱樂部 的小幫手
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