#coding: utf-8
from flask import Flask, request, abort
from linebot import ( LineBotApi, WebhookHandler )
from linebot.exceptions import( InvalidSignatureError )
from linebot.models import *


app = Flask(__name__)  


line_bot_api = LineBotApi("AdFEcoktb3nvIrUtjZ1DXpsh+4iWRLQkiJ4jeqb8qXc2pZkNDjX7/oS6Hbx+EuYdVtrU4Hsm2ofBwWlGEc71jn+8NL8+XyroR4Va15mOEcSWU7dFE5IjbBWc7DAEJ1q8yPOg4ehzsrlOZ/rsKxJsCQdB04t89/1O/w1cDnyilFU=")  #-- YOUR_CHANNEL_ACCESS_TOKEN

handler = WebhookHandler("2e8876fa18133363b4eaa642b733cda2")  


@app.route("/callback", methods=['POST']) 

def callback():
    print(">>>>>>>>> 1.testing") 
    signature = request.headers['X-Line-Signature']
    print(">>>>>>>>> 2.testing")  
    body = request.get_data(as_text=True)
    print(">>>>>>>>> 3.testing"+body)
    app.logger.info("Request body: " + body)
    print(">>>>>>>>> 4.testing-body:"+body)
    
    try:
        print(">>>>>>>>> 5.testing-try:...")
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)



