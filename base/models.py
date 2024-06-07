from django.db import models
from django.db.models import Sum
from django.core.validators import MaxValueValidator


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name


class IncomeCategory(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=256, blank=True)
    balance = models.IntegerField(default=0)

    def calculate_balance(self):
        total_income = Income.objects.filter(account=self.pk).aggregate(total=Sum('amount'))['total'] or 0
        total_expense = Expense.objects.filter(account=self.pk).aggregate(total=Sum('amount'))['total'] or 0
        total_transfer_from = Transfer.objects.filter(account_from=self.pk).aggregate(total=Sum('amount'))['total'] or 0
        total_transfer_to = Transfer.objects.filter(account_to=self.pk).aggregate(total=Sum('amount'))['total'] or 0

        return total_income + total_expense - total_transfer_from + total_transfer_to


    def __str__(self):
        return self.name


class Transfer(models.Model):
    amount = models.IntegerField()
    notes = models.CharField(max_length=256, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    account_from = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="acc_from")
    account_to = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="acc_to")

    def __str__(self):
        return self.account_from + " -> " + self.account_to


class Expense(models.Model):
    amount = models.IntegerField(validators=[MaxValueValidator(-1)])
    notes = models.CharField(max_length=256, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.DO_NOTHING)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)


class Income(models.Model):
    amount = models.PositiveIntegerField()
    notes = models.CharField(max_length=256, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(IncomeCategory, on_delete=models.DO_NOTHING)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
