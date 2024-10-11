from rest_framework import serializers
from .models import Category, Video, Tour, Hotel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'
        # extra_kwargs = {'description':{'write_only':True}, 'id':{'read_only':True}}
        # read_only_fields = ['description', 'price']
        depth = 1
        # exclude = ['description', 'price']
        # fields = ['id', 'name', 'description', 'price', 'date']


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
        depth = 1