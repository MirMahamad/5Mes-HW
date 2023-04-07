from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    @property
    def products_count(self):
        return self.products.count()

    @property
    def products_list(self):
        return [product.title for product in self.products.all()]

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                 related_name='products', null=True)
    tags = models.ManyToManyField('Tag', blank=True, null=True)

    @property
    def rating(self):
        stars = [review.stars for review in self.reviews.all()]
        return round(sum(stars) / len(stars), 2)

    @property
    def category_name(self):
        name_category = [category.name for category in self.category.all()]
        return name_category

    def __str__(self):
        return self.title


class Review(models.Model):
    CHOICES = ((i, '*' * i) for i in range(1, 6))
    product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                related_name='reviews')
    stars = models.IntegerField(choices=CHOICES, null=True)
    text = models.TextField(blank=True, null=True)

    @property
    def product_title(self):
        return self.product.title

    def __str__(self):
        return self.text


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

