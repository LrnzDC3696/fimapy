from rest_framework import serializers

from .models import ExpenseCategory, IncomeCategory, Account, Transfer, Expense, Income


class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = "__all__"


class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    current_balance = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = "__all__"

    def get_current_balance(self, obj):
        return obj.calculate_balance()


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = "__all__"
