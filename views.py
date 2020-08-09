import requests
import xml.etree.ElementTree as ET
from .models import RssUrl, News, Login, Category, NewsMaster, UserData, User
from rest_framework import generics
from .serializers import NewsSerializer, LoginSerializer,CategorySerializer, NewsMasterSerializer, UserDataSerializer,UserSerializer
from django.shortcuts import HttpResponse


class NewsList(generics.ListAPIView):
    queryset = News.objects.all().order_by("-id")[:5]
    serializer_class = NewsSerializer

class LoginList(generics.ListAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class NewsMasterList(generics.ListAPIView):
    queryset = NewsMaster.objects.all()
    serializer_class = NewsMasterSerializer

class UserDataList(generics.ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer





def create_models(request):
    urls = RssUrl.objects.all()
    for url in urls:
        url=url.url
        resp = requests.get(url)
        resp = resp.content
        root = ET.fromstring(resp)
        for news in root.iter("item"):
            title = news.find("title").text
            description = news.find("description").text
            link = news.find("link").text
            News.objects.create(title=title, description=description, link=link)
    return HttpResponse("News Model created Successfully!")
