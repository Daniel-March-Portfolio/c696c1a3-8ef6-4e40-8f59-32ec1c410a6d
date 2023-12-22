import stripe
from django.conf import settings
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from item.models import Item
from item.utils.create_stripe_line_item import create_stripe_line_item


class ItemView(View):
    def get(self, request: HttpRequest, item_id: int | None = None):
        if item_id is not None:
            item: Item = Item.objects.get(id=item_id)
            return render(request, "item/item.html", {"item": item})
        items: list[Item] = Item.objects.all()
        return render(request, "item/items.html", {"items": items})


class BuyItemView(View):
    def get(self, request: HttpRequest, item_id: int):
        item = Item.objects.get(id=item_id)
        stripe_session = stripe.checkout.Session.create(
            line_items=[create_stripe_line_item(item, 1)],
            mode="payment",
            api_key=settings.STRIPE_API_KEY,
            success_url=settings.STRIPE_BACK_URL + "/item/payment_status/success",
            cancel_url=settings.STRIPE_BACK_URL + "/item/payment_status/canceled",
        )
        return redirect(stripe_session.url)


class PaymentView(View):
    def get(self, request: HttpRequest, status: str):
        return render(request, "item/status.html", {"status": status})
