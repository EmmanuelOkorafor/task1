# Copyright (c) 2024, PearMonie LLC. All Rights Reserved.








from django.db import models
from django.contrib.auth.models import User




class Expenses(models.Model):
    user =  models.ForeignKey(User, on_delete = models.CASCADE)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    category = models.CharField(max_length = 50)
    description = models.TextField()
    date = models.DateField()


    def __str__(self):
        return f"{self.user.username}:   {self.amount} | {self.amount} | {self.category} | {self.description} | {self.date}"
    



class Budget(models.Model):
    user =  models.ForeignKey(User, on_delete = models.CASCADE)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    category = models.CharField(max_length = 50)


    def __str__(self):
        return f"{self.user.username}:   {self.amount} | {self.category}"
    
    # curl -X POST -d "username=pearmonie&password=pearmonie" http://127.0.0.1:8000/api/token/