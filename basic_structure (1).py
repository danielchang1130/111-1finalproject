#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask_ngrok import run_with_ngrok
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage   # 載入 TextSendMessage 模組
import json
import pandas as pd


# In[22]:


test = pd.read_csv('test.csv')


# In[ ]:


name = []
for i in test['品項']:
    name.append(i)

kcal = []
for i in test['熱量(kcal)']:
    kcal.append(i)

category = []
for i in test['分類']:
    category.append(i)
    
menu = []
for i in range(len(name)):
    menu.append([name[i], int(kcal[i]), category[i]])


# In[ ]:


category_lst = []
for i in category:
    if i not in category_lst:
        category_lst.append(i)


# In[ ]:




@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi('QdnxdzUpW3bG3IekkGkys2bKehjP46GR3pABHDgqz0oFVcIkVNYjYaadWnbI1vpyv+CzYjTGOavX2eFBXVCixm4TxrGVul2RZlVg0/m9hZZ5s2rqbZa+iq/nm9lMxyiYfu6NpLC4W8g7D2v+3FOFKAdB04t89/1O/w1cDnyilFU=')
        handler = WebhookHandler('1d52764ed6d474557dd6b589adecddac')
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']         # 取得 reply token
        msg = json_data['events'][0]['message']['text']   # 取得使用者發送的訊息
        for i in menu:
            if msg == i[0]:
            reply_content = '您所選擇的食品為'+i[0]+' ,熱量為'+str(i[1])+'大卡'
                text_message = TextSendMessage(text=reply_content)   # 設定回傳同樣的訊息
                line_bot_api.reply_message(tk,text_message)          # 回傳訊息
    except:
        print('error')
    return 'OK'

if __name__ == "__main__":
    run_with_ngrok(app)
    app.run()
