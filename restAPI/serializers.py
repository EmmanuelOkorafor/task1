# Copyright (c) 2024, PearMonie LLC. All Rights Reserved.








from .models import Expenses, Budget
from rest_framework import serializers


# Rather than have a "def get()" that: formats and returns the user for
# each model.  

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'



class BudgetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'