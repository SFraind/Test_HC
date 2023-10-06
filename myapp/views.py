from rest_framework import generics
from .models import Product, ProductAccess, Lesson, LessonView
from .serializers import ProductSerializer, ProductAccessSerializer, LessonSerializer, LessonViewSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductAccessListCreateView(generics.ListCreateAPIView):
    queryset = ProductAccess.objects.all()
    serializer_class = ProductAccessSerializer

class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonViewListCreateView(generics.ListCreateAPIView):
    queryset = LessonView.objects.all()
    serializer_class = LessonViewSerializer
