from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re 
from rate.models import Rate

from rate.serializers import RateSerializer
from rest_framework import viewsets

# Create your views here.


def rate(request):
    
    bank = "esun"
    
    #判斷是選擇哪家銀行匯率
    if request.GET.get('bankSelect') == None or request.GET.get('bankSelect') == "1" :
        bank = "esun"
    else:
        bank = "taiwan"

    #先刪除之前的資料
    Rate.objects.filter(bank=bank).delete()

    if bank == "esun" :
        esunRate(bank)
    else:
        taiwanRate(bank)

    return render(request, 'rate.html',{
                'rateList': Rate.objects.filter(bank=bank),
                'bank': bank
            })


#抓取台灣銀行匯率的邏輯
def taiwanRate(bank):
    p=re.compile('\s+') 

    res = requests.get("http://rate.bot.com.tw/xrt?Lang=zh-TW")
    soup = BeautifulSoup(res.content,"html5lib")
    rateImgSrc = "http://rate.bot.com.tw"

    for idx0,item in enumerate(soup.select("table tr")):
        if idx0 > 2: #標頭後的才是資料
            countryName=re.sub(p,'',item.select("td .print_show")[0].text)
            buyCashRate = 0
            sellCashRate = 0
            buySpotRate = 0
            sellSpotRate = 0
            if item.select("td")[1].text != "-" :
                 buyCashRate=  float(item.select("td")[1].text) 
            if item.select("td")[2].text != "-" :
                sellCashRate= float(item.select("td")[2].text)
            if item.select("td")[3].text != "-" :
                buySpotRate= float(item.select("td")[3].text)
            if item.select("td")[4].text != "-" :
                sellSpotRate= float(item.select("td")[4].text)
            Rate.objects.create(countryName=countryName,
                                buyCashRate=buyCashRate,
                                sellCashRate=sellCashRate,
                                buySpotRate=buySpotRate,
                                sellSpotRate=sellSpotRate,
                                bank=bank)

#抓取玉山銀行匯率的邏輯
def esunRate(bank):
    p=re.compile('\s+') 

    res = requests.get("https://www.esunbank.com.tw/bank/personal/deposit/rate/forex/foreign-exchange-rates")
    soup = BeautifulSoup(res.content,"html5lib")
    rateImgSrc = "https://www.esunbank.com.tw/bank/personal/deposit/rate/forex/"

    data = []

    for idx0,item in enumerate(soup.select("#inteTable1 .tableContent-light")):


        countryName=re.sub(p,'',item.select("td")[0].text)
        buyCashRate = 0
        sellCashRate = 0
        buySpotRate = 0
        sellSpotRate = 0
        if re.sub(p,'',item.select("td")[3].text) != "" :
                buyCashRate=  float(item.select("td")[3].text) 
        if re.sub(p,'',item.select("td")[4].text) != "" :
            sellCashRate= float(item.select("td")[4].text)
        if re.sub(p,'',item.select("td")[1].text) != "" :
            buySpotRate= float(item.select("td")[1].text)
        if re.sub(p,'',item.select("td")[2].text) != "" :
            sellSpotRate= float(item.select("td")[2].text)

        Rate.objects.create(countryName=countryName,
                            img = rateImgSrc + item.select("img")[0]["src"],
                            buyCashRate=buyCashRate,
                            sellCashRate=sellCashRate,
                            buySpotRate=buySpotRate,
                            sellSpotRate=sellSpotRate,
                            bank=bank)



# Create your views here.
class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer