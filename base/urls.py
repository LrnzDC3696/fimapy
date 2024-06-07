from django.urls import path
from .views import (
    hello_world,
    ExpenseCategoryList,
    ExpenseCategoryDetail,
    IncomeCategoryList,
    IncomeCategoryDetail,
    AccountList,
    AccountDetail,
    TransferList,
    TransferDetail,
    ExpenseList,
    ExpenseDetail,
    IncomeList,
    IncomeDetail,
)

urlpatterns = [
    path("", hello_world, name="base_hello-world"),
    path("expense/category/", ExpenseCategoryList.as_view(), name="expense-category_list"),
    path("expense/category/<int:pk>/", ExpenseCategoryDetail.as_view(), name="expense-category_detail"),
    path("income/category/", IncomeCategoryList.as_view(), name="income-category_list"),
    path("income/category/<int:pk>/", IncomeCategoryDetail.as_view(), name="income-category_detail"),
    path("account", AccountList.as_view(), name="account_list"),
    path("account/<int:pk>/", AccountDetail.as_view(), name="account_detail"),
    path("transfer", TransferList.as_view(), name="transfer-category_list"),
    path("transfer/<int:pk>/", TransferDetail.as_view(), name="transfer-category_detail"),
    path("expense", ExpenseList.as_view(), name="expense_list"),
    path("expense/<int:pk>/", ExpenseDetail.as_view(), name="expense_detail"),
    path("income", IncomeList.as_view(), name="income_list"),
    path("income/<int:pk>/", IncomeDetail.as_view(), name="income_detail"),
]