def handle_message(event):
    print(event)
    if event.message.id == "100001":
        return
    text = event.message.text
    if (text=="help"):
        reply_text = "請對我輸入以下的關鍵字\n\n目前支援指令：\n[時間] + [縣市] + 天氣 or 空氣 or 帶傘\n[縣市] + [時間] + 天氣 or 空氣 or 帶傘\n\n例如：今天桃園市天氣、臺北市明天空氣、後天臺中市帶傘\n\n[時間]：今天、明天、後天\n[縣市]：臺北市、新北市、桃園市、臺中市、臺南市、高雄市、基隆市、新竹市、嘉義市、新竹縣、苗栗縣、彰化縣、南投縣、雲林縣、嘉義縣、屏東縣、宜蘭縣、花蓮縣、臺東縣、台東縣、澎湖縣、金門縣、連江縣"
    elif(text=="Help"): 
        reply_text = "請對我輸入以下的關鍵字\n\n目前支援指令：\n[時間] + [縣市] + 天氣 or 空氣 or 帶傘\n[縣市] + [時間] + 天氣 or 空氣 or 帶傘\n\n例如：今天桃園市天氣、臺北市明天空氣、後天臺中市帶傘\n\n[時間]：今天、明天、後天\n[縣市]：臺北市、新北市、桃園市、臺中市、臺南市、高雄市、基隆市、新竹市、嘉義市、新竹縣、苗栗縣、彰化縣、南投縣、雲林縣、嘉義縣、屏東縣、宜蘭縣、花蓮縣、臺東縣、台東縣、澎湖縣、金門縣、連江縣"
    elif(text=="hElp"):
        reply_text = "請對我輸入以下的關鍵字\n\n目前支援指令：\n[時間] + [縣市] + 天氣 or 空氣 or 帶傘\n[縣市] + [時間] + 天氣 or 空氣 or 帶傘\n\n例如：今天桃園市天氣、臺北市明天空氣、後天臺中市帶傘\n\n[時間]：今天、明天、後天\n[縣市]：臺北市、新北市、桃園市、臺中市、臺南市、高雄市、基隆市、新竹市、嘉義市、新竹縣、苗栗縣、彰化縣、南投縣、雲林縣、嘉義縣、屏東縣、宜蘭縣、花蓮縣、臺東縣、台東縣、澎湖縣、金門縣、連江縣"
    elif(text=="heLp"):
        reply_text = "請對我輸入以下的關鍵字\n\n目前支援指令：\n[時間] + [縣市] + 天氣 or 空氣 or 帶傘\n[縣市] + [時間] + 天氣 or 空氣 or 帶傘\n\n例如：今天桃園市天氣、臺北市明天空氣、後天臺中市帶傘\n\n[時間]：今天、明天、後天\n[縣市]：臺北市、新北市、桃園市、臺中市、臺南市、高雄市、基隆市、新竹市、嘉義市、新竹縣、苗栗縣、彰化縣、南投縣、雲林縣、嘉義縣、屏東縣、宜蘭縣、花蓮縣、臺東縣、台東縣、澎湖縣、金門縣、連江縣"
    elif(text=="helP"):
        reply_text = "請對我輸入以下的關鍵字\n\n目前支援指令：\n[時間] + [縣市] + 天氣 or 空氣 or 帶傘\n[縣市] + [時間] + 天氣 or 空氣 or 帶傘\n\n例如：今天桃園市天氣、臺北市明天空氣、後天臺中市帶傘\n\n[時間]：今天、明天、後天\n[縣市]：臺北市、新北市、桃園市、臺中市、臺南市、高雄市、基隆市、新竹市、嘉義市、新竹縣、苗栗縣、彰化縣、南投縣、雲林縣、嘉義縣、屏東縣、宜蘭縣、花蓮縣、臺東縣、台東縣、澎湖縣、金門縣、連江縣"
    elif(text=="HELP"):
        reply_text = "請對我輸入以下的關鍵字\n\n目前支援指令：\n[時間] + [縣市] + 天氣 or 空氣 or 帶傘\n[縣市] + [時間] + 天氣 or 空氣 or 帶傘\n\n例如：今天桃園市天氣、臺北市明天空氣、後天臺中市帶傘\n\n[時間]：今天、明天、後天\n[縣市]：臺北市、新北市、桃園市、臺中市、臺南市、高雄市、基隆市、新竹市、嘉義市、新竹縣、苗栗縣、彰化縣、南投縣、雲林縣、嘉義縣、屏東縣、宜蘭縣、花蓮縣、臺東縣、台東縣、澎湖縣、金門縣、連江縣"
    elif(text=="hELP"):
        reply_text = "請對我輸入以下的關鍵字\n\n目前支援指令：\n[時間] + [縣市] + 天氣 or 空氣 or 帶傘\n[縣市] + [時間] + 天氣 or 空氣 or 帶傘\n\n例如：今天桃園市天氣、臺北市明天空氣、後天臺中市帶傘\n\n[時間]：今天、明天、後天\n[縣市]：臺北市、新北市、桃園市、臺中市、臺南市、高雄市、基隆市、新竹市、嘉義市、新竹縣、苗栗縣、彰化縣、南投縣、雲林縣、嘉義縣、屏東縣、宜蘭縣、花蓮縣、臺東縣、台東縣、澎湖縣、金門縣、連江縣"
    elif(text=="HeLP"):
        reply_text = "請對我輸入以下的關鍵字\n\n目前支援指令：\n[時間] + [縣市] + 天氣 or 空氣 or 帶傘\n[縣市] + [時間] + 天氣 or 空氣 or 帶傘\n\n例如：今天桃園市天氣、臺北市明天空氣、後天臺中市帶傘\n\n[時間]：今天、明天、後天\n[縣市]：臺北市、新北市、桃園市、臺中市、臺南市、高雄市、基隆市、新竹市、嘉義市、新竹縣、苗栗縣、彰化縣、南投縣、雲林縣、嘉義縣、屏東縣、宜蘭縣、花蓮縣、臺東縣、台東縣、澎湖縣、金門縣、連江縣"
    elif(text=="HElP"):
        reply_text = "請對我輸入以下的關鍵字\n\n目前支援指令：\n[時間] + [縣市] + 天氣 or 空氣 or 帶傘\n[縣市] + [時間] + 天氣 or 空氣 or 帶傘\n\n例如：今天桃園市天氣、臺北市明天空氣、後天臺中市帶傘\n\n[時間]：今天、明天、後天\n[縣市]：臺北市、新北市、桃園市、臺中市、臺南市、高雄市、基隆市、新竹市、嘉義市、新竹縣、苗栗縣、彰化縣、南投縣、雲林縣、嘉義縣、屏東縣、宜蘭縣、花蓮縣、臺東縣、台東縣、澎湖縣、金門縣、連江縣"
    elif(text=="HELp"):
        reply_text = "請對我輸入以下的關鍵字\n\n目前支援指令：\n[時間] + [縣市] + 天氣 or 空氣 or 帶傘\n[縣市] + [時間] + 天氣 or 空氣 or 帶傘\n\n例如：今天桃園市天氣、臺北市明天空氣、後天臺中市帶傘\n\n[時間]：今天、明天、後天\n[縣市]：臺北市、新北市、桃園市、臺中市、臺南市、高雄市、基隆市、新竹市、嘉義市、新竹縣、苗栗縣、彰化縣、南投縣、雲林縣、嘉義縣、屏東縣、宜蘭縣、花蓮縣、臺東縣、台東縣、澎湖縣、金門縣、連江縣"





    elif(text=="今天臺北市天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：30%\n風速：26公里/時"
    elif(text=="今天台北市天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：30%\n風速：26公里/時"
    elif(text=="今天新北市天氣"):
        reply_text ="多雲\n降雨機率：20%\n濕度：25%\n風速：32公里/時"
    elif(text=="今天桃園市天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：20%\n風速：20公里/時"
    elif(text=="今天臺中市天氣"):
        reply_text ="陰\n降雨機率：30%\n濕度：42%\n風速：27公里/時"
    elif(text=="今天台中市天氣"):
        reply_text ="陰\n降雨機率：30%\n濕度：42%\n風速：27公里/時"
    elif(text=="今天臺南市天氣"):
        reply_text ="陣雨\n降雨機率：60%\n濕度：70%\n風速：28公里/時"
    elif(text=="今天台南市天氣"):
        reply_text ="陣雨\n降雨機率：60%\n濕度：70%\n風速：28公里/時"
    elif(text=="今天高雄市天氣"):
        reply_text ="雷陣雨\n降雨機率：100%\n濕度：85%\n風速：45公里/時"
    elif(text=="今天基隆市天氣"):
        reply_text ="小雨\n降雨機率：70%\n濕度：75%\n風速：15公里/時"
    elif(text=="今天新竹市天氣"):
        reply_text ="中雨\n降雨機率：100%\n濕度：80%\n風速：37公里/時"
    elif(text=="今天嘉義市天氣"):
        reply_text ="大雨\n降雨機率：100%\n濕度：90%\n風速：41公里/時"
    elif(text=="今天新竹縣天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：12%\n風速：15公里/時"
    elif(text=="今天苗栗縣天氣"):
        reply_text ="多雲\n降雨機率：0%\n濕度：16%\n風速：26公里/時"
    elif(text=="今天彰化縣天氣"):
        reply_text ="陰\n降雨機率：50%\n濕度：55%\n風速：17公里/時"
    elif(text=="今天南投縣天氣"):
        reply_text ="陣雨\n降雨機率：77%\n濕度：64%\n風速：30公里/時"
    elif(text=="今天雲林縣天氣"):
        reply_text ="雷陣雨\n降雨機率：98%\n濕度：80%\n風速：12公里/時"
    elif(text=="今天嘉義縣天氣"):
        reply_text ="小雨\n降雨機率：85%\n濕度：75%\n風速：34公里/時"
    elif(text=="今天屏東縣天氣"):
        reply_text ="中雨\n降雨機率：92%\n濕度：88%\n風速：17公里/時"
    elif(text=="今天宜蘭縣天氣"):
        reply_text ="大雨\n降雨機率：100%\n濕度：90%\n風速：24公里/時"
    elif(text=="今天花蓮縣天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：16%\n風速：45公里/時"
    elif(text=="今天臺東縣天氣"):
        reply_text ="多雲\n降雨機率：15%\n濕度：28%\n風速：29公里/時"
    elif(text=="今天台東縣天氣"):
        reply_text ="多雲\n降雨機率：15%\n濕度：28%\n風速：29公里/時"
    elif(text=="今天澎湖縣天氣"):
        reply_text ="陰\n降雨機率：34%\n濕度：66%\n風速：17公里/時"
    elif(text=="今天金門縣天氣"):
        reply_text ="陣雨\n降雨機率：86%\n濕度：76%\n風速：25公里/時"
    elif(text=="今天連江縣天氣"):
        reply_text ="雷陣雨\n降雨機率：96%\n濕度：86%\n風速：47公里/時"






    elif(text=="明天臺北市天氣"):
        reply_text ="中雨\n降雨機率：92%\n濕度：88%\n風速：17公里/時"
    elif(text=="明天台北市天氣"):
        reply_text ="中雨\n降雨機率：92%\n濕度：88%\n風速：17公里/時"
    elif(text=="明天新北市天氣"):
        reply_text ="雷陣雨\n降雨機率：96%\n濕度：86%\n風速：47公里/時"
    elif(text=="明天桃園市天氣"):
        reply_text ="陰\n降雨機率：30%\n濕度：42%\n風速：27公里/時"
    elif(text=="明天臺中市天氣"):
        reply_text ="雷陣雨\n降雨機率：98%\n濕度：80%\n風速：12公里/時"
    elif(text=="明天台中市天氣"):
        reply_text ="雷陣雨\n降雨機率：98%\n濕度：80%\n風速：12公里/時"
    elif(text=="明天臺南市天氣"):
        reply_text ="陣雨\n降雨機率：77%\n濕度：64%\n風速：30公里/時"
    elif(text=="明天台南市天氣"):
        reply_text ="陣雨\n降雨機率：77%\n濕度：64%\n風速：30公里/時"
    elif(text=="明天高雄市天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：20%\n風速：20公里/時"
    elif(text=="明天基隆市天氣"):
        reply_text ="多雲\n降雨機率：20%\n濕度：25%\n風速：32公里/時"
    elif(text=="明天新竹市天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：16%\n風速：45公里/時"
    elif(text=="明天嘉義市天氣"):
        reply_text ="陰\n降雨機率：30%\n濕度：42%\n風速：27公里/時"
    elif(text=="明天新竹縣天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：16%\n風速：45公里/時"
    elif(text=="明天苗栗縣天氣"):
        reply_text ="多雲\n降雨機率：0%\n濕度：16%\n風速：26公里/時"
    elif(text=="明天彰化縣天氣"):
        reply_text ="大雨\n降雨機率：100%\n濕度：90%\n風速：41公里/時"
    elif(text=="明天南投縣天氣"):
        reply_text ="中雨\n降雨機率：92%\n濕度：88%\n風速：17公里/時"
    elif(text=="明天雲林縣天氣"):
        reply_text ="陣雨\n降雨機率：75%\n濕度：77%\n風速：15公里/時"
    elif(text=="明天嘉義縣天氣"):
        reply_text ="多雲\n降雨機率：20%\n濕度：25%\n風速：32公里/時"
    elif(text=="明天屏東縣天氣"):
        reply_text ="小雨\n降雨機率：70%\n濕度：75%\n風速：15公里/時"
    elif(text=="明天宜蘭縣天氣"):
        reply_text ="雷陣雨\n降雨機率：96%\n濕度：86%\n風速：47公里/時"
    elif(text=="明天花蓮縣天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：20%\n風速：20公里/時"
    elif(text=="明天臺東縣天氣"):
        reply_text ="小雨\n降雨機率：70%\n濕度：75%\n風速：15公里/時"
    elif(text=="明天台東縣天氣"):
        reply_text ="小雨\n降雨機率：70%\n濕度：75%\n風速：15公里/時"
    elif(text=="明天澎湖縣天氣"):
        reply_text ="陣雨\n降雨機率：60%\n濕度：70%\n風速：28公里/時"
    elif(text=="明天金門縣天氣"):
        reply_text ="小雨\n降雨機率：70%\n濕度：75%\n風速：15公里/時"
    elif(text=="明天連江縣天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：30%\n風速：26公里/時"






    elif(text=="後天臺北市天氣"):
        reply_text ="多雲\n降雨機率：15%\n濕度：28%\n風速：29公里/時"
    elif(text=="後天台北市天氣"):
        reply_text ="多雲\n降雨機率：15%\n濕度：28%\n風速：29公里/時"
    elif(text=="後天新北市天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：16%\n風速：45公里/時"
    elif(text=="後天桃園市天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：30%\n風速：26公里/時"
    elif(text=="後天臺中市天氣"):
        reply_text ="陣雨\n降雨機率：86%\n濕度：76%\n風速：25公里/時"
    elif(text=="後天台中市天氣"):
        reply_text ="陣雨\n降雨機率：86%\n濕度：76%\n風速：25公里/時"
    elif(text=="後天臺南市天氣"):
        reply_text ="多雲\n降雨機率：20%\n濕度：25%\n風速：32公里/時"
    elif(text=="後天台南市天氣"):
        reply_text ="多雲\n降雨機率：20%\n濕度：25%\n風速：32公里/時"
    elif(text=="後天高雄市天氣"):
        reply_text ="陣雨\n降雨機率：75%\n濕度：77%\n風速：15公里/時"
    elif(text=="後天基隆市天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：20%\n風速：20公里/時"
    elif(text=="後天新竹市天氣"):
        reply_text ="陰\n降雨機率：50%\n濕度：55%\n風速：17公里/時"
    elif(text=="後天嘉義市天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：16%\n風速：45公里/時"
    elif(text=="後天新竹縣天氣"):
        reply_text ="雷陣雨\n降雨機率：96%\n濕度：86%\n風速：47公里/時"
    elif(text=="後天苗栗縣天氣"):
        reply_text ="多雲\n降雨機率：20%\n濕度：25%\n風速：32公里/時"
    elif(text=="後天彰化縣天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：16%\n風速：45公里/時"
    elif(text=="後天南投縣天氣"):
        reply_text ="陣雨\n降雨機率：86%\n濕度：76%\n風速：25公里/時"
    elif(text=="後天雲林縣天氣"):
        reply_text ="小雨\n降雨機率：70%\n濕度：75%\n風速：15公里/時"
    elif(text=="後天嘉義縣天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：20%\n風速：20公里/時"
    elif(text=="後天屏東縣天氣"):
        reply_text ="大雨\n降雨機率：100%\n濕度：90%\n風速：41公里/時"
    elif(text=="後天宜蘭縣天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：16%\n風速：45公里/時"
    elif(text=="後天花蓮縣天氣"):
        reply_text ="中雨\n降雨機率：92%\n濕度：88%\n風速：17公里/時"
    elif(text=="後天臺東縣天氣"):
        reply_text ="多雲\n降雨機率：0%\n濕度：16%\n風速：26公里/時"
    elif(text=="後天台東縣天氣"):
        reply_text ="多雲\n降雨機率：0%\n濕度：16%\n風速：26公里/時"
    elif(text=="後天澎湖縣天氣"):
        reply_text ="雷陣雨\n降雨機率：98%\n濕度：80%\n風速：12公里/時"
    elif(text=="後天金門縣天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：16%\n風速：45公里/時"
    elif(text=="後天連江縣天氣"):
        reply_text ="多雲\n降雨機率：15%\n濕度：28%\n風速：29公里/時"
    




    elif(text=="臺北市今天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：30%\n風速：26公里/時"
    elif(text=="台北市今天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：30%\n風速：26公里/時"
    elif(text=="新北市今天天氣"):
        reply_text ="多雲\n降雨機率：20%\n濕度：25%\n風速：32公里/時"
    elif(text=="桃園市今天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：20%\n風速：20公里/時"
    elif(text=="臺中市今天天氣"):
        reply_text ="陰\n降雨機率：30%\n濕度：42%\n風速：27公里/時"
    elif(text=="台中市今天天氣"):
        reply_text ="陰\n降雨機率：30%\n濕度：42%\n風速：27公里/時"
    elif(text=="臺南市今天天氣"):
        reply_text ="陣雨\n降雨機率：60%\n濕度：70%\n風速：28公里/時"
    elif(text=="台南市今天天氣"):
        reply_text ="陣雨\n降雨機率：60%\n濕度：70%\n風速：28公里/時"
    elif(text=="高雄市今天天氣"):
        reply_text ="雷陣雨\n降雨機率：100%\n濕度：85%\n風速：45公里/時"
    elif(text=="基隆市今天天氣"):
        reply_text ="小雨\n降雨機率：70%\n濕度：75%\n風速：15公里/時"
    elif(text=="新竹市今天天氣"):
        reply_text ="中雨\n降雨機率：100%\n濕度：80%\n風速：37公里/時"
    elif(text=="嘉義市今天天氣"):
        reply_text ="大雨\n降雨機率：100%\n濕度：90%\n風速：41公里/時"
    elif(text=="新竹縣今天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：12%\n風速：15公里/時"
    elif(text=="苗栗縣今天天氣"):
        reply_text ="多雲\n降雨機率：0%\n濕度：16%\n風速：26公里/時"
    elif(text=="彰化縣今天天氣"):
        reply_text ="陰\n降雨機率：50%\n濕度：55%\n風速：17公里/時"
    elif(text=="南投縣今天天氣"):
        reply_text ="陣雨\n降雨機率：77%\n濕度：64%\n風速：30公里/時"
    elif(text=="雲林縣今天天氣"):
        reply_text ="雷陣雨\n降雨機率：98%\n濕度：80%\n風速：12公里/時"
    elif(text=="嘉義縣今天天氣"):
        reply_text ="小雨\n降雨機率：85%\n濕度：75%\n風速：34公里/時"
    elif(text=="屏東縣今天天氣"):
        reply_text ="中雨\n降雨機率：92%\n濕度：88%\n風速：17公里/時"
    elif(text=="宜蘭縣今天天氣"):
        reply_text ="大雨\n降雨機率：100%\n濕度：90%\n風速：24公里/時"
    elif(text=="花蓮縣今天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：16%\n風速：45公里/時"
    elif(text=="臺東縣今天天氣"):
        reply_text ="多雲\n降雨機率：15%\n濕度：28%\n風速：29公里/時"
    elif(text=="台東縣今天天氣"):
        reply_text ="多雲\n降雨機率：15%\n濕度：28%\n風速：29公里/時"
    elif(text=="澎湖縣今天天氣"):
        reply_text ="陰\n降雨機率：34%\n濕度：66%\n風速：17公里/時"
    elif(text=="金門縣今天天氣"):
        reply_text ="陣雨\n降雨機率：86%\n濕度：76%\n風速：25公里/時"
    elif(text=="連江縣今天天氣"):
        reply_text ="雷陣雨\n降雨機率：96%\n濕度：86%\n風速：47公里/時"






    elif(text=="臺北市明天天氣"):
        reply_text ="中雨\n降雨機率：92%\n濕度：88%\n風速：17公里/時"
    elif(text=="台北市明天天氣"):
        reply_text ="中雨\n降雨機率：92%\n濕度：88%\n風速：17公里/時"
    elif(text=="新北市明天天氣"):
        reply_text ="雷陣雨\n降雨機率：96%\n濕度：86%\n風速：47公里/時"
    elif(text=="桃園市明天天氣"):
        reply_text ="陰\n降雨機率：30%\n濕度：42%\n風速：27公里/時"
    elif(text=="臺中市明天天氣"):
        reply_text ="雷陣雨\n降雨機率：98%\n濕度：80%\n風速：12公里/時"
    elif(text=="台中市明天天氣"):
        reply_text ="雷陣雨\n降雨機率：98%\n濕度：80%\n風速：12公里/時"
    elif(text=="臺南市明天天氣"):
        reply_text ="陣雨\n降雨機率：77%\n濕度：64%\n風速：30公里/時"
    elif(text=="台南市明天天氣"):
        reply_text ="陣雨\n降雨機率：77%\n濕度：64%\n風速：30公里/時"
    elif(text=="高雄市明天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：20%\n風速：20公里/時"
    elif(text=="基隆市明天天氣"):
        reply_text ="多雲\n降雨機率：20%\n濕度：25%\n風速：32公里/時"
    elif(text=="新竹市明天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：16%\n風速：45公里/時"
    elif(text=="嘉義市明天天氣"):
        reply_text ="陰\n降雨機率：30%\n濕度：42%\n風速：27公里/時"
    elif(text=="新竹縣明天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：16%\n風速：45公里/時"
    elif(text=="苗栗縣明天天氣"):
        reply_text ="多雲\n降雨機率：0%\n濕度：16%\n風速：26公里/時"
    elif(text=="彰化縣明天天氣"):
        reply_text ="大雨\n降雨機率：100%\n濕度：90%\n風速：41公里/時"
    elif(text=="南投縣明天天氣"):
        reply_text ="中雨\n降雨機率：92%\n濕度：88%\n風速：17公里/時"
    elif(text=="雲林縣明天天氣"):
        reply_text ="陣雨\n降雨機率：75%\n濕度：77%\n風速：15公里/時"
    elif(text=="嘉義縣明天天氣"):
        reply_text ="多雲\n降雨機率：20%\n濕度：25%\n風速：32公里/時"
    elif(text=="屏東縣明天天氣"):
        reply_text ="小雨\n降雨機率：70%\n濕度：75%\n風速：15公里/時"
    elif(text=="宜蘭縣明天天氣"):
        reply_text ="雷陣雨\n降雨機率：96%\n濕度：86%\n風速：47公里/時"
    elif(text=="花蓮縣明天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：20%\n風速：20公里/時"
    elif(text=="臺東縣明天天氣"):
        reply_text ="小雨\n降雨機率：70%\n濕度：75%\n風速：15公里/時"
    elif(text=="台東縣明天天氣"):
        reply_text ="小雨\n降雨機率：70%\n濕度：75%\n風速：15公里/時"
    elif(text=="澎湖縣明天天氣"):
        reply_text ="陣雨\n降雨機率：60%\n濕度：70%\n風速：28公里/時"
    elif(text=="金門縣明天天氣"):
        reply_text ="小雨\n降雨機率：70%\n濕度：75%\n風速：15公里/時"
    elif(text=="連江縣明天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：30%\n風速：26公里/時"






    elif(text=="臺北市後天天氣"):
        reply_text ="多雲\n降雨機率：15%\n濕度：28%\n風速：29公里/時"
    elif(text=="台北市後天天氣"):
        reply_text ="多雲\n降雨機率：15%\n濕度：28%\n風速：29公里/時"
    elif(text=="新北市後天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：16%\n風速：45公里/時"
    elif(text=="桃園市後天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：30%\n風速：26公里/時"
    elif(text=="臺中市後天天氣"):
        reply_text ="陣雨\n降雨機率：86%\n濕度：76%\n風速：25公里/時"
    elif(text=="台中市後天天氣"):
        reply_text ="陣雨\n降雨機率：86%\n濕度：76%\n風速：25公里/時"
    elif(text=="臺南市後天天氣"):
        reply_text ="多雲\n降雨機率：20%\n濕度：25%\n風速：32公里/時"
    elif(text=="台南市後天天氣"):
        reply_text ="多雲\n降雨機率：20%\n濕度：25%\n風速：32公里/時"
    elif(text=="高雄市後天天氣"):
        reply_text ="陣雨\n降雨機率：75%\n濕度：77%\n風速：15公里/時"
    elif(text=="基隆市後天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：20%\n風速：20公里/時"
    elif(text=="新竹市後天天氣"):
        reply_text ="陰\n降雨機率：50%\n濕度：55%\n風速：17公里/時"
    elif(text=="嘉義市後天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：16%\n風速：45公里/時"
    elif(text=="新竹縣後天天氣"):
        reply_text ="雷陣雨\n降雨機率：96%\n濕度：86%\n風速：47公里/時"
    elif(text=="苗栗縣後天天氣"):
        reply_text ="多雲\n降雨機率：20%\n濕度：25%\n風速：32公里/時"
    elif(text=="彰化縣後天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：16%\n風速：45公里/時"
    elif(text=="南投縣後天天氣"):
        reply_text ="陣雨\n降雨機率：86%\n濕度：76%\n風速：25公里/時"
    elif(text=="雲林縣後天天氣"):
        reply_text ="小雨\n降雨機率：70%\n濕度：75%\n風速：15公里/時"
    elif(text=="嘉義縣後天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：20%\n風速：20公里/時"
    elif(text=="屏東縣後天天氣"):
        reply_text ="大雨\n降雨機率：100%\n濕度：90%\n風速：41公里/時"
    elif(text=="宜蘭縣後天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：16%\n風速：45公里/時"
    elif(text=="花蓮縣後天天氣"):
        reply_text ="中雨\n降雨機率：92%\n濕度：88%\n風速：17公里/時"
    elif(text=="臺東縣後天天氣"):
        reply_text ="多雲\n降雨機率：0%\n濕度：16%\n風速：26公里/時"
    elif(text=="台東縣後天天氣"):
        reply_text ="多雲\n降雨機率：0%\n濕度：16%\n風速：26公里/時"
    elif(text=="澎湖縣後天天氣"):
        reply_text ="雷陣雨\n降雨機率：98%\n濕度：80%\n風速：12公里/時"
    elif(text=="金門縣後天天氣"):
        reply_text ="晴\n降雨機率：0%\n濕度：16%\n風速：45公里/時"
    elif(text=="連江縣後天天氣"):
        reply_text ="多雲\n降雨機率：15%\n濕度：28%\n風速：29公里/時"
    






    elif(text=="今天臺北市帶傘"):
        reply_text ="今天臺北市降雨機率為0％\n外出時不必攜帶雨具"
    elif(text=="今天台北市帶傘"):
        reply_text ="今天台北市降雨機率為0％\n外出時不必攜帶雨具"
    elif(text=="今天新北市帶傘"):
        reply_text ="今天新北市降雨機率為20%\n外出時不必攜帶雨具"
    elif(text=="今天桃園市帶傘"):
        reply_text ="今天桃園市降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="今天臺中市帶傘"):
        reply_text ="今天臺中市降雨機率為30%\n外出時不必攜帶雨具"
    elif(text=="今天台中市帶傘"):
        reply_text ="今天台中市降雨機率為30%\n外出時不必攜帶雨具"
    elif(text=="今天臺南市帶傘"):
        reply_text ="今天臺南市降雨機率為60%\n建議您外出時要攜帶雨具"
    elif(text=="今天台南市帶傘"):
        reply_text ="今天台南市降雨機率為60%\n建議您外出時要攜帶雨具"
    elif(text=="今天高雄市帶傘"):
        reply_text ="今天高雄市降雨機率為100%\n建議您外出時要攜帶雨具"
    elif(text=="今天基隆市帶傘"):
        reply_text ="今天基隆市降雨機率為70%\n建議您外出時要攜帶雨具"
    elif(text=="今天新竹市帶傘"):
        reply_text ="今天新竹市降雨機率為100%\n建議您外出時要攜帶雨具"
    elif(text=="今天嘉義市帶傘"):
        reply_text ="今天嘉義市降雨機率為100%\n建議您外出時要攜帶雨具"
    elif(text=="今天新竹縣帶傘"):
        reply_text ="今天新竹縣降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="今天苗栗縣帶傘"):
        reply_text ="今天苗栗縣降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="今天彰化縣帶傘"):
        reply_text ="今天彰化縣降雨機率為50%\n建議您外出時要攜帶雨具"
    elif(text=="今天南投縣帶傘"):
        reply_text ="今天南投縣降雨機率為77%\n建議您外出時要攜帶雨具"
    elif(text=="今天雲林縣帶傘"):
        reply_text ="今天雲林縣降雨機率為98%\nn建議您外出時要攜帶雨具"
    elif(text=="今天嘉義縣帶傘"):
        reply_text ="今天嘉義縣降雨機率為85%\n建議您外出時要攜帶雨具"
    elif(text=="今天屏東縣帶傘"):
        reply_text ="今天屏東縣降雨機率為92%\n建議您外出時要攜帶雨具"
    elif(text=="今天宜蘭縣帶傘"):
        reply_text ="今天宜蘭縣降雨機率為100%\n建議您外出時要攜帶雨具"
    elif(text=="今天花蓮縣帶傘"):
        reply_text ="今天花蓮縣降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="今天臺東縣帶傘"):
        reply_text ="今天臺東縣降雨機率為15%\n外出時不必攜帶雨具"
    elif(text=="今天台東縣帶傘"):
        reply_text ="今天台東縣降雨機率為15%\n外出時不必攜帶雨具"
    elif(text=="今天澎湖縣帶傘"):
        reply_text ="今天澎湖縣降雨機率為34%\n外出時不必攜帶雨具"
    elif(text=="今天金門縣帶傘"):
        reply_text ="今天金門縣降雨機率：86%\n建議您外出時要攜帶雨具"
    elif(text=="今天連江縣帶傘"):
        reply_text ="今天連江縣降雨機率：96%\n建議您外出時要攜帶雨具"




    elif(text=="明天臺北市帶傘"):
        reply_text ="明天臺北市降雨機率為92%\n建議您外出時要攜帶雨具"
    elif(text=="明天台北市帶傘"):
        reply_text ="明天台北市降雨機率為92%\n建議您外出時要攜帶雨具"
    elif(text=="明天新北市帶傘"):
        reply_text ="明天新北市降雨機率為96%\n建議您外出時要攜帶雨具"
    elif(text=="明天桃園市帶傘"):
        reply_text ="明天桃園市降雨機率為30%\n外出時不必攜帶雨具"
    elif(text=="明天臺中市帶傘"):
        reply_text ="明天臺中市降雨機率為98%\n建議您外出時要攜帶雨具"
    elif(text=="明天台中市帶傘"):
        reply_text ="明天台中市降雨機率為98%\n建議您外出時要攜帶雨具"
    elif(text=="明天臺南市帶傘"):
        reply_text ="明天臺南市降雨機率為77%\n建議您外出時要攜帶雨具"
    elif(text=="明天台南市帶傘"):
        reply_text ="明天台南市降雨機率為77%\n建議您外出時要攜帶雨具"
    elif(text=="明天高雄市帶傘"):
        reply_text ="明天高雄市降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="明天基隆市帶傘"):
        reply_text ="明天基隆市降雨機率為20%\n外出時不必攜帶雨具"
    elif(text=="明天新竹市帶傘"):
        reply_text ="明天新竹市降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="明天嘉義市帶傘"):
        reply_text ="明天嘉義市降雨機率為30%\n外出時不必攜帶雨具"
    elif(text=="明天新竹縣帶傘"):
        reply_text ="明天新竹縣降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="明天苗栗縣帶傘"):
        reply_text ="明天苗栗縣降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="明天彰化縣帶傘"):
        reply_text ="明天彰化縣降雨機率為100%\n建議您外出時要攜帶雨具"
    elif(text=="明天南投縣帶傘"):
        reply_text ="明天南投縣降雨機率為92%\n建議您外出時要攜帶雨具"
    elif(text=="明天雲林縣帶傘"):
        reply_text ="明天雲林縣降雨機率為75%\n建議您外出時要攜帶雨具"
    elif(text=="明天嘉義縣帶傘"):
        reply_text ="明天嘉義縣降雨機率20%\n外出時不必攜帶雨具"
    elif(text=="明天屏東縣帶傘"):
        reply_text ="明天屏東縣降雨機率為70%\n建議您外出時要攜帶雨具"
    elif(text=="明天宜蘭縣帶傘"):
        reply_text ="明天宜蘭縣降雨機率為96%\n建議您外出時要攜帶雨具"
    elif(text=="明天花蓮縣帶傘"):
        reply_text ="明天花蓮縣降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="明天臺東縣帶傘"):
        reply_text ="明天臺東縣降雨機率為70%\n建議您外出時要攜帶雨具"
    elif(text=="明天台東縣帶傘"):
        reply_text ="明天台東縣降雨機率為70%\n建議您外出時要攜帶雨具"
    elif(text=="明天澎湖縣帶傘"):
        reply_text ="明天澎湖縣降雨機率：60%\n建議您外出時要攜帶雨具"
    elif(text=="明天金門縣帶傘"):
        reply_text ="明天金門縣降雨機率：70%\n建議您外出時要攜帶雨具"
    elif(text=="明天連江縣帶傘"):
        reply_text ="明天連江縣降雨機率：0%\n外出時不必攜帶雨具"





    elif(text=="後天臺北市帶傘"):
        reply_text ="後天臺北市降雨機率為15%\n外出時不必攜帶雨具"
    elif(text=="後天台北市帶傘"):
        reply_text ="後天台北市降雨機率為15%\n外出時不必攜帶雨具"
    elif(text=="後天新北市帶傘"):
        reply_text ="後天新北市降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="後天桃園市帶傘"):
        reply_text ="後天桃園市降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="後天臺中市帶傘"):
        reply_text ="後天臺中市降雨機率為86%\n建議您外出時要攜帶雨具"
    elif(text=="後天台中市帶傘"):
        reply_text ="後天台中市降雨機率為86%\n建議您外出時要攜帶雨具"
    elif(text=="後天臺南市帶傘"):
        reply_text ="後天臺南市降雨機率為20%\n外出時不必攜帶雨具"
    elif(text=="後天台南市帶傘"):
        reply_text ="後天台南市降雨機率為20%\n外出時不必攜帶雨具"
    elif(text=="後天高雄市帶傘"):
        reply_text ="後天高雄市降雨機率為75%\n建議您外出時要攜帶雨具"
    elif(text=="後天基隆市帶傘"):
        reply_text ="後天基隆市降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="後天新竹市帶傘"):
        reply_text ="後天新竹市降雨機率為50%\n建議您外出時要攜帶雨具"
    elif(text=="後天嘉義市帶傘"):
        reply_text ="後天嘉義市降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="後天新竹縣帶傘"):
        reply_text ="後天新竹縣降雨機率為96%\n建議您外出時要攜帶雨具"
    elif(text=="後天苗栗縣帶傘"):
        reply_text ="後天苗栗縣降雨機率為20%\n外出時不必攜帶雨具"
    elif(text=="後天彰化縣帶傘"):
        reply_text ="後天彰化縣降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="後天南投縣帶傘"):
        reply_text ="後天南投縣降雨機率為86%\n建議您外出時要攜帶雨具"
    elif(text=="後天雲林縣帶傘"):
        reply_text ="後天雲林縣降雨機率為70%\n建議您外出時要攜帶雨具"
    elif(text=="後天嘉義縣帶傘"):
        reply_text ="後天嘉義縣降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="後天屏東縣帶傘"):
        reply_text ="後天屏東縣降雨機率為100%\n建議您外出時要攜帶雨具"
    elif(text=="後天宜蘭縣帶傘"):
        reply_text ="後天宜蘭縣降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="後天花蓮縣帶傘"):
        reply_text ="後天花蓮縣降雨機率為92%\n建議您外出時要攜帶雨具"
    elif(text=="後天臺東縣帶傘"):
        reply_text ="後天臺東縣降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="後天台東縣帶傘"):
        reply_text ="後天台東縣降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="後天澎湖縣帶傘"):
        reply_text ="後天澎湖縣降雨機率為98%\n建議您外出時要攜帶雨具"
    elif(text=="後天金門縣帶傘"):
        reply_text ="後天金門縣降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="後天連江縣帶傘"):
        reply_text ="後天連江縣降雨機率為15%\n外出時不必攜帶雨具"





    elif(text=="臺北市今天帶傘"):
        reply_text ="臺北市今天降雨機率為0％\n外出時不必攜帶雨具"
    elif(text=="台北市今天帶傘"):
        reply_text ="台北市今天降雨機率為0％\n外出時不必攜帶雨具"
    elif(text=="新北市今天帶傘"):
        reply_text ="新北市今天降雨機率為20%\n外出時不必攜帶雨具"
    elif(text=="桃園市今天帶傘"):
        reply_text ="桃園市今天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="臺中市今天帶傘"):
        reply_text ="臺中市今天降雨機率為30%\n外出時不必攜帶雨具"
    elif(text=="台中市今天帶傘"):
        reply_text ="台中市今天降雨機率為30%\n外出時不必攜帶雨具"
    elif(text=="臺南市今天帶傘"):
        reply_text ="臺南市今天降雨機率為60%\n建議您外出時要攜帶雨具"
    elif(text=="台南市今天帶傘"):
        reply_text ="台南市今天降雨機率為60%\n建議您外出時要攜帶雨具"
    elif(text=="高雄市今天帶傘"):
        reply_text ="高雄市今天降雨機率為100%\n建議您外出時要攜帶雨具"
    elif(text=="基隆市今天帶傘"):
        reply_text ="基隆市今天降雨機率為70%\n建議您外出時要攜帶雨具"
    elif(text=="新竹市今天帶傘"):
        reply_text ="新竹市今天降雨機率為100%\n建議您外出時要攜帶雨具"
    elif(text=="嘉義市今天帶傘"):
        reply_text ="嘉義市今天降雨機率為100%\n建議您外出時要攜帶雨具"
    elif(text=="新竹縣今天帶傘"):
        reply_text ="新竹縣今天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="苗栗縣今天帶傘"):
        reply_text ="苗栗縣今天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="彰化縣今天帶傘"):
        reply_text ="彰化縣今天降雨機率為50%\n建議您外出時要攜帶雨具"
    elif(text=="南投縣今天帶傘"):
        reply_text ="南投縣今天降雨機率為77%\n建議您外出時要攜帶雨具"
    elif(text=="雲林縣今天帶傘"):
        reply_text ="雲林縣今天降雨機率為98%\nn建議您外出時要攜帶雨具"
    elif(text=="嘉義縣今天帶傘"):
        reply_text ="嘉義縣今天降雨機率為85%\n建議您外出時要攜帶雨具"
    elif(text=="屏東縣今天帶傘"):
        reply_text ="屏東縣今天降雨機率為92%\n建議您外出時要攜帶雨具"
    elif(text=="宜蘭縣今天帶傘"):
        reply_text ="宜蘭縣今天降雨機率為100%\n建議您外出時要攜帶雨具"
    elif(text=="花蓮縣今天帶傘"):
        reply_text ="花蓮縣今天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="臺東縣今天帶傘"):
        reply_text ="臺東縣今天降雨機率為15%\n外出時不必攜帶雨具"
    elif(text=="台東縣今天帶傘"):
        reply_text ="台東縣今天降雨機率為15%\n外出時不必攜帶雨具"
    elif(text=="澎湖縣今天帶傘"):
        reply_text ="澎湖縣今天降雨機率為34%\n外出時不必攜帶雨具"
    elif(text=="金門縣今天帶傘"):
        reply_text ="金門縣今天降雨機率：86%\n建議您外出時要攜帶雨具"
    elif(text=="連江縣今天帶傘"):
        reply_text ="連江縣今天降雨機率：96%\n建議您外出時要攜帶雨具"




    elif(text=="臺北市明天帶傘"):
        reply_text ="臺北市明天降雨機率為92%\n建議您外出時要攜帶雨具"
    elif(text=="台北市明天帶傘"):
        reply_text ="台北市明天降雨機率為92%\n建議您外出時要攜帶雨具"
    elif(text=="新北市明天帶傘"):
        reply_text ="新北市明天降雨機率為96%\n建議您外出時要攜帶雨具"
    elif(text=="桃園市明天帶傘"):
        reply_text ="桃園市明天降雨機率為30%\n外出時不必攜帶雨具"
    elif(text=="臺中市明天帶傘"):
        reply_text ="臺中市明天降雨機率為98%\n建議您外出時要攜帶雨具"
    elif(text=="台中市明天帶傘"):
        reply_text ="台中市明天降雨機率為98%\n建議您外出時要攜帶雨具"
    elif(text=="臺南市明天帶傘"):
        reply_text ="臺南市明天降雨機率為77%\n建議您外出時要攜帶雨具"
    elif(text=="台南市明天帶傘"):
        reply_text ="台南市明天降雨機率為77%\n建議您外出時要攜帶雨具"
    elif(text=="高雄市明天帶傘"):
        reply_text ="高雄市明天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="基隆市明天帶傘"):
        reply_text ="基隆市明天降雨機率為20%\n外出時不必攜帶雨具"
    elif(text=="新竹市明天帶傘"):
        reply_text ="新竹市明天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="嘉義市明天帶傘"):
        reply_text ="嘉義市明天降雨機率為30%\n外出時不必攜帶雨具"
    elif(text=="新竹縣明天帶傘"):
        reply_text ="新竹縣明天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="苗栗縣明天帶傘"):
        reply_text ="苗栗縣明天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="彰化縣明天帶傘"):
        reply_text ="彰化縣明天降雨機率為100%\n建議您外出時要攜帶雨具"
    elif(text=="南投縣明天帶傘"):
        reply_text ="南投縣明天降雨機率為92%\n建議您外出時要攜帶雨具"
    elif(text=="雲林縣明天帶傘"):
        reply_text ="雲林縣明天降雨機率為75%\n建議您外出時要攜帶雨具"
    elif(text=="嘉義縣明天帶傘"):
        reply_text ="嘉義縣明天降雨機率20%\n外出時不必攜帶雨具"
    elif(text=="屏東縣明天帶傘"):
        reply_text ="屏東縣明天降雨機率為70%\n建議您外出時要攜帶雨具"
    elif(text=="宜蘭縣明天帶傘"):
        reply_text ="宜蘭縣明天降雨機率為96%\n建議您外出時要攜帶雨具"
    elif(text=="花蓮縣明天帶傘"):
        reply_text ="明天花蓮縣降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="臺東縣明天帶傘"):
        reply_text ="臺東縣明天降雨機率為70%\n建議您外出時要攜帶雨具"
    elif(text=="台東縣明天帶傘"):
        reply_text ="台東縣明天降雨機率為70%\n建議您外出時要攜帶雨具"
    elif(text=="澎湖縣明天帶傘"):
        reply_text ="澎湖縣明天降雨機率：60%\n建議您外出時要攜帶雨具"
    elif(text=="金門縣明天帶傘"):
        reply_text ="金門縣明天降雨機率：70%\n建議您外出時要攜帶雨具"
    elif(text=="連江縣明天帶傘"):
        reply_text ="連江縣明天降雨機率：0%\n外出時不必攜帶雨具"





    elif(text=="臺北市後天帶傘"):
        reply_text ="臺北市後天降雨機率為15%\n外出時不必攜帶雨具"
    elif(text=="台北市後天帶傘"):
        reply_text ="台北市後天降雨機率為15%\n外出時不必攜帶雨具"
    elif(text=="新北市後天帶傘"):
        reply_text ="新北市後天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="桃園市後天帶傘"):
        reply_text ="桃園市後天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="臺中市後天帶傘"):
        reply_text ="臺中市後天降雨機率為86%\n建議您外出時要攜帶雨具"
    elif(text=="台中市後天帶傘"):
        reply_text ="台中市後天降雨機率為86%\n建議您外出時要攜帶雨具"
    elif(text=="臺南市後天帶傘"):
        reply_text ="臺南市後天降雨機率為20%\n外出時不必攜帶雨具"
    elif(text=="台南市後天帶傘"):
        reply_text ="台南市後天降雨機率為20%\n外出時不必攜帶雨具"
    elif(text=="高雄市後天帶傘"):
        reply_text ="高雄市後天降雨機率為75%\n建議您外出時要攜帶雨具"
    elif(text=="基隆市後天帶傘"):
        reply_text ="基隆市後天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="新竹市後天帶傘"):
        reply_text ="新竹市後天降雨機率為50%\n建議您外出時要攜帶雨具"
    elif(text=="嘉義市後天帶傘"):
        reply_text ="嘉義市後天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="新竹縣後天帶傘"):
        reply_text ="新竹縣後天降雨機率為96%\n建議您外出時要攜帶雨具"
    elif(text=="苗栗縣後天帶傘"):
        reply_text ="苗栗縣後天降雨機率為20%\n外出時不必攜帶雨具"
    elif(text=="彰化縣後天帶傘"):
        reply_text ="彰化縣後天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="南投縣後天帶傘"):
        reply_text ="南投縣後天降雨機率為86%\n建議您外出時要攜帶雨具"
    elif(text=="雲林縣後天帶傘"):
        reply_text ="雲林縣後天降雨機率為70%\n建議您外出時要攜帶雨具"
    elif(text=="嘉義縣後天帶傘"):
        reply_text ="嘉義縣後天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="屏東縣後天帶傘"):
        reply_text ="屏東縣後天降雨機率為100%\n建議您外出時要攜帶雨具"
    elif(text=="宜蘭縣後天帶傘"):
        reply_text ="宜蘭縣後天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="花蓮縣後天帶傘"):
        reply_text ="花蓮縣後天降雨機率為92%\n建議您外出時要攜帶雨具"
    elif(text=="臺東縣後天帶傘"):
        reply_text ="臺東縣後天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="台東縣後天帶傘"):
        reply_text ="台東縣後天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="澎湖縣後天帶傘"):
        reply_text ="澎湖縣後天降雨機率為98%\n建議您外出時要攜帶雨具"
    elif(text=="金門縣後天帶傘"):
        reply_text ="金門縣後天降雨機率為0%\n外出時不必攜帶雨具"
    elif(text=="連江縣後天帶傘"):
        reply_text ="連江縣後天降雨機率為15%\n外出時不必攜帶雨具"





    elif(text=="今天臺北市空氣"):
        reply_text ="今天臺北市空氣品質指標AQI為120\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="今天台北市空氣"):
        reply_text ="今天台北市空氣品質指標AQI為120\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="今天新北市空氣"):
        reply_text ="今天新北市空氣品質指標AQI為140\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="今天桃園市空氣"):
        reply_text ="今天桃園市空氣品質指標AQI為20\n空氣品質良好"
    elif(text=="今天臺中市空氣"):
        reply_text ="今天臺中市空氣品質指標AQI為42\n空氣品質良好"
    elif(text=="今天台中市空氣"):
        reply_text ="今天台中市空氣品質指標AQI為42\n空氣品質良好"
    elif(text=="今天臺南市空氣"):
        reply_text ="今天臺南市空氣品質指標AQI為67\n空氣品質普通"
    elif(text=="今天台南市空氣"):
        reply_text ="今天台南市空氣品質指標AQI為67\n空氣品質普通"
    elif(text=="今天高雄市空氣"):
        reply_text ="今天高雄市空氣品質指標AQI為30\n空氣品質良好"
    elif(text=="今天基隆市空氣"):
        reply_text ="今天基隆市空氣品質指標AQI為90\n空氣品質普通"
    elif(text=="今天新竹市空氣"):
        reply_text ="今天新竹市空氣品質指標AQI為25\n空氣品質良好"
    elif(text=="今天嘉義市空氣"):
        reply_text ="今天嘉義市空氣品質指標AQI為210\n非常不健康\n建議您盡量少外出"
    elif(text=="今天新竹縣空氣"):
        reply_text ="今天新竹縣空氣品質指標AQI為20\n空氣品質良好"
    elif(text=="今天苗栗縣空氣"):
        reply_text ="今天苗栗縣空氣品質指標AQI為320\n對健康有危害影響\n建議您盡量少外出"
    elif(text=="今天彰化縣空氣"):
        reply_text ="今天彰化縣空氣品質指標AQI為400\n對健康有危害影響\n建議您盡量少外出"
    elif(text=="今天南投縣空氣"):
        reply_text ="今天南投縣空氣品質指標AQI為160\n對所有族群不健康\n建議您外出時配戴口罩"
    elif(text=="今天雲林縣空氣"):
        reply_text ="今天雲林縣空氣品質指標AQI為34\n空氣品質良好"
    elif(text=="今天嘉義縣空氣"):
        reply_text ="今天嘉義縣空氣品質指標AQI為125\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="今天屏東縣空氣"):
        reply_text ="今天屏東縣空氣品質指標AQI為26\n空氣品質良好"
    elif(text=="今天宜蘭縣空氣"):
        reply_text ="今天宜蘭縣空氣品質指標AQI為140\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="今天花蓮縣空氣"):
        reply_text ="今天花蓮縣空氣品質指標AQI為10\n空氣品質良好"
    elif(text=="今天臺東縣空氣"):
        reply_text ="今天臺東縣空氣品質指標AQI為15\n空氣品質良好"
    elif(text=="今天台東縣空氣"):
        reply_text ="今天台東縣空氣品質指標AQI為15\n空氣品質良好"
    elif(text=="今天澎湖縣空氣"):
        reply_text ="今天澎湖縣空氣品質指標AQI為48\n空氣品質良好"
    elif(text=="今天金門縣空氣"):
        reply_text ="今天金門縣空氣品質指標AQI為24\n空氣品質良好"
    elif(text=="今天連江縣空氣"):
        reply_text ="今天連江縣空氣品質指標AQI為36\n空氣品質良好"





    elif(text=="明天臺北市空氣"):
        reply_text ="明天臺北市空氣品質指標AQI為90\n空氣品質普通"
    elif(text=="明天台北市空氣"):
        reply_text ="明天台北市空氣品質指標AQI為90\n空氣品質普通"
    elif(text=="明天新北市空氣"):
        reply_text ="明天新北市空氣品質指標AQI為67\n空氣品質普通"
    elif(text=="明天桃園市空氣"):
        reply_text ="明天桃園市空氣品質指標AQI為120\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="明天臺中市空氣"):
        reply_text ="明天臺中市空氣品質指標AQI為25\n空氣品質良好"
    elif(text=="明天台中市空氣"):
        reply_text ="明天台中市空氣品質指標AQI為25\n空氣品質良好"
    elif(text=="明天臺南市空氣"):
        reply_text ="明天臺南市空氣品質指標AQI為90\n空氣品質普通"
    elif(text=="明天台南市空氣"):
        reply_text ="明天台南市空氣品質指標AQI為90\n空氣品質普通"
    elif(text=="明天高雄市空氣"):
        reply_text ="明天高雄市空氣品質指標AQI為15\n空氣品質良好"
    elif(text=="明天基隆市空氣"):
        reply_text ="明天基隆市空氣品質指標AQI為210\n非常不健康\n建議您盡量少外出"
    elif(text=="明天新竹市空氣"):
        reply_text ="明天新竹市空氣品質指標AQI為25\n空氣品質良好"
    elif(text=="明天嘉義市空氣"):
        reply_text ="明天嘉義市空氣品質指標AQI為320\n對健康有危害影響\n建議您盡量少外出"
    elif(text=="明天新竹縣空氣"):
        reply_text ="明天新竹縣空氣品質指標AQI為48\n空氣品質良好"
    elif(text=="明天苗栗縣空氣"):
        reply_text ="明天苗栗縣空氣品質指標AQI為42\n空氣品質良好"
    elif(text=="明天彰化縣空氣"):
        reply_text ="明天彰化縣空氣品質指標AQI為320\n對健康有危害影響\n建議您盡量少外出"
    elif(text=="明天南投縣空氣"):
        reply_text ="明天南投縣空氣品質指標AQI為140\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="明天雲林縣空氣"):
        reply_text ="明天雲林縣空氣品質指標AQI為67\n空氣品質普通"
    elif(text=="明天嘉義縣空氣"):
        reply_text ="明天嘉義縣空氣品質指標AQI為36\n空氣品質良好"
    elif(text=="明天屏東縣空氣"):
        reply_text ="明天屏東縣空氣品質指標AQI為30\n空氣品質良好"
    elif(text=="明天宜蘭縣空氣"):
        reply_text ="明天宜蘭縣空氣品質指標AQI為26\n空氣品質良好"
    elif(text=="明天花蓮縣空氣"):
        reply_text ="明天花蓮縣空氣品質指標AQI為15\n空氣品質良好"
    elif(text=="明天臺東縣空氣"):
        reply_text ="明天臺東縣空氣品質指標AQI為36\n空氣品質良好"
    elif(text=="明天台東縣空氣"):
        reply_text ="明天台東縣空氣品質指標AQI為42\n空氣品質良好"
    elif(text=="明天澎湖縣空氣"):
        reply_text ="明天澎湖縣空氣品質指標AQI為125\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="明天金門縣空氣"):
        reply_text ="明天金門縣空氣品質指標AQI為67\n空氣品質普通"
    elif(text=="明天連江縣空氣"):
        reply_text ="明天連江縣空氣品質指標AQI為90\n空氣品質普通"






    elif(text=="後天臺北市空氣"):
        reply_text ="後天臺北市空氣品質指標AQI為140\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="後天台北市空氣"):
        reply_text ="後天台北市空氣品質指標AQI為140\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="後天新北市空氣"):
        reply_text ="後天新北市空氣品質指標AQI為125\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="後天桃園市空氣"):
        reply_text ="後天桃園市空氣品質指標AQI為25\n空氣品質良好"
    elif(text=="後天臺中市空氣"):
        reply_text ="後天臺中市空氣品質指標AQI為26\n空氣品質良好"
    elif(text=="後天台中市空氣"):
        reply_text ="後天台中市空氣品質指標AQI為26\n空氣品質良好"
    elif(text=="後天臺南市空氣"):
        reply_text ="後天臺南市空氣品質指標AQI為36\n空氣品質良好"
    elif(text=="後天台南市空氣"):
        reply_text ="後天台南市空氣品質指標AQI為36\n空氣品質良好"
    elif(text=="後天高雄市空氣"):
        reply_text ="後天高雄市空氣品質指標AQI為320\n對健康有危害影響\n建議您盡量少外出"
    elif(text=="後天基隆市空氣"):
        reply_text ="後天基隆市空氣品質指標AQI為36\n空氣品質良好"
    elif(text=="後天新竹市空氣"):
        reply_text ="後天新竹市空氣品質指標AQI為15\n空氣品質良好"
    elif(text=="後天嘉義市空氣"):
        reply_text ="後天嘉義市空氣品質指標AQI為42\n空氣品質良好"
    elif(text=="後天新竹縣空氣"):
        reply_text ="後天新竹縣空氣品質指標AQI為26\n空氣品質良好"
    elif(text=="後天苗栗縣空氣"):
        reply_text ="後天苗栗縣空氣品質指標AQI為90\n空氣品質普通"
    elif(text=="後天彰化縣空氣"):
        reply_text ="後天彰化縣空氣品質指標AQI為320\n對健康有危害影響\n建議您盡量少外出"
    elif(text=="後天南投縣空氣"):
        reply_text ="後天南投縣空氣品質指標AQI為90\n空氣品質普通"
    elif(text=="後天雲林縣空氣"):
        reply_text ="後天雲林縣空氣品質指標AQI為67\n空氣品質普通"
    elif(text=="後天嘉義縣空氣"):
        reply_text ="後天嘉義縣空氣品質指標AQI為25\n空氣品質良好"
    elif(text=="後天屏東縣空氣"):
        reply_text ="後天屏東縣空氣品質指標AQI為30\n空氣品質良好"
    elif(text=="後天宜蘭縣空氣"):
        reply_text ="後天宜蘭縣空氣品質指標AQI為15\n空氣品質良好"
    elif(text=="後天花蓮縣空氣"):
        reply_text ="後天花蓮縣空氣品質指標AQI為42\n空氣品質良好"
    elif(text=="後天臺東縣空氣"):
        reply_text ="後天臺東縣空氣品質指標AQI為67\n空氣品質普通"
    elif(text=="後天台東縣空氣"):
        reply_text ="後天台東縣空氣品質指標AQI為90\n空氣品質普通"
    elif(text=="後天澎湖縣空氣"):
        reply_text ="後天澎湖縣空氣品質指標AQI為42\n空氣品質良好"
    elif(text=="後天金門縣空氣"):
        reply_text ="後天金門縣空氣品質指標AQI為26\n空氣品質良好"
    elif(text=="後天連江縣空氣"):
        reply_text ="後天連江縣空氣品質指標AQI為48\n空氣品質良好"







    elif(text=="臺北市今天空氣"):
        reply_text ="臺北市今天空氣品質指標AQI為120\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="台北市今天空氣"):
        reply_text ="台北市今天空氣品質指標AQI為120\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="新北市今天空氣"):
        reply_text ="新北市今天空氣品質指標AQI為140\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="桃園市今天空氣"):
        reply_text ="桃園市今天空氣品質指標AQI為20\n空氣品質良好"
    elif(text=="臺中市今天空氣"):
        reply_text ="臺中市今天空氣品質指標AQI為42\n空氣品質良好"
    elif(text=="台中市今天空氣"):
        reply_text ="台中市今天空氣品質指標AQI為42\n空氣品質良好"
    elif(text=="臺南市今天空氣"):
        reply_text ="臺南市今天空氣品質指標AQI為67\n空氣品質普通"
    elif(text=="台南市今天空氣"):
        reply_text ="台南市今天空氣品質指標AQI為67\n空氣品質普通"
    elif(text=="高雄市今天空氣"):
        reply_text ="高雄市今天空氣品質指標AQI為30\n空氣品質良好"
    elif(text=="基隆市今天空氣"):
        reply_text ="基隆市今天空氣品質指標AQI為90\n空氣品質普通"
    elif(text=="今天新竹市空氣"):
        reply_text ="今天新竹市空氣品質指標AQI為25\n空氣品質良好"
    elif(text=="嘉義市今天空氣"):
        reply_text ="嘉義市今天空氣品質指標AQI為210\n非常不健康\n建議您盡量少外出"
    elif(text=="新竹縣今天空氣"):
        reply_text ="新竹縣今天空氣品質指標AQI為20\n空氣品質良好"
    elif(text=="苗栗縣今天空氣"):
        reply_text ="苗栗縣今天空氣品質指標AQI為320\n對健康有危害影響\n建議您盡量少外出"
    elif(text=="彰化縣今天空氣"):
        reply_text ="彰化縣今天空氣品質指標AQI為400\n對健康有危害影響\n建議您盡量少外出"
    elif(text=="今天南投縣空氣"):
        reply_text ="今天南投縣空氣品質指標AQI為160\n對所有族群不健康\n建議您外出時配戴口罩"
    elif(text=="雲林縣今天空氣"):
        reply_text ="雲林縣今天空氣品質指標AQI為34\n空氣品質良好"
    elif(text=="嘉義縣今天空氣"):
        reply_text ="嘉義縣今天空氣品質指標AQI為125\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="屏東縣今天空氣"):
        reply_text ="屏東縣今天空氣品質指標AQI為26\n空氣品質良好"
    elif(text=="宜蘭縣今天空氣"):
        reply_text ="宜蘭縣今天空氣品質指標AQI為140\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="花蓮縣今天空氣"):
        reply_text ="花蓮縣今天空氣品質指標AQI為10\n空氣品質良好"
    elif(text=="臺東縣今天空氣"):
        reply_text ="臺東縣今天空氣品質指標AQI為15\n空氣品質良好"
    elif(text=="台東縣今天空氣"):
        reply_text ="台東縣今天空氣品質指標AQI為15\n空氣品質良好"
    elif(text=="澎湖縣今天空氣"):
        reply_text ="澎湖縣今天空氣品質指標AQI為48\n空氣品質良好"
    elif(text=="金門縣今天空氣"):
        reply_text ="金門縣今天空氣品質指標AQI為24\n空氣品質良好"
    elif(text=="連江縣今天空氣"):
        reply_text ="連江縣今天空氣品質指標AQI為36\n空氣品質良好"





    elif(text=="臺北市明天空氣"):
        reply_text ="臺北市明天空氣品質指標AQI為90\n空氣品質普通"
    elif(text=="台北市明天空氣"):
        reply_text ="台北市明天空氣品質指標AQI為90\n空氣品質普通"
    elif(text=="新北市明天空氣"):
        reply_text ="新北市明天空氣品質指標AQI為67\n空氣品質普通"
    elif(text=="桃園市明天空氣"):
        reply_text ="桃園市明天空氣品質指標AQI為120\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="臺中市明天空氣"):
        reply_text ="臺中市明天空氣品質指標AQI為25\n空氣品質良好"
    elif(text=="台中市明天空氣"):
        reply_text ="台中市明天空氣品質指標AQI為25\n空氣品質良好"
    elif(text=="臺南市明天空氣"):
        reply_text ="臺南市明天空氣品質指標AQI為90\n空氣品質普通"
    elif(text=="台南市明天空氣"):
        reply_text ="台南市明天空氣品質指標AQI為90\n空氣品質普通"
    elif(text=="高雄市明天空氣"):
        reply_text ="高雄市明天空氣品質指標AQI為15\n空氣品質良好"
    elif(text=="基隆市明天空氣"):
        reply_text ="基隆市明天空氣品質指標AQI為210\n非常不健康\n建議您盡量少外出"
    elif(text=="新竹市明天空氣"):
        reply_text ="新竹市明天空氣品質指標AQI為25\n空氣品質良好"
    elif(text=="嘉義市明天空氣"):
        reply_text ="嘉義市明天空氣品質指標AQI為320\n對健康有危害影響\n建議您盡量少外出"
    elif(text=="新竹縣明天空氣"):
        reply_text ="新竹縣明天空氣品質指標AQI為48\n空氣品質良好"
    elif(text=="苗栗縣明天空氣"):
        reply_text ="苗栗縣明天空氣品質指標AQI為42\n空氣品質良好"
    elif(text=="彰化縣明天空氣"):
        reply_text ="彰化縣明天空氣品質指標AQI為320\n對健康有危害影響\n建議您盡量少外出"
    elif(text=="南投縣明天空氣"):
        reply_text ="南投縣明天空氣品質指標AQI為140\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="雲林縣明天空氣"):
        reply_text ="雲林縣明天空氣品質指標AQI為67\n空氣品質普通"
    elif(text=="嘉義縣明天空氣"):
        reply_text ="嘉義縣明天空氣品質指標AQI為36\n空氣品質良好"
    elif(text=="屏東縣明天空氣"):
        reply_text ="屏東縣明天空氣品質指標AQI為30\n空氣品質良好"
    elif(text=="宜蘭縣明天空氣"):
        reply_text ="宜蘭縣明天空氣品質指標AQI為26\n空氣品質良好"
    elif(text=="花蓮縣明天空氣"):
        reply_text ="花蓮縣明天空氣品質指標AQI為15\n空氣品質良好"
    elif(text=="臺東縣明天空氣"):
        reply_text ="臺東縣明天空氣品質指標AQI為36\n空氣品質良好"
    elif(text=="台東縣明天空氣"):
        reply_text ="台東縣明天空氣品質指標AQI為42\n空氣品質良好"
    elif(text=="澎湖縣明天空氣"):
        reply_text ="澎湖縣明天空氣品質指標AQI為125\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="金門縣明天空氣"):
        reply_text ="金門縣明天空氣品質指標AQI為67\n空氣品質普通"
    elif(text=="連江縣明天空氣"):
        reply_text ="連江縣明天空氣品質指標AQI為90\n空氣品質普通"






    elif(text=="臺北市後天空氣"):
        reply_text ="臺北市後天空氣品質指標AQI為140\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="台北市後天空氣"):
        reply_text ="台北市後天空氣品質指標AQI為140\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="新北市後天空氣"):
        reply_text ="新北市後天空氣品質指標AQI為125\n對敏感族群不健康\n建議您外出時配戴口罩"
    elif(text=="桃園市後天空氣"):
        reply_text ="桃園市後天空氣品質指標AQI為25\n空氣品質良好"
    elif(text=="臺中市後天空氣"):
        reply_text ="臺中市後天空氣品質指標AQI為26\n空氣品質良好"
    elif(text=="台中市後天空氣"):
        reply_text ="台中市後天空氣品質指標AQI為26\n空氣品質良好"
    elif(text=="臺南市後天空氣"):
        reply_text ="臺南市後天空氣品質指標AQI為36\n空氣品質良好"
    elif(text=="台南市後天空氣"):
        reply_text ="台南市後天空氣品質指標AQI為36\n空氣品質良好"
    elif(text=="高雄市後天空氣"):
        reply_text ="高雄市後天空氣品質指標AQI為320\n對健康有危害影響\n建議您盡量少外出"
    elif(text=="基隆市後天空氣"):
        reply_text ="基隆市後天空氣品質指標AQI為36\n空氣品質良好"
    elif(text=="新竹市後天空氣"):
        reply_text ="新竹市後天空氣品質指標AQI為15\n空氣品質良好"
    elif(text=="嘉義市後天空氣"):
        reply_text ="嘉義市後天空氣品質指標AQI為42\n空氣品質良好"
    elif(text=="新竹縣後天空氣"):
        reply_text ="新竹縣後天空氣品質指標AQI為26\n空氣品質良好"
    elif(text=="苗栗縣後天空氣"):
        reply_text ="苗栗縣後天空氣品質指標AQI為90\n空氣品質普通"
    elif(text=="彰化縣後天空氣"):
        reply_text ="彰化縣後天空氣品質指標AQI為320\n對健康有危害影響\n建議您盡量少外出"
    elif(text=="南投縣後天空氣"):
        reply_text ="南投縣後天空氣品質指標AQI為90\n空氣品質普通"
    elif(text=="雲林縣後天空氣"):
        reply_text ="雲林縣後天空氣品質指標AQI為67\n空氣品質普通"
    elif(text=="嘉義縣後天空氣"):
        reply_text ="嘉義縣後天空氣品質指標AQI為25\n空氣品質良好"
    elif(text=="屏東縣後天空氣"):
        reply_text ="屏東縣後天空氣品質指標AQI為30\n空氣品質良好"
    elif(text=="宜蘭縣後天空氣"):
        reply_text ="宜蘭縣後天空氣品質指標AQI為15\n空氣品質良好"
    elif(text=="花蓮縣後天空氣"):
        reply_text ="花蓮縣後天空氣品質指標AQI為42\n空氣品質良好"
    elif(text=="臺東縣後天空氣"):
        reply_text ="臺東縣後天空氣品質指標AQI為67\n空氣品質普通"
    elif(text=="台東縣後天空氣"):
        reply_text ="台東縣後天空氣品質指標AQI為90\n空氣品質普通"
    elif(text=="澎湖縣後天空氣"):
        reply_text ="澎湖縣後天空氣品質指標AQI為42\n空氣品質良好"
    elif(text=="金門縣後天空氣"):
        reply_text ="金門縣後天空氣品質指標AQI為26\n空氣品質良好"
    elif(text=="連江縣後天空氣"):
        reply_text ="連江縣後天空氣品質指標AQI為48\n空氣品質良好"



    else:  
        reply_text = "很抱歉！我不太明白您的意思，您可以輸入 help 查看目前支援指令，以及其說明。例如：今天桃園市天氣、臺北市明天空氣、後天臺中市帶傘。"
    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
