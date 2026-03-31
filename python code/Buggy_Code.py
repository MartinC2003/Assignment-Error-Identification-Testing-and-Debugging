# order_management.py

class Order:
    def __init__(self, customer_name, items):
        self.customer_name = customer_name
        self.items = items  

    """
    Error: calculate_total used addition instead of multiplication, producing incorrect totals.
    Old Code:
        def calculate_total(self):
            total = 0
            for item in self.items:
                total += item[1] + item[2]
            if total == 0:
                return "Empty Order"
            return total
    Fixed Code:
        def calculate_total(self):
            total = 0
            for item in self.items:
                total += item[1] * item[2]
            return total
    """

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1] * item[2]  # item[1] + item[2] changed to item[1] * item[2]
        return total
    
    """
    Error: Missing colon in add_item method caused a SyntaxError.
    Old Code:
        def add_item(self, item_name, quantity, price)
            self.items.append((item_name, quantity, price)) 
    Fixed Code:
        def add_item(self, item_name, quantity, price):
            self.items.append((item_name, quantity, price)) 
    """
    def add_item(self, item_name, quantity, price): #colon added at the end of the add_item statement
        self.items.append((item_name, quantity, price))  

    def remove_item(self, item_name):
        for item in self.items:  
            if item[0] == item_name:
                self.items.remove(item)  
    
    """
   Error 1: Incorrect spelling of items attribute caused a RuntimeError
   Error 2: Missing closing parenthesis at the end of print statement caused a SyntaxError
   Error 3: Missing clause to handle orders with no items can cause a unhandled ExceptionError
  
   Solution 1: 
   Old Code:
       def add_item(self, item_name, quantity, price)
           self.items.append((item_name, quantity, price)) 
   Fixed Code:
       for item in self.items: #<--spelling corrected
           print(f"{item[1]} x {item[0]} @ ${item[2]:.2f}")


   Solution 2:
       Old Code:
       def add_item(self, item_name, quantity, price)
           self.items.append((item_name, quantity, price)) 
       Fixed Code:
           for item in self.items: #<--spelling corrected
               print(f"{item[1]} x {item[0]} @ ${item[2]:.2f}")
   
   Solution 3:
       Old Code:
        print("Order Summary for", self.customer_name)
       Fixed Code:
        if not self.items:
            print("No items in this order.") # print statement to return when order is empty, instead of the string

    """
    def print_summary(self):
        if not self.items:
            print("No items in this order.") # print statement to return when order is empty, instead of the string
            return
        print("Order Summary for", self.customer_name)
        for item in self.items: #self.itemz corrected to self.items
             print(f"{item[1]} x {item[0]} @ ${item[2]:.2f}")
        print("Total: $", self.calculate_total()) #closing parenthesis added to the print statement
    
    """
    Error: Missing else clause for return value 
    Old Code:
        def apply_discount(self, code):
            if code == "SAVE10":
                return 0.1
            elif code == "SAVE20":
                return 0.2
    Fixed Code:
        def apply_discount(self, code):
            if code == "SAVE10":
                return 0.1
            elif code == "SAVE20":
                return 0.2
            else:
                return 0.0
    """
    def apply_discount(self, code): 
        if code == "SAVE10":
            return 0.1
        elif code == "SAVE20":
            return 0.2
        else:
            return 0.0 #added return value 0.0 for mismatched discount codes
        

"""
Error: program was missing the calculate_total() function during runtime and was added in 
Old Code:
    def main():
        order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
        order.add_item("Notebook", 3, 5.00)
        order.remove_item("Pen")
        order.print_summary()
        discount = order.apply_discount("SAVE30")
        print("Discount rate:", discount)
Fixed Code:
    def main():
        order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
        order.add_item("Notebook", 3, 5.00)
        order.remove_item("Pen")
        order.print_summary()
        discount = order.apply_discount("SAVE30")
        total = order.calculate_total()
        discounted_total = total * (1 - discount)
        print("Discount rate:", discount)
        print("Total after discount: $", discounted_total)
"""
def main():
    order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
    order.add_item("Notebook", 3, 5.00)
    order.remove_item("Pen")
    order.print_summary()
    discount = order.apply_discount("SAVE30")
    total = order.calculate_total()
    discounted_total = total * (1 - discount) #calculates the discounted total
    print("Discount rate:", discount)
    print("Total after discount: $",discounted_total)

main()
