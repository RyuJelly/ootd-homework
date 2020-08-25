from django.db import models

# Create your models here.
class Sido(models.Model):
    sido_id = models.IntegerField(primary_key=True)
    sido_name = models.CharField(max_length=10,verbose_name="시도명")

class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=10,verbose_name="시군구명")
    city_lat = models.FloatField(default=0.0)
    city_lng = models.FloatField(default=0.0)
    sido_id = models.ForeignKey(Sido, on_delete=models.CASCADE)

class Image(models.Model):
    image_name = models.CharField(max_length=10,verbose_name="작성자")
    image_like = models.IntegerField(default=0)
    image_dislike = models.IntegerField(default=0)
    image_cnt = models.IntegerField(default=0)
    image_date = models.DateTimeField(auto_now_add=True)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    sido_id = models.ForeignKey(Sido, on_delete=models.CASCADE)
    image_file = models.FileField(blank=True, upload_to="photo_%Y_%m_%d")

