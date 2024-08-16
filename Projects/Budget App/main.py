class Category:

    def __init__(self, name):

        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):

        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):

        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description}) # Widthrawals set to negative for get_balance function
            return True
        return False

    def get_balance(self):

        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):

        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):

        return self.get_balance() >= amount

    def __str__(self):

        name = f"{self.name:*^30}\n"
        items = ""
        total = 0

        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}\n"
            total += item['amount']
        
        return name + items + "Total: " + f"{total:.2f}"

def create_spend_chart(categories):

    total = 0
    percents = []

    # Calculate the total across all categories
    for category in categories:
        for item in category.ledger:
            if item['amount'] < 0: total += -item['amount']
    
    # Calculate the percentage spent by category
    for category in categories:
        cat_total = 0
        for item in category.ledger:
            if item['amount'] < 0: cat_total += -item['amount']
        percent = (cat_total / total) * 100
        percents.append(percent)

    # Chart Set Up
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percent in percents:
            if percent >= i: chart += "o  "
            else: chart += "   "
        chart += "\n"
    chart += "    -" + "---" * len(categories) + "\n"

    length = max(len(category.name) for category in categories)

    for i in range(length):
        chart += "     "
        for category in categories:
            if i < len(category.name): chart += category.name[i] + "  "
            else: chart += "   "
        chart += "\n"

    return chart.rstrip("\n")

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

clothing = Category("Clothing")
auto = Category("Auto")
clothing.withdraw(15, "shirt")
clothing.withdraw(25, "jeans")
auto.deposit(500, "initial deposit")
auto.withdraw(100, "oil change")
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))