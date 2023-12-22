from django.urls import path

from item.views import ItemView, BuyItemView, PaymentView

urlpatterns = [
    path("", ItemView.as_view()),
    path("<int:item_id>", ItemView.as_view()),
    path("buy/<int:item_id>", BuyItemView.as_view()),
    path("payment_status/<str:status>", PaymentView.as_view()),
]
