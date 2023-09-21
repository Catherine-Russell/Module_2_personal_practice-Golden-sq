class Order():
    def __init__(self, address):
        self.address = address
        self.order_list = []

    def add_item(self, item):
        self.order_list.append(item)

    def format_note(self):
        return f"Order for {self.address}: {', '.join(self.order_list)}"
    