#-----------------------------------------------------------------------------------------------------------------------
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
#-----------------------------------------------------------------------------------------------------------------------
from product.models import Category, Product, Review, Tag
from product.serializers import CategorySerializers, ProductSerializers, ReviewSerializers, ProductsReviewsSerializers,\
    ProductValidateSerializers, CategoryValidateSerializers, ReviewValidateSerializers
#-----------------------------------------------------------------------------------------------------------------------




class ProductsModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    validate_serializer_class = ProductValidateSerializers
    pagination_class = PageNumberPagination


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    validate_serializer_class = CategoryValidateSerializers
    pagination_class = PageNumberPagination


class ReviewModelViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    validate_serializer_class = ReviewValidateSerializers
    pagination_class = PageNumberPagination


class RatingModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsReviewsSerializers
    pagination_class = PageNumberPagination


@api_view(['GET'])
def products_reviews_api_view(request):
    products = Product.objects.all()
    serializer = ProductsReviewsSerializers(products, many=True)
    return Response(data=serializer.data)
