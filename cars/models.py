from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True) 
    model = models.CharField(max_length=200) # modelo do carro, exemplo: "Onix"
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') # marca do carro, exemplo: "Chevrolet"
    factory_year = models.IntegerField(blank=True,null=True) # ano de fabricação, exemplo: 2022
    model_year = models.IntegerField(blank=True,null=True) # ano do modelo, exemplo: 2023
    plate = models.CharField(max_length=10, blank=True, null=True) # placa do carro, exemplo: "ABC-1234"
    value = models.FloatField(blank=True,null=True) # numero flutuante exemplo: 1234.56
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)  # imagem do carro

    def __str__(self):
        return self.model