from lib.deliveroo_class import *

def test_whether_order_address_is_saved():
    order = Order("123 Fake Street")
    assert order.address == "123 Fake Street"

# When we add two valid items to the order
# And we format the order note
# It returns a string with the address and the items
def test_whether_items_are_added_and_recalled():
    order = Order("123 Fake Street")
    order.add_item("Chair")
    order.add_item("Moisturiser")
    assert order.format_note() == "Order for 123 Fake Street: Chair, Moisturiser"