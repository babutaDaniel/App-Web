from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import Max


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    type = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    profile_image = models.ImageField(null=False, blank=False, upload_to="images/")
    second_image = models.ImageField(null=False, blank=False, upload_to="images/")
    third_image = models.ImageField(null=False, blank=False, upload_to="images/")
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    avg = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    nr_com = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    likes = models.ManyToManyField(User, related_name='blog_post')
    total_like = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def total_likes(self):
        return self.likes.count()

    def most_likes(self):
        return self.likes.aggregate(most_like=Max('like'))


class Order(models.Model):
    avg = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)


RATE_CHOICES =[
    (1, '1 - Trash'),
    (2, '2 - Bad'),
    (3, '3 - OK'),
    (4, '4 - Good'),
    (5, '5 - Perfect'),
]


class Comment(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(blank=True, default=datetime.now)
    stars = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return '{}'.format(self.post.name)



