from.models import News, Login, Category, NewsMaster, UserData, User
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = News
		fields = ("title", "description", "link")

class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = Login
		fields = ("Login_id","Login_type","status","craeted_at","updated_at")

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ("category_name","category_description","created_at","updated_at")

class NewsMasterSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewsMaster
		fields = ("news_title","news_headline","news_image","news_assets","news_category_id","news_text","craeted_at","updated_at")

class UserDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserData
		fields = ("user_id","news_id","created_at","updated_at")

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ("user_id","first_name","last_name","email","password","mob_no","OTP","fb_check","loc_latitude","loc_longitude","created_at","updated_at")




