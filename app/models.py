from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField()

    def __str__(self):
        return self.name

class Tour(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    price = models.IntegerField()
    date = models.IntegerField()
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name