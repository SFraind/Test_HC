from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('product-access/', views.ProductAccessListCreateView.as_view(), name='product-access-list'),
    path('lessons/', views.LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lesson-views/', views.LessonViewListCreateView.as_view(), name='lesson-view-list-create'),
]
