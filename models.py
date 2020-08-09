from django.db import models



class RssUrl(models.Model):
    url = models.CharField(max_length=100)
class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    link = models.CharField(max_length=200)

    def _str_(self):
        return str(self.title)

class Login(models.Model):
    Login_id = models.IntegerField(max_length=30)
    Login_type = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    Category_name = models.CharField(max_length=30)
    Category_description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class NewsMaster(models.Model):
    news_id = models.IntegerField(max_length=30)
    news_title = models.CharField(max_length=50)
    news_headline = models.CharField(max_length=30)
    news_image = models.ImageField(blank=True, null=True)
    news_assets = models.CharField(max_length=100)
    news_category_id = models.IntegerField(max_length=20)
    news_text = models.CharField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserData(models.Model):
    user_id = models.IntegerField(max_length=30)
    news_id = models.IntegerField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    user_id = models.IntegerField(max_length=30)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=70, blank=True)
    password = models.CharField(max_length=32)
    mob_no = models.IntegerField(max_length=20)
    OTP = models.IntegerField(max_length=10)
    fb_check = models.CharField(max_length=30)
    loc_latitude = models.FloatField()
    loc_longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




