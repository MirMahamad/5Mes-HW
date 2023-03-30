from rest_framework import serializers
from product.models import Category, Product, Review


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name products_count products_list'.split()


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title description price category_name'.split()


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars product_title'.split()


class ProductsReviewsSerializers(serializers.ModelSerializer):
    # reviews = ReviewSerializers(many=True)

    class Meta:
        model = Product
        fields = 'id reviews rating'.split()
