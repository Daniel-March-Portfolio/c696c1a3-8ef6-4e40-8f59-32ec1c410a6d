from item.models import Item


def create_stripe_line_item(item: Item, count: int = 1) -> dict:
    return {
        "price_data": {
            "product_data": {
                "name": item.name,
                "description": item.description
            },
            "unit_amount": item.price,
            "currency": "usd"
        },
        "quantity": count,
    }
