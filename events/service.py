from line_bot_api import *
from urllib.parse import parse_qsl
import datetime

from extensions import db
from models.user import User
from models.reservation import Reservation

services = {
    1: {
        'category': '美甲單色',
        'img_url': 'https://drive.google.com/uc?export=download&id=15ftd3m_rOX3Op_js9B5OCiz2a4KyQfXi',
        'title': '按摩調理（指壓／精油）',
        'duration': '90min',
        'description': '深層肌肉緊繃痠痛、工作壓力和緊繃情緒、身體疲勞者，想解除肌肉緊繃僵硬不適感',
        'price': 2000,
        'post_url': 'https://linecorp.com'
    },
    2: {
        'category': '美甲單色',
        'img_url': 'https://drive.google.com/uc?export=download&id=1naYV7ySDy1PBTR9_smzchSu3xPfuKRYO',
        'title': '運動按摩（按摩與伸展）',
        'duration': '90min',
        'description': '全身肌肉按摩放鬆與伸展，能夠改善運動後引發的延遲性痠痛，血液循環流通順暢',
        'price': 1500,
        'post_url': 'https://linecorp.com'
    },
    3: {
        'category': '美甲單色',
        'img_url': 'https://drive.google.com/uc?export=download&id=1dOiR8rnSski88B7s8tEClN6bR4OXP2VY',
        'title': '熱石精油紓壓',
        'duration': '90min',
        'description': '「火山石」成份含有豐富礦物質及獨特的自然能量，溫熱觸感能活絡循環，鬆解疲勞感，舒緩肌肉緊繃',
        'price': 2000,
        'post_url': 'https://linecorp.com'
    },
    4: {
        'category': '美甲單色',
        'img_url': 'https://drive.google.com/uc?export=download&id=1j9k2ivv1D3DwthQABmiI-PLsn6pN7sIZ',
        'title': '粉刺淨化 + 深層保濕',
        'duration': '90min',
        'description': '臉部淨化，粉刺淨化 + 深層保濕繃',
        'price': 1500,
        'post_url': 'https://linecorp.com'
    },
}


def service_category_event(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text='請選擇想服務類別',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/okeVTFf.jpg',
                    action=PostbackAction(
                        label='美甲單色',
                        display_text='想了解美甲單色',
                        data= 'action=service&category=美甲單色'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/okeVTFf.jpg',
                    action=PostbackAction(
                        label='美甲單色',
                        display_text='想了解美甲單色',
                        data= 'action=service&category=美甲單色'
                    )
                )
            ]
        )
    ) 

    line_bot_api.reply_message(
        event.reply_token,
        [image_carousel_template_message])




def service_event(event):
    #底下三個要等上面的service建立後才寫,主要是要跑service的服務
    #data = dict(parse_qsl(event.postback.data))
    #bubbles = []
    #for service_id in services:
    data = dict(parse_qsl(event.postback.data))

    bubbles = []

    for service_id in services:
        if services[service_id]['category'] == data['category']:
            service = services[service_id]
            bubble = {
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
          "type": "carousel",
          "contents": bubbles
        }
    )

    line_bot_api.reply_message(
        event.reply_token,
        [flex_message])

