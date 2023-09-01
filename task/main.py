#https://card.wb.ru/cards/detail?appType=1&curr=rub&dest=-1257786&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,1,31,66,22,110,48,71,114&spp=0&nm=64245978
#Товар там есть root
#https://feedbacks2.wb.ru/feedbacks/v1/48718998
#Тут лежат отзывы
#url_feedbacks1 = f"https://feedbacks1.wb.ru/feedbacks/v1/{root}"
#url_feedbacks2 = f"https://feedbacks2.wb.ru/feedbacks/v1/{root}"


"""
На текущий момент он собирает все отзывы и отсылает в телегу на бота, а бот соответственно отсылает их мне
Можно сделать 

"""

import requests
import json

messages = []
def parse(id:str):
    url = f"https://card.wb.ru/cards/detail?appType=1&curr=rub&dest=-1257786&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,1,31,66,22,110,48,71,114&spp=0&nm={id}"
    site = requests.get(url)
    content = json.loads(site.content)
    root = content['data']['products'][0]['root']
    print(content['data']['products'][0]['root'])
    
    feedback_status = "Негативный отзыв"
    product_name = content['data']['products'][0]['name']
    sku = id
    star = int()
    text = ''
    total_rating = content['data']['products'][0]['reviewRating']
        #print(f'{}')
    
    
    url_feedbacks1 = f"https://feedbacks1.wb.ru/feedbacks/v1/{root}"
    url_feedbacks2 = f"https://feedbacks2.wb.ru/feedbacks/v1/{root}"
    feedbacks = json.loads(requests.get(url_feedbacks1).content)
    
    if feedbacks['feedbacks'] == None:
        feedbacks = json.loads(requests.get(url_feedbacks2).content)

        
    total_reviews = feedbacks['feedbackCountWithText']
    
    
    for i in range(len(feedbacks['feedbacks'])):
        star = int(feedbacks['feedbacks'][i]['productValuation'])
        
        if star > 4:
            continue
        
        text = feedbacks['feedbacks'][i]['text']
        message = f"{feedback_status} / {product_name} / {sku} / {star} / {text} / {total_rating}"
        messages.append(message)
    
    TOKEN = "5914047175:AAFA-S9m_UJsseXP20UYgkut9dG7eeRQkj4"
    chat_id = "441485120"
    
    for message in messages:
        url_tg = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url_tg).json())
    #Дальше идёт на телеграм
    #print(content2)


if __name__ == "__main__":
    parse('64245978')