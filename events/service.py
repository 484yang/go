from line_bot_api import *
from urllib.parse import parse_qsl

services = {


    1:{
        'category':'美甲單色',
        'img_url':'https://i.imgur.com/okeVTFf.jpg',
        'title' : 'sdf' ,
        'duration' : 'sdf',
        'description' : 'sdf',
        'price':550,
        'post_url': 'asd',
    },

    1:{
        'category':'美甲單色',
        'img_url':'https://i.imgur.com/okeVTFf.jpg',
        'title' : 'sdf' ,
        'duration' : 'sdf',
        'description' : 'sdf',
        'price':550,
        'post_url': 'asd',
    },



}



def service_category_event(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text='請選擇想服務類別',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselTemplate(
                    image_url='https://i.imgur.com/okeVTFf.jpg',
                    action=PostbackAction(
                        label='按摩調理',
                        display_text='想了解按摩調理',
                        data= 'action=service&category=按摩調理'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/okeVTFf.jpg',
                    action=PostbackAction(
                        label='按摩調理',
                        display_text='想了解按摩調理',
                        data= 'action=service&category=按摩調理'
                    )
                )
            ]
        )
    ) 

    line_bot_api.reply_message(
        event.reply_token,
        [image_carousel_template_message])





def service_event(event):
      
    data = dict(parse_qsl(event.postback.data))

    bubble = []

    for service_id in services:
        if services[service_id]['category'] == data['category']:
            service = services[service_id]
            bubbles = {
                "type": "bubble",
                "hero": {
                "type": "image",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "url": service['img_url']
                },
                "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                    "type": "text",
                    "text": service['title'],
                    "wrap": True,
                    "weight": "bold",
                    "size": "xl"
                    },
                    {
                    "type": "text",
                    "text": service['duration'],
                    "size": "md",
                    "weight": "bold"
                    },
                    {
                    "type": "text",
                    "text": service['description'],
                    "margin": "lg",
                    "wrap": True
                    },
                    {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                        "type": "text",
                        "text": f"NT$ {service['price']}",
                        "wrap": True,
                        "weight": "bold",
                        "size": "xl",
                        "flex": 0
                        }
                    ],
                    "margin": "xl"
                    }
                ]
                },
                "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                    "type": "button",
                    "style": "primary",
                    "action": {
                        "type": "postback",
                        "label": "預約",
                        "data": f"action=select_date&service_id={service_id}",
                        "displayText": f"我想預約【{service['title']} {service['duration']}】"
                    },
                    "color": "#b28530"
                    },
                    {
                    "type": "button",
                    "action": {
                        "type": "uri",
                        "label": "了解詳情",
                        "uri": service['post_url']
                    }
                    }
                ]
                }
            }

            bubbles.append(bubble)

    flex_message = FlexSendMessage(
            alt_text='請選擇預約項目',
            contents={
                "type":"carousel",
                "contents": bubbles
            }
    )  


