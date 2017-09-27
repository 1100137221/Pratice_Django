from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re 

class weatherＭodel:
    def __init__(self,title,temperature,imgUrl):
        self.title = title
        self.temperature = temperature
        self.imgUrl = imgUrl

def weather(request):

    p=re.compile('\s+') 

    result = requests.get('http://www.cwb.gov.tw/V7/forecast/week/week.htm')
    result.encoding = 'UTF-8'
    soup = BeautifulSoup(result.text,"html5lib")

    weatherImgSrc = "http://www.cwb.gov.tw/V7/"
    weatherList = []

    for itemIdx,item in enumerate(soup.select('.BoxTableInside tr')):
        data = []
        if itemIdx == 0 :
            for titleItem in item.select("th"):
                    data.append(weatherＭodel(titleItem.text,'',''))
        else:
            country = item.select("th")
            
            if len(country) == 9:
                continue;
            if len(country) == 1: #抓取城市的判斷
                data.append(weatherＭodel(country[0].text,'',''))
            else:
                data.append(weatherＭodel('','','')) 
            for bodyIdx,bodyItem in enumerate(item.select("td")) :
                if bodyIdx == 0 : 
                    data.append(weatherＭodel(bodyItem.text,'',''))
                else :
                    data.append(weatherＭodel(bodyItem.select('img')[0]['title'],
                                        re.sub(p,'',bodyItem.text),
                                        weatherImgSrc + bodyItem.select('img')[0]['src'].replace("../../","")))
        weatherList.append(data)
        
        
    print(weatherList)
        

    return render(request, 'weather.html', {
        'weatherList': weatherList,
    })





