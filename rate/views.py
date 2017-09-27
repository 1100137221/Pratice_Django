from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re 

# Create your views here.

class rateModel:
    def __init__(self, countryName, countryImg,
                        buyCashRate, sellCashRate,
                        buySpotRate, sellSpotRate):
        self.countryName = countryName
        self.countryImg = countryImg
        self.buyCashRate = buyCashRate
        self.sellCashRate = sellCashRate
        self.buySpotRate = buySpotRate
        self.sellSpotRate = sellSpotRate

def rate(request):
    
    p=re.compile('\s+') 

    res = requests.get("http://rate.bot.com.tw/xrt?Lang=zh-TW")
    soup = BeautifulSoup(res.content,"html5lib")
    rateImgSrc = "http://rate.bot.com.tw"

    data = []

    for idx0,item in enumerate(soup.select("table tr")):
        if idx0 > 2: #標頭後的才是資料
            data.append(rateModel(  re.sub(p,'',item.select("td .print_show")[0].text),
                                    rateImgSrc + item.select("img")[0]["src"],
                                    item.select("td")[1].text,
                                    item.select("td")[2].text,
                                    item.select("td")[3].text,
                                    item.select("td")[4].text))
    print(data)
    
    return render(request, 'rate.html',{
                'rateList': data
            })