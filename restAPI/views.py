# Copyright (c) 2024, PearMonie LLC. All Rights Reserved.








from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Expenses, Budget
from .serializers import BudgetsSerializer, ExpensesSerializer


# CRUD Operations


# List and creating new budgets
class BudgetList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Budget.objects.all()
    serializer_class = BudgetsSerializer



# Retrieving updating, and deleting budget
class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Budget.objects.all()
    serializer_class = BudgetsSerializer



class ExpensesList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer

class ExpensesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer



class PermissionDeniedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'error': 'You do not have permission to access this resource'}, status = 403)