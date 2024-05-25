from django.contrib import admin

from .models import ExpenseCategory, IncomeCategory, Account, Transfer, Income, Expense

# Register your models here.
admin.site.register(ExpenseCategory)
admin.site.register(IncomeCategory)
admin.site.register(Account)
admin.site.register(Transfer)
admin.site.register(Income)
admin.site.register(Expense)