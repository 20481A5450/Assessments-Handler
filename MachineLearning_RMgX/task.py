class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def calculate_total(self, menu):
        total = sum(menu[item].price * qty for item, qty in self.items.items())
        return total

class Cafe:
    def __init__(self):
        self.menu = {
            'Coffee': MenuItem('Coffee', 2.5),
            'Tea': MenuItem('Tea', 1.5),
            'Sandwich': MenuItem('Sandwich', 5.0),
            'Burger': MenuItem('Burger', 7.0),
            'Fries': MenuItem('Fries', 3.0),
            'Cake': MenuItem('Cake', 4.0)
        }
        self.orders = {}

    def new_order(self, table):
        if table not in self.orders:
            self.orders[table] = Order()
        print(f"Order started for table {table}")

    def add_to_order(self, table, item, quantity):
        if table in self.orders:
            self.orders[table].add_item(item, quantity)
            print(f"Added {quantity} {item}(s) to table {table}'s order")

    def close_order(self, table):
        if table in self.orders:
            total = self.orders[table].calculate_total(self.menu)
            print(f"Total for table {table}: ${total:.2f}")
            del self.orders[table]

def main():
    cafe = Cafe()
    while True:
        action = input("Enter action (new, add, close, exit): ").strip().lower()
        if action == 'new':
            table = input("Enter table number: ").strip()
            cafe.new_order(table)
        elif action == 'add':
            table = input("Enter table number: ").strip()
            item = input("Enter item name: ").strip()
            quantity = int(input("Enter quantity: ").strip())
            cafe.add_to_order(table, item, quantity)
        elif action == 'close':
            table = input("Enter table number: ").strip()
            cafe.close_order(table)
        elif action == 'exit':
            break

if __name__ == "__main__":
    main()
