from django.contrib import admin
from .models import RssUrl, News, Login, NewsMaster, Category, UserData,User
admin.site.register(RssUrl)
admin.site.register(News)
admin.site.register(Login)
admin.site.register(Category)
admin.site.register(NewsMaster)
admin.site.register(UserData)
admin.site.register(User)