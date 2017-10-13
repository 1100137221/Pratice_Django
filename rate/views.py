from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re 
from rate.models import Rate

from rate.serializers import RateSerializer
from rest_framework import viewsets

# Create your views here.


def rate(request):
    
    #先刪除資料
    Rate.objects.all().delete()

    p=re.compile('\s+') 

    res = requests.get("http://rate.bot.com.tw/xrt?Lang=zh-TW")
    soup = BeautifulSoup(res.content,"html5lib")
    rateImgSrc = "http://rate.bot.com.tw"

    data = []

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
                                sellSpotRate=sellSpotRate)

    return render(request, 'rate.html',{
                'rateList': Rate.objects.all()
            })






# Create your views here.
class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer