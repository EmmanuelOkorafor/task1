# Copyright (c) 2024, PearMonie LLC. All Rights Reserved.








from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect




class ExpensesAndBudgetAccessMiddleware(MiddlewareMixin):

    def sieve(self, request):
        protectedPaths = ['budget/', 'expenses/']

        # if the requested endpoint is token protected and the user hasn't been authenticated
        if request.path in protectedPaths and not request.user.IsAuthenticated:

            # prompt an access denied message to the user
            return redirect('permission_denied')