from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/categories/', views.CategoryModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/categories/<int:pk>/', views.CategoryModelViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                                            'delete': 'destroy',
                                                                            'patch': 'partial_update'})),
    path('api/v1/products/', views.ProductsModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/products/<int:pk>/', views.ProductsModelViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                                          'delete': 'destroy',
                                                                          'patch': 'partial_update'})),
    path('api/v1/reviews/', views.ReviewModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/reviews/<int:pk>/', views.ReviewModelViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                                       'delete': 'destroy',
                                                                       'patch': 'partial_update'})),
    path('api/v1/products/reviews/', views.RatingModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/products/reviews/<int:pk>/', views.RatingModelViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                                                'delete': 'destroy',
                                                                                'patch': 'partial_update'})),
]