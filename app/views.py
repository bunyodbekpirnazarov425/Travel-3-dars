from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Video, Tour, Hotel
from .serializers import CategorySerializer, VideoSerializer, TourSerializer, HotelSerializer

class CategoryAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        categorys = Category.objects.get(pk=pk)
        serializer = CategorySerializer(categorys, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        categorys = Category.objects.get(pk=pk)
        categorys.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VideoAPIView(APIView):
    def get(self, request, pk):
        if pk:
            videolar = Video.objects.get(pk=pk)
            serializer = VideoSerializer(videolar)
            return Response(serializer.data, status=status.HTTP_200_OK)
        videolar = Video.objects.all()
        serializer = VideoSerializer(videolar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        videolar = Category.objects.get(pk=pk)
        serializer = VideoSerializer(videolar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        videolar = Category.objects.get(pk=pk)
        videolar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TourAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            tours = Tour.objects.get(pk=pk)
            serializer = TourSerializer(tours)
            return Response(serializer.data, status=status.HTTP_200_OK)
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        tours = Tour.objects.get(pk=pk)
        serializer = TourSerializer(tours, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tours = Tour.objects.get(pk=pk)
        tours.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HotelAPIView(APIView):
    def get(self, request, pk):
        if pk:
            hotels = Hotel.objects.get(pk=pk)
            serializer = HotelSerializer(hotels)
            return Response(serializer.data, status=status.HTTP_200_OK)
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        hotels = Tour.objects.get(pk=pk)
        serializer = HotelSerializer(hotels, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        hotels = Tour.objects.get(pk=pk)
        hotels.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)