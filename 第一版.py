#!/usr/bin/env python
# coding: utf-8
# sdfsddsdsd
# In[ ]:


#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('QdnxdzUpW3bG3IekkGkys2bKehjP46GR3pABHDgqz0oFVcIkVNYjYaadWnbI1vpyv+CzYjTGOavX2eFBXVCixm4TxrGVul2RZlVg0/m9hZZ5s2rqbZa+iq/nm9lMxyiYfu6NpLC4W8g7D2v+3FOFKAdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('1d52764ed6d474557dd6b589adecddac')

line_bot_api.push_message('Uc148f9785af67639ec3b4581f49bab47', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# In[31]:


import pandas as pd


# In[32]:


test = pd.read_csv('test.csv')


# In[33]:


name = []
for i in test['品項']:
    for j in range(len(i)):
        if i[j] == '(':
            name.append(i[:j])
        elif i[j] == '（':
            name.append(i[:j])
kcal = []
for i in test['熱量(kcal)']:
    kcal.append(i)

category = []
for i in test['分類']:
    category.append(i)

menu = []
for i in range(len(name)):
    menu.append([name[i], int(kcal[i]), category[i]])


# In[34]:


category_lst = []
for i in category:
    if i not in category_lst:
        category_lst.append(i)


# In[ ]:

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    for i in menu:
        if re.match('黑胡椒麵',message):
            reply = '您選的餐點是 黑胡椒麵，這項餐點的熱量為 474 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蘑菇麵',message):
            reply = '您選的餐點是 蘑菇麵，這項餐點的熱量為 453 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蘑菇麵加蛋',message):
            reply = '您選的餐點是 蘑菇麵加蛋，這項餐點的熱量為 596 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('黑胡椒麵加蛋',message):
            reply = '您選的餐點是 黑胡椒麵加蛋，這項餐點的熱量為 575 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('醬燒沙茶麵加蛋',message):
            reply = '您選的餐點是 醬燒沙茶麵加蛋，這項餐點的熱量為 617 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('宮保雞丁麵加蛋',message):
            reply = '您選的餐點是 宮保雞丁麵加蛋，這項餐點的熱量為 505 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('三杯雞丁麵加蛋',message):
            reply = '您選的餐點是 三杯雞丁麵加蛋，這項餐點的熱量為 529 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('麻油雞麵加蛋',message):
            reply = '您選的餐點是 麻油雞麵加蛋，這項餐點的熱量為 560 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('鍋燒意麵',message):
            reply = '您選的餐點是 鍋燒意麵，這項餐點的熱量為 467 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('醡醬麵',message):
            reply = '您選的餐點是 醡醬麵，這項餐點的熱量為 434 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('餛飩麵',message):
            reply = '您選的餐點是 餛飩麵，這項餐點的熱量為 483 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('榨菜肉絲麵',message):
            reply = '您選的餐點是 榨菜肉絲麵，這項餐點的熱量為 356 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('雞絲麵',message):
            reply = '您選的餐點是 雞絲麵，這項餐點的熱量為 335 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('豬肉鍋燒麵',message):
            reply = '您選的餐點是 豬肉鍋燒麵，這項餐點的熱量為 480 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蝦仁炒麵',message):
            reply = '您選的餐點是 蝦仁炒麵，這項餐點的熱量為 620 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('羊肉麵',message):
            reply = '您選的餐點是 羊肉麵，這項餐點的熱量為 715 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('香菇雞麵 ',message):
            reply = '您選的餐點是 香菇雞麵 ，這項餐點的熱量為 373 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('傳統涼麵',message):
            reply = '您選的餐點是 傳統涼麵，這項餐點的熱量為 230 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('四物雞湯麵 ',message):
            reply = '您選的餐點是 四物雞湯麵 ，這項餐點的熱量為 396 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('叉燒麵 ',message):
            reply = '您選的餐點是 叉燒麵 ，這項餐點的熱量為 301 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('牛肉麵',message):
            reply = '您選的餐點是 牛肉麵，這項餐點的熱量為 580 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('大腸蚵仔麵線',message):
            reply = '您選的餐點是 大腸蚵仔麵線，這項餐點的熱量為 447 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('絲瓜蚌麵 ',message):
            reply = '您選的餐點是 絲瓜蚌麵 ，這項餐點的熱量為 388 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('草莓乳酪餅 ',message):
            reply = '您選的餐點是 草莓乳酪餅 ，這項餐點的熱量為 304 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('巧克力乳酪餅 ',message):
            reply = '您選的餐點是 巧克力乳酪餅 ，這項餐點的熱量為 369 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('奶油乳酪餅',message):
            reply = '您選的餐點是 奶油乳酪餅，這項餐點的熱量為 389 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('奶酥乳酪餅 ',message):
            reply = '您選的餐點是 奶酥乳酪餅 ，這項餐點的熱量為 384 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('花生乳酪餅 ',message):
            reply = '您選的餐點是 花生乳酪餅 ，這項餐點的熱量為 380 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('起司高鈣乳酪餅',message):
            reply = '您選的餐點是 起司高鈣乳酪餅，這項餐點的熱量為 440 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('火腿高鈣乳酪餅 ',message):
            reply = '您選的餐點是 火腿高鈣乳酪餅 ，這項餐點的熱量為 421 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('培根高鈣乳酪餅 ',message):
            reply = '您選的餐點是 培根高鈣乳酪餅 ，這項餐點的熱量為 500 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('滿福高鈣乳酪餅 ',message):
            reply = '您選的餐點是 滿福高鈣乳酪餅 ，這項餐點的熱量為 509 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('熱狗高鈣乳酪餅 ',message):
            reply = '您選的餐點是 熱狗高鈣乳酪餅 ，這項餐點的熱量為 480 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('原味抓餅 ',message):
            reply = '您選的餐點是 原味抓餅 ，這項餐點的熱量為 398 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蔥蛋抓餅 ',message):
            reply = '您選的餐點是 蔥蛋抓餅 ，這項餐點的熱量為 479 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('起司蛋抓餅 ',message):
            reply = '您選的餐點是 起司蛋抓餅 ，這項餐點的熱量為 541 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('培根蛋抓餅 ',message):
            reply = '您選的餐點是 培根蛋抓餅 ，這項餐點的熱量為 538 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('火腿蛋抓餅',message):
            reply = '您選的餐點是 火腿蛋抓餅，這項餐點的熱量為 521 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蔬菜蛋抓餅',message):
            reply = '您選的餐點是 蔬菜蛋抓餅，這項餐點的熱量為 488 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('滿福蛋抓餅',message):
            reply = '您選的餐點是 滿福蛋抓餅，這項餐點的熱量為 564 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('里肌蛋抓餅 ',message):
            reply = '您選的餐點是 里肌蛋抓餅 ，這項餐點的熱量為 561 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('鮪魚鬆餅 ',message):
            reply = '您選的餐點是 鮪魚鬆餅 ，這項餐點的熱量為 394 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('鮮奶油鬆餅 ',message):
            reply = '您選的餐點是 鮮奶油鬆餅 ，這項餐點的熱量為 430 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蜂蜜鬆餅 ',message):
            reply = '您選的餐點是 蜂蜜鬆餅 ，這項餐點的熱量為 438 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('花生鬆餅 ',message):
            reply = '您選的餐點是 花生鬆餅 ，這項餐點的熱量為 565 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('草莓鬆餅 ',message):
            reply = '您選的餐點是 草莓鬆餅 ，這項餐點的熱量為 425 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('冰淇淋鬆餅 ',message):
            reply = '您選的餐點是 冰淇淋鬆餅 ，這項餐點的熱量為 507 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('巧克力鬆餅 ',message):
            reply = '您選的餐點是 巧克力鬆餅 ，這項餐點的熱量為 484 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('海鮮披薩',message):
            reply = '您選的餐點是 海鮮披薩，這項餐點的熱量為 218 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('總匯披薩',message):
            reply = '您選的餐點是 總匯披薩，這項餐點的熱量為 238 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('夏威夷披薩 ',message):
            reply = '您選的餐點是 夏威夷披薩 ，這項餐點的熱量為 252 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('素食披薩 ',message):
            reply = '您選的餐點是 素食披薩 ，這項餐點的熱量為 195 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('燻雞披薩 ',message):
            reply = '您選的餐點是 燻雞披薩 ，這項餐點的熱量為 238 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('小熱狗 /5支 ',message):
            reply = '您選的餐點是 小熱狗 /5支 ，這項餐點的熱量為 231 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('煎餃 /8粒 ',message):
            reply = '您選的餐點是 煎餃 /8粒 ，這項餐點的熱量為 280 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('薯條 ',message):
            reply = '您選的餐點是 薯條 ，這項餐點的熱量為 130 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('麥克雞塊 /6塊 ',message):
            reply = '您選的餐點是 麥克雞塊 /6塊 ，這項餐點的熱量為 350 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('脆皮雞排 ',message):
            reply = '您選的餐點是 脆皮雞排 ，這項餐點的熱量為 480 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('卡拉雞捲 ',message):
            reply = '您選的餐點是 卡拉雞捲 ，這項餐點的熱量為 560 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('起司豬排 ',message):
            reply = '您選的餐點是 起司豬排 ，這項餐點的熱量為 440 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('煙燻雞肉捲 ',message):
            reply = '您選的餐點是 煙燻雞肉捲 ，這項餐點的熱量為 322 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('生菜熱狗 ',message):
            reply = '您選的餐點是 生菜熱狗 ，這項餐點的熱量為 375 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('水餃 10粒 ',message):
            reply = '您選的餐點是 水餃 10粒 ，這項餐點的熱量為 409 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('沙朗牛排',message):
            reply = '您選的餐點是 沙朗牛排，這項餐點的熱量為 980 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('特製牛排 ',message):
            reply = '您選的餐點是 特製牛排 ，這項餐點的熱量為 880 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('嫩煎無骨牛小排',message):
            reply = '您選的餐點是 嫩煎無骨牛小排，這項餐點的熱量為 690 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('英式田園雞腿排',message):
            reply = '您選的餐點是 英式田園雞腿排，這項餐點的熱量為 665 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('原味雞腿排 ',message):
            reply = '您選的餐點是 原味雞腿排 ，這項餐點的熱量為 720 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('厚讚香蒜雞排',message):
            reply = '您選的餐點是 厚讚香蒜雞排，這項餐點的熱量為 752 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('脆皮鴨胸佐紅酒圓蔥醬',message):
            reply = '您選的餐點是 脆皮鴨胸佐紅酒圓蔥醬，這項餐點的熱量為 896 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炭烤鯛魚',message):
            reply = '您選的餐點是 炭烤鯛魚，這項餐點的熱量為 530 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('清蒸冰島鱈魚',message):
            reply = '您選的餐點是 清蒸冰島鱈魚，這項餐點的熱量為 395 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('香煎金目鱸魚排佐鯷魚大蒜醬',message):
            reply = '您選的餐點是 香煎金目鱸魚排佐鯷魚大蒜醬，這項餐點的熱量為 572 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('薑汁照燒豬肉排',message):
            reply = '您選的餐點是 薑汁照燒豬肉排，這項餐點的熱量為 767 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('南瓜季節鮮蔬',message):
            reply = '您選的餐點是 南瓜季節鮮蔬，這項餐點的熱量為 377 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('碳烤紐西蘭無骨牛小排佐珍菌菇醬100g  ',message):
            reply = '您選的餐點是 碳烤紐西蘭無骨牛小排佐珍菌菇醬100g  ，這項餐點的熱量為 249 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('香煎麥年魴魚排佐檸檬酸豆奶油醬100g',message):
            reply = '您選的餐點是 香煎麥年魴魚排佐檸檬酸豆奶油醬100g，這項餐點的熱量為 160 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('和風義大利麵 ',message):
            reply = '您選的餐點是 和風義大利麵 ，這項餐點的熱量為 711 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('清炒鯷魚橄欖風乾番茄義大利麵 ',message):
            reply = '您選的餐點是 清炒鯷魚橄欖風乾番茄義大利麵 ，這項餐點的熱量為 754 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('茄汁雞肉義大利麵 ',message):
            reply = '您選的餐點是 茄汁雞肉義大利麵 ，這項餐點的熱量為 608 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('原汁墨魚海鮮義大利麵 ',message):
            reply = '您選的餐點是 原汁墨魚海鮮義大利麵 ，這項餐點的熱量為 690 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('野菜鮮蔬義大利麵 ',message):
            reply = '您選的餐點是 野菜鮮蔬義大利麵 ，這項餐點的熱量為 625 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('義式蒜辣培根麵 ',message):
            reply = '您選的餐點是 義式蒜辣培根麵 ，這項餐點的熱量為 675 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('奶油培根義大利麵',message):
            reply = '您選的餐點是 奶油培根義大利麵，這項餐點的熱量為 591 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('鮮魚義大利麵 ',message):
            reply = '您選的餐點是 鮮魚義大利麵 ，這項餐點的熱量為 468 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('滿福蛋堡',message):
            reply = '您選的餐點是 滿福蛋堡，這項餐點的熱量為 677 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('香雞蛋堡',message):
            reply = '您選的餐點是 香雞蛋堡，這項餐點的熱量為 743 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('鮪魚蛋堡',message):
            reply = '您選的餐點是 鮪魚蛋堡，這項餐點的熱量為 669 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('煙燻雞肉蛋堡',message):
            reply = '您選的餐點是 煙燻雞肉蛋堡，這項餐點的熱量為 612 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('花枝蛋堡',message):
            reply = '您選的餐點是 花枝蛋堡，這項餐點的熱量為 661 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('里肌豬排蛋堡',message):
            reply = '您選的餐點是 里肌豬排蛋堡，這項餐點的熱量為 656 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('鮮蝦蛋堡',message):
            reply = '您選的餐點是 鮮蝦蛋堡，這項餐點的熱量為 607 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('照燒豬肉蛋堡',message):
            reply = '您選的餐點是 照燒豬肉蛋堡，這項餐點的熱量為 659 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('總匯漢堡',message):
            reply = '您選的餐點是 總匯漢堡，這項餐點的熱量為 745 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('脆皮雞排蛋堡',message):
            reply = '您選的餐點是 脆皮雞排蛋堡，這項餐點的熱量為 748 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('藍帶起司豬排蛋堡',message):
            reply = '您選的餐點是 藍帶起司豬排蛋堡，這項餐點的熱量為 697 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('超厚牛肉起司蛋堡',message):
            reply = '您選的餐點是 超厚牛肉起司蛋堡，這項餐點的熱量為 797 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('烤煎蛋三明治',message):
            reply = '您選的餐點是 烤煎蛋三明治，這項餐點的熱量為 386 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('火腿蛋三明治',message):
            reply = '您選的餐點是 火腿蛋三明治，這項餐點的熱量為 472 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('起司蛋三明治',message):
            reply = '您選的餐點是 起司蛋三明治，這項餐點的熱量為 494 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('培根蛋三明治',message):
            reply = '您選的餐點是 培根蛋三明治，這項餐點的熱量為 553 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('薯餅蛋三明治',message):
            reply = '您選的餐點是 薯餅蛋三明治，這項餐點的熱量為 529 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('鮪魚蛋三明治',message):
            reply = '您選的餐點是 鮪魚蛋三明治，這項餐點的熱量為 554 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('里肌蛋三明治',message):
            reply = '您選的餐點是 里肌蛋三明治，這項餐點的熱量為 514 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('照燒豬肉蛋三明治',message):
            reply = '您選的餐點是 照燒豬肉蛋三明治，這項餐點的熱量為 519 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('脆皮雞排蛋三明治',message):
            reply = '您選的餐點是 脆皮雞排蛋三明治，這項餐點的熱量為 638 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('豬排總匯三明治',message):
            reply = '您選的餐點是 豬排總匯三明治，這項餐點的熱量為 850 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('海陸總匯三明治',message):
            reply = '您選的餐點是 海陸總匯三明治，這項餐點的熱量為 881 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('黑胡椒牛肉三明治',message):
            reply = '您選的餐點是 黑胡椒牛肉三明治，這項餐點的熱量為 369 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('原味蛋餅',message):
            reply = '您選的餐點是 原味蛋餅，這項餐點的熱量為 236 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('九層塔蛋餅',message):
            reply = '您選的餐點是 九層塔蛋餅，這項餐點的熱量為 239 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('起司蛋餅',message):
            reply = '您選的餐點是 起司蛋餅，這項餐點的熱量為 300 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('培根蛋餅',message):
            reply = '您選的餐點是 培根蛋餅，這項餐點的熱量為 298 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('火腿蛋餅',message):
            reply = '您選的餐點是 火腿蛋餅，這項餐點的熱量為 281 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('熱狗蛋餅',message):
            reply = '您選的餐點是 熱狗蛋餅，這項餐點的熱量為 329 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蔬菜蛋餅',message):
            reply = '您選的餐點是 蔬菜蛋餅，這項餐點的熱量為 248 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('滿福蛋餅',message):
            reply = '您選的餐點是 滿福蛋餅，這項餐點的熱量為 324 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('鮪魚蛋餅',message):
            reply = '您選的餐點是 鮪魚蛋餅，這項餐點的熱量為 392 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('里肌蛋餅',message):
            reply = '您選的餐點是 里肌蛋餅，這項餐點的熱量為 320 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('香烤雞肉堡',message):
            reply = '您選的餐點是 香烤雞肉堡，這項餐點的熱量為 320 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('燒烤牛肉堡',message):
            reply = '您選的餐點是 燒烤牛肉堡，這項餐點的熱量為 320 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('火腿堡',message):
            reply = '您選的餐點是 火腿堡，這項餐點的熱量為 290 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('火雞胸肉堡',message):
            reply = '您選的餐點是 火雞胸肉堡，這項餐點的熱量為 280 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('義大利經典堡',message):
            reply = '您選的餐點是 義大利經典堡，這項餐點的熱量為 450 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('鮪魚堡',message):
            reply = '您選的餐點是 鮪魚堡，這項餐點的熱量為 450 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蔬菜堡',message):
            reply = '您選的餐點是 蔬菜堡，這項餐點的熱量為 230 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('火雞火腿堡',message):
            reply = '您選的餐點是 火雞火腿堡，這項餐點的熱量為 290 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('波蘿麵包',message):
            reply = '您選的餐點是 波蘿麵包，這項餐點的熱量為 185 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('紅豆麵包',message):
            reply = '您選的餐點是 紅豆麵包，這項餐點的熱量為 264 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('奶酥麵包',message):
            reply = '您選的餐點是 奶酥麵包，這項餐點的熱量為 265 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('全麥核桃麵包',message):
            reply = '您選的餐點是 全麥核桃麵包，這項餐點的熱量為 352 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('草莓麵包',message):
            reply = '您選的餐點是 草莓麵包，這項餐點的熱量為 225 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('香蒜麵包',message):
            reply = '您選的餐點是 香蒜麵包，這項餐點的熱量為 506 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('椰子麵包',message):
            reply = '您選的餐點是 椰子麵包，這項餐點的熱量為 226 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('吐司',message):
            reply = '您選的餐點是 吐司，這項餐點的熱量為 70 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('小餐包',message):
            reply = '您選的餐點是 小餐包，這項餐點的熱量為 70 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('貝果',message):
            reply = '您選的餐點是 貝果，這項餐點的熱量為 250 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('起司貝果',message):
            reply = '您選的餐點是 起司貝果，這項餐點的熱量為 280 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蘿蔔糕/2片',message):
            reply = '您選的餐點是 蘿蔔糕/2片，這項餐點的熱量為 214 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('薯餅 /2片',message):
            reply = '您選的餐點是 薯餅 /2片，這項餐點的熱量為 99 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('紫米飯糰',message):
            reply = '您選的餐點是 紫米飯糰，這項餐點的熱量為 317 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('白飯',message):
            reply = '您選的餐點是 白飯，這項餐點的熱量為 280 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('粥',message):
            reply = '您選的餐點是 粥，這項餐點的熱量為 140 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('麵條',message):
            reply = '您選的餐點是 麵條，這項餐點的熱量為 140 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('饅頭',message):
            reply = '您選的餐點是 饅頭，這項餐點的熱量為 280 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('香煎排骨',message):
            reply = '您選的餐點是 香煎排骨，這項餐點的熱量為 250 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('鼓椒排骨',message):
            reply = '您選的餐點是 鼓椒排骨，這項餐點的熱量為 287 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('鹽酥排骨',message):
            reply = '您選的餐點是 鹽酥排骨，這項餐點的熱量為 255 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('糖醋排骨',message):
            reply = '您選的餐點是 糖醋排骨，這項餐點的熱量為 330 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炸豬排',message):
            reply = '您選的餐點是 炸豬排，這項餐點的熱量為 255 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('香滷控肉',message):
            reply = '您選的餐點是 香滷控肉，這項餐點的熱量為 270 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蘿蔔燒肉',message):
            reply = '您選的餐點是 蘿蔔燒肉，這項餐點的熱量為 268 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('回鍋肉',message):
            reply = '您選的餐點是 回鍋肉，這項餐點的熱量為 265 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('黑胡椒肉片',message):
            reply = '您選的餐點是 黑胡椒肉片，這項餐點的熱量為 206 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('醬爆肉片',message):
            reply = '您選的餐點是 醬爆肉片，這項餐點的熱量為 215 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('醬爆肉片',message):
            reply = '您選的餐點是 醬爆肉片，這項餐點的熱量為 173 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蒜泥白肉',message):
            reply = '您選的餐點是 蒜泥白肉，這項餐點的熱量為 129 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('叉燒肉',message):
            reply = '您選的餐點是 叉燒肉，這項餐點的熱量為 134 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('清蒸獅子頭',message):
            reply = '您選的餐點是 清蒸獅子頭，這項餐點的熱量為 229 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('瓜仔肉',message):
            reply = '您選的餐點是 瓜仔肉，這項餐點的熱量為 277 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('滷雞腿',message):
            reply = '您選的餐點是 滷雞腿，這項餐點的熱量為 205 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炸雞腿',message):
            reply = '您選的餐點是 炸雞腿，這項餐點的熱量為 255 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('烤腿排',message):
            reply = '您選的餐點是 烤腿排，這項餐點的熱量為 215 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('花雕醉雞',message):
            reply = '您選的餐點是 花雕醉雞，這項餐點的熱量為 283 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('黃燜雞丁',message):
            reply = '您選的餐點是 黃燜雞丁，這項餐點的熱量為 118 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('雪菜雞片',message):
            reply = '您選的餐點是 雪菜雞片，這項餐點的熱量為 185 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('成都子雞',message):
            reply = '您選的餐點是 成都子雞，這項餐點的熱量為 161 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('小黃魚煲',message):
            reply = '您選的餐點是 小黃魚煲，這項餐點的熱量為 217 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('香炸白帶魚',message):
            reply = '您選的餐點是 香炸白帶魚，這項餐點的熱量為 240 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('樹子蒸午仔魚',message):
            reply = '您選的餐點是 樹子蒸午仔魚，這項餐點的熱量為 214 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蔥爆鯽魚',message):
            reply = '您選的餐點是 蔥爆鯽魚，這項餐點的熱量為 252 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('醋溜魚塊',message):
            reply = '您選的餐點是 醋溜魚塊，這項餐點的熱量為 216 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('五味魚丁',message):
            reply = '您選的餐點是 五味魚丁，這項餐點的熱量為 172 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('五味軟絲',message):
            reply = '您選的餐點是 五味軟絲，這項餐點的熱量為 192 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炸花枝條',message):
            reply = '您選的餐點是 炸花枝條，這項餐點的熱量為 180 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('紅蘿蔔炒蛋',message):
            reply = '您選的餐點是 紅蘿蔔炒蛋，這項餐點的熱量為 103 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蕃茄炒蛋',message):
            reply = '您選的餐點是 蕃茄炒蛋，這項餐點的熱量為 123 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('四色炒蛋',message):
            reply = '您選的餐點是 四色炒蛋，這項餐點的熱量為 182 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蒸蛋',message):
            reply = '您選的餐點是 蒸蛋，這項餐點的熱量為 60 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('香滷豆干',message):
            reply = '您選的餐點是 香滷豆干，這項餐點的熱量為 154 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('小魚豆乾',message):
            reply = '您選的餐點是 小魚豆乾，這項餐點的熱量為 210 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('小魚苦瓜',message):
            reply = '您選的餐點是 小魚苦瓜，這項餐點的熱量為 120 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('咖哩洋芋',message):
            reply = '您選的餐點是 咖哩洋芋，這項餐點的熱量為 120 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('南瓜蓮子',message):
            reply = '您選的餐點是 南瓜蓮子，這項餐點的熱量為 121 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('青椒炒培根',message):
            reply = '您選的餐點是 青椒炒培根，這項餐點的熱量為 166 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('小魚苦瓜',message):
            reply = '您選的餐點是 小魚苦瓜，這項餐點的熱量為 120 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('咖理洋芋',message):
            reply = '您選的餐點是 咖理洋芋，這項餐點的熱量為 120 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('甜椒肉片',message):
            reply = '您選的餐點是 甜椒肉片，這項餐點的熱量為 102 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炒玉米',message):
            reply = '您選的餐點是 炒玉米，這項餐點的熱量為 150 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('高麗培根',message):
            reply = '您選的餐點是 高麗培根，這項餐點的熱量為 166 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('雙脆肉片',message):
            reply = '您選的餐點是 雙脆肉片，這項餐點的熱量為 102 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('筊白筍炒肉絲',message):
            reply = '您選的餐點是 筊白筍炒肉絲，這項餐點的熱量為 116 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('大白炒蝦米',message):
            reply = '您選的餐點是 大白炒蝦米，這項餐點的熱量為 114 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('玉米肉絲',message):
            reply = '您選的餐點是 玉米肉絲，這項餐點的熱量為 137 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('麻婆豆腐',message):
            reply = '您選的餐點是 麻婆豆腐，這項餐點的熱量為 163 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('肉羹黃瓜',message):
            reply = '您選的餐點是 肉羹黃瓜，這項餐點的熱量為 107 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('三色豆',message):
            reply = '您選的餐點是 三色豆，這項餐點的熱量為 125 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('鹹菜豬血',message):
            reply = '您選的餐點是 鹹菜豬血，這項餐點的熱量為 78 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('油燜苦瓜',message):
            reply = '您選的餐點是 油燜苦瓜，這項餐點的熱量為 245 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('苦瓜肉片',message):
            reply = '您選的餐點是 苦瓜肉片，這項餐點的熱量為 96 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('拌三絲',message):
            reply = '您選的餐點是 拌三絲，這項餐點的熱量為 91 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炸豆腐',message):
            reply = '您選的餐點是 炸豆腐，這項餐點的熱量為 170 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炒高麗菜',message):
            reply = '您選的餐點是 炒高麗菜，這項餐點的熱量為 75 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炒綠花椰',message):
            reply = '您選的餐點是 炒綠花椰，這項餐點的熱量為 66 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炒波菜',message):
            reply = '您選的餐點是 炒波菜，這項餐點的熱量為 77 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('海芽炒豆芽',message):
            reply = '您選的餐點是 海芽炒豆芽，這項餐點的熱量為 70 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('涼拌海帶絲',message):
            reply = '您選的餐點是 涼拌海帶絲，這項餐點的熱量為 65 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炒地瓜葉',message):
            reply = '您選的餐點是 炒地瓜葉，這項餐點的熱量為 70 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('涼拌青花菜',message):
            reply = '您選的餐點是 涼拌青花菜，這項餐點的熱量為 47 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炒空心菜',message):
            reply = '您選的餐點是 炒空心菜，這項餐點的熱量為 70 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炒豌豆夾',message):
            reply = '您選的餐點是 炒豌豆夾，這項餐點的熱量為 89 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炒韭菜花',message):
            reply = '您選的餐點是 炒韭菜花，這項餐點的熱量為 75 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炒菠菜',message):
            reply = '您選的餐點是 炒菠菜，這項餐點的熱量為 68 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炒萵苣',message):
            reply = '您選的餐點是 炒萵苣，這項餐點的熱量為 57 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炒白菜',message):
            reply = '您選的餐點是 炒白菜，這項餐點的熱量為 59 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炒青江菜',message):
            reply = '您選的餐點是 炒青江菜，這項餐點的熱量為 62 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炒牛蒡絲',message):
            reply = '您選的餐點是 炒牛蒡絲，這項餐點的熱量為 143 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炒蘿蔔絲',message):
            reply = '您選的餐點是 炒蘿蔔絲，這項餐點的熱量為 83 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('涼拌藕片',message):
            reply = '您選的餐點是 涼拌藕片，這項餐點的熱量為 78 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炒筍絲',message):
            reply = '您選的餐點是 炒筍絲，這項餐點的熱量為 69 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('苜蓿芽沙拉',message):
            reply = '您選的餐點是 苜蓿芽沙拉，這項餐點的熱量為 70 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('炒筊白筍',message):
            reply = '您選的餐點是 炒筊白筍，這項餐點的熱量為 69 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('涼拌荸齊',message):
            reply = '您選的餐點是 涼拌荸齊，這項餐點的熱量為 84 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('滷蘿蔔',message):
            reply = '您選的餐點是 滷蘿蔔，這項餐點的熱量為 25 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('醃製嫩薑',message):
            reply = '您選的餐點是 醃製嫩薑，這項餐點的熱量為 41 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('涼拌花椰沙拉',message):
            reply = '您選的餐點是 涼拌花椰沙拉，這項餐點的熱量為 70 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('沙拉筍',message):
            reply = '您選的餐點是 沙拉筍，這項餐點的熱量為 77 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('茶',message):
            reply = '您選的餐點是 茶，這項餐點的熱量為 830 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('茶(無糖) ',message):
            reply = '您選的餐點是 茶(無糖) ，這項餐點的熱量為 891 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('枸杞茶',message):
            reply = '您選的餐點是 枸杞茶，這項餐點的熱量為 773 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('菊花茶',message):
            reply = '您選的餐點是 菊花茶，這項餐點的熱量為 795 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('洛神茶',message):
            reply = '您選的餐點是 洛神茶，這項餐點的熱量為 558 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蜂蜜茶飲',message):
            reply = '您選的餐點是 蜂蜜茶飲，這項餐點的熱量為 773 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('紅',message):
            reply = '您選的餐點是 紅，這項餐點的熱量為 691 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('紅(綠)茶',message):
            reply = '您選的餐點是 紅(綠)茶，這項餐點的熱量為 490 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('阿薩姆紅茶',message):
            reply = '您選的餐點是 阿薩姆紅茶，這項餐點的熱量為 766 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('茉香綠茶',message):
            reply = '您選的餐點是 茉香綠茶，這項餐點的熱量為 496 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('多多綠茶',message):
            reply = '您選的餐點是 多多綠茶，這項餐點的熱量為 644 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('百香綠茶',message):
            reply = '您選的餐點是 百香綠茶，這項餐點的熱量為 653 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('葡萄柚綠茶',message):
            reply = '您選的餐點是 葡萄柚綠茶，這項餐點的熱量為 605 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('奶茶',message):
            reply = '您選的餐點是 奶茶，這項餐點的熱量為 603 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('養樂多綠',message):
            reply = '您選的餐點是 養樂多綠，這項餐點的熱量為 730 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('特調鮮奶茶',message):
            reply = '您選的餐點是 特調鮮奶茶，這項餐點的熱量為 670 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('茉香奶茶',message):
            reply = '您選的餐點是 茉香奶茶，這項餐點的熱量為 610 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('珍珠奶茶',message):
            reply = '您選的餐點是 珍珠奶茶，這項餐點的熱量為 536 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('特調鮮奶綠',message):
            reply = '您選的餐點是 特調鮮奶綠，這項餐點的熱量為 590 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('大吉嶺鮮奶茶',message):
            reply = '您選的餐點是 大吉嶺鮮奶茶，這項餐點的熱量為 753 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蜂蜜檸檬茶',message):
            reply = '您選的餐點是 蜂蜜檸檬茶，這項餐點的熱量為 588 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蜂蜜柚子茶',message):
            reply = '您選的餐點是 蜂蜜柚子茶，這項餐點的熱量為 523 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('梅果綠茶',message):
            reply = '您選的餐點是 梅果綠茶，這項餐點的熱量為 559 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('美式咖啡',message):
            reply = '您選的餐點是 美式咖啡，這項餐點的熱量為 377 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('義式濃縮咖啡',message):
            reply = '您選的餐點是 義式濃縮咖啡，這項餐點的熱量為 733 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('熱咖啡',message):
            reply = '您選的餐點是 熱咖啡，這項餐點的熱量為 612 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('冰咖啡',message):
            reply = '您選的餐點是 冰咖啡，這項餐點的熱量為 887 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('熱卡布奇諾',message):
            reply = '您選的餐點是 熱卡布奇諾，這項餐點的熱量為 804 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('熱維也納咖啡',message):
            reply = '您選的餐點是 熱維也納咖啡，這項餐點的熱量為 684 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('冰維也納咖啡',message):
            reply = '您選的餐點是 冰維也納咖啡，這項餐點的熱量為 470 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('提拉米蘇/拿鐵',message):
            reply = '您選的餐點是 提拉米蘇/拿鐵，這項餐點的熱量為 885 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('冰拿鐵',message):
            reply = '您選的餐點是 冰拿鐵，這項餐點的熱量為 900 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('冰淇淋咖啡',message):
            reply = '您選的餐點是 冰淇淋咖啡，這項餐點的熱量為 829 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('冰摩卡巧克力',message):
            reply = '您選的餐點是 冰摩卡巧克力，這項餐點的熱量為 848 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('義式香濃可可',message):
            reply = '您選的餐點是 義式香濃可可，這項餐點的熱量為 802 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('義式香濃可可(冰)',message):
            reply = '您選的餐點是 義式香濃可可(冰)，這項餐點的熱量為 716 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('義式香濃可可',message):
            reply = '您選的餐點是 義式香濃可可，這項餐點的熱量為 848 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('義式香濃可可(熱)',message):
            reply = '您選的餐點是 義式香濃可可(熱)，這項餐點的熱量為 711 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('義式摩卡巧克力',message):
            reply = '您選的餐點是 義式摩卡巧克力，這項餐點的熱量為 758 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('抹茶牛奶',message):
            reply = '您選的餐點是 抹茶牛奶，這項餐點的熱量為 480 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('可可牛奶',message):
            reply = '您選的餐點是 可可牛奶，這項餐點的熱量為 738 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('可口可樂',message):
            reply = '您選的餐點是 可口可樂，這項餐點的熱量為 584 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('雪碧',message):
            reply = '您選的餐點是 雪碧，這項餐點的熱量為 587 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('抹茶冰淇淋',message):
            reply = '您選的餐點是 抹茶冰淇淋，這項餐點的熱量為 372 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('香草冰淇淋',message):
            reply = '您選的餐點是 香草冰淇淋，這項餐點的熱量為 767 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('豆漿',message):
            reply = '您選的餐點是 豆漿，這項餐點的熱量為 838 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('可樂',message):
            reply = '您選的餐點是 可樂，這項餐點的熱量為 765 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('柳橙汁',message):
            reply = '您選的餐點是 柳橙汁，這項餐點的熱量為 753 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('蘋果多多',message):
            reply = '您選的餐點是 蘋果多多，這項餐點的熱量為 833 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('貢丸湯',message):
            reply = '您選的餐點是 貢丸湯，這項餐點的熱量為 744 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('餛飩湯',message):
            reply = '您選的餐點是 餛飩湯，這項餐點的熱量為 745 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('玉米濃湯',message):
            reply = '您選的餐點是 玉米濃湯，這項餐點的熱量為 371 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('酸辣湯',message):
            reply = '您選的餐點是 酸辣湯，這項餐點的熱量為 418 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif re.match('紅燒湯',message):
            reply = '您選的餐點是 紅燒湯，這項餐點的熱量為 620 大卡'
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage('沒這東西'))


#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

