

from line_bot_api import *



def about_us_event(event):
    emoji = [
        {
            "index": 0,
            "productId": "5ac21184040ab15980c9b43a",
            "emojiId": "225"
        },
        {
            "index": 13,
            "productId": "5ac21184040ab15980c9b43a",
            "emojiId": "225"
        }
    ]
    text_message = TextSendMessage(text='''$ Master SPA $

指甲選購 買五送一
長短都可 加購50元 試甲片有保障
長期美裝櫃姐配合有折扣
好友推薦 請輸入 ID  。 ''' , emojis=emoji) 
    
    sticker_message = StickerSendMessage(
        package_id='6136',
        sticker_ID='10551378'
        )

    about_us_img = 'https://i.imgur.com/70A4wdI.jpg'

    image_message = ImageSendMessage(
        original_content_url = about_us_img,
        preview_image_url=about_us_img
    )

    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message, image_message])

def location_event(event):
    location_message = LocationSendMessage(
        title='Master SPA',
        address= '高雄市 中山一路',
        latitude= 22.74212324850629, 
        longitude=120.32569190569878
    )
    
    line_bot_api.reply_message(
        event.reply_token,
        location_message)
    
     