from django.db import models

# Create your models here.

class Categoty(models.Model):
    name = models.CharField

class Staff(models.Model):

    name = models.CharField()
    price = models.FloatField()
    description = models.TextField()
    categoty = models.ForeignKey(Categoty, on_delete=models.CASCADE,null=True)
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.pictures = Picture.objects.filter(staff = self.id)

class Picture(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='files/images/',null=True)

