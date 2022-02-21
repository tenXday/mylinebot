from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Script_type,Script_pnumber,Script_list# 引入資料模型

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import (MessageEvent, TextSendMessage,ImageCarouselTemplate, 
                                TemplateSendMessage, ImageCarouselColumn, ImageSendMessage, 
                                CarouselTemplate,CarouselColumn,ButtonsTemplate,MessageAction,
                                URIAction,LocationSendMessage)


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):  # 如果有訊息事件
                if event.message.text =="test":
                    profile = line_bot_api.get_profile(event.source.user_id)
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(
                            text=profile.user_id
                        )
                    ) 
                    
                if event.message.text == "劇本查詢":
                    s_type = Script_type.objects.all()
                    reply_arr=[]
                    output = []
                    for stype in s_type:
                        output.append(
                            CarouselColumn(
                                thumbnail_image_url=stype.photo,
                                title=stype.type,
                                text=" ",
                                actions=[
                                    MessageAction(
                                        label='查詢',
                                        text=stype.type
                                    )                                    
                                ]
                            )
                        )
                    reply_arr.append(
                        TemplateSendMessage(
                            alt_text='Carousel template',
                            template=CarouselTemplate(
                                columns=output
                            )
                        )
                    )
                    output=[]
                    s_pnumber=Script_pnumber.objects.all()
                    for spnumber in s_pnumber:
                        output.append(
                            CarouselColumn(
                                thumbnail_image_url=spnumber.photo,
                                title=spnumber.pnumber,
                                text=" ",
                                actions=[
                                    MessageAction(
                                        label='查詢',
                                        text=spnumber.pnumber
                                    )                                    
                                ]
                            )
                        )
                    reply_arr.append(
                        TemplateSendMessage(
                            alt_text='Carousel template',
                            template=CarouselTemplate(
                                columns=output
                            )
                        )
                    )
            
                    line_bot_api.reply_message(
                        event.reply_token,reply_arr
                    )

                #-----------------------------------------------------------------------------------------------
                S_list=Script_list.objects.filter(type=event.message.text)
                if len(S_list)>0 :
                    output=[]
                    for script in S_list:
                        output.append(
                            ImageCarouselColumn(
                                image_url=script.photo,
                                action=MessageAction(
                                        label='介紹',
                                        text=script.sname
                                    )
                                )
                        )
                    line_bot_api.reply_message(
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='ImageCarousel template',
                            template=ImageCarouselTemplate(
                                columns=output
                            )
                        )
                    )


                S_list=Script_list.objects.filter(pnumber=event.message.text)
                if len(S_list)>0 :
                    output=[]
                    for script in S_list:
                        output.append(
                            ImageCarouselColumn(
                                image_url=script.photo,
                                action=MessageAction(
                                        label='介紹',
                                        text=script.sname
                                    )
                                )
                        )
                    line_bot_api.reply_message(
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='ImageCarousel template',
                            template=ImageCarouselTemplate(
                                columns=output
                            )
                        )
                    )
                #---------------------------------------------------------------------------------------

                S_intro=Script_list.objects.filter(sname=event.message.text)
                if len(S_intro)>0 :
                    line_bot_api.reply_message(
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='ImageCarousel template',
                            template=ButtonsTemplate(
                                        thumbnail_image_url=S_intro[0].photo,
                                        title=S_intro[0].sname,
                                        text=S_intro[0].intro,
                                        actions=[
                                            URIAction(
                                                label='預約',
                                                uri='https://larplus.simplybook.asia/v2/#'
                                            )
                                        ]
                                    )
                            )
                        )
                if  event.message.text=="店址資訊" :
                    reply_arr=[]
                    reply_arr.append(
                        LocationSendMessage(
                            title='拉普拉斯LARPlus推理聚場(科技大樓店)',
                            address='106台北市大安區和平東路二段175巷33號',
                            latitude=25.0269953139313,
                            longitude= 121.54231416445494
                        )
                    )
                    reply_arr.append(
                        LocationSendMessage(
                            title='拉普拉斯LARPlus推理聚場(微風店)',
                            address='10556台北市松山區八德路二段346巷3弄19號',
                            latitude=25.047781260416134,
                            longitude=  121.54637372768076
                        )
                    )
                    line_bot_api.reply_message(
                        event.reply_token,reply_arr
                    )        
                # Sp_list=Script_list.objects.filter(sname=event.message.text)
                # if len(Sp_list)>0 :
                #     line_bot_api.reply_message(
                #         event.reply_token,
                #         ImageSendMessage(
                #             original_content_url=Script_list[0].intro,
                #             preview_image_url=Script_list[0].intro
                #         )
                #     )        
                    # reply_arr=[]
                    # reply_arr.append(TemplateSendMessage(
                    #         alt_text='ImageCarousel template',
                    #         template=ImageCarouselTemplate(
                    #             columns=output
                    #         )
                            
                    #     ))
                    # reply_arr.append(TemplateSendMessage(
                    #         alt_text='ImageCarousel template',
                    #         template=ImageCarouselTemplate(
                    #             columns=output
                    #         )
                            
                    #     ))    
                    
                    
        return HttpResponse()
    else:
        return HttpResponseBadRequest()