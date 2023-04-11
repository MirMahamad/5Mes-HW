#-----------------------------------------------------------------------------------------------------------------------
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
#-----------------------------------------------------------------------------------------------------------------------
from product.models import Category, Product, Review, Tag
#-----------------------------------------------------------------------------------------------------------------------


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


class CategoryValidateSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)


class ProductValidateSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(required=False, default='No description')
    price = serializers.IntegerField(min_value=0)
    category = serializers.IntegerField()

    def validate_category(self, category_id):
        for i in category_id:
            try:
                Product.objects.get(id=i)
            except Product.DoesNotExist:
                raise ValidationError(f'Product with id ({i}) not found')
            return i

    def validate_tag(self, tags):
        filtered_tags = Tag.objects.filter(id__in=tags)
        if len(tags) == filtered_tags.count():
            return tags
        lst_ = {i['id'] for i in filtered_tags.values_list().values()}
        raise ValidationError(f'This ids doesnt exist {set(tags).difference(lst_)}')


class ReviewValidateSerializers(serializers.Serializer):
    text = serializers.CharField(required=False, default='None')
    stars = serializers.IntegerField(min_value=1, max_value=5)
    product_id = serializers.IntegerField()

    def validate_product_id(self, products_id):
        try:
            Review.objects.get(product_id=products_id)
        except Product.DoesNotExist:
            raise ValidationError(f'Review with id ({products_id}) not found')
        return products_id