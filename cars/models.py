from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.

class Car(models.Model):
    vin=models.CharField(max_length=50, verbose_name='Vin',db_index=True)
    color=models.CharField(max_length=50,verbose_name='color')
    brand=models.CharField(max_length=50,verbose_name='Brand')
    CAR_TYPES =(
        (1,'Седан'),
        (2,'Хэтчбек'),
        (3,'Универсал'),
        (4,'Купе')
    )
    car_type=models.IntegerField(verbose_name='Car_Type',choices=CAR_TYPES)
    user=models.ForeignKey(User,verbose_name='Use', on_delete=models.CASCADE)
