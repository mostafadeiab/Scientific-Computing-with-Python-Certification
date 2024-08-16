
# Build a Budget App Project

Complete the `Category` class. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called `ledger` that is a list. The class should also contain the following methods:

## Methods

### 1. `deposit` method
- Accepts an amount and description.
- If no description is given, it should default to an empty string.
- The method should append an object to the ledger list in the form of `{'amount': amount, 'description': description}`.

### 2. `withdraw` method
- Similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number.
- If there are not enough funds, nothing should be added to the ledger.
- This method should return `True` if the withdrawal took place, and `False` otherwise.

### 3. `get_balance` method
- Returns the current balance of the budget category based on the deposits and withdrawals that have occurred.

### 4. `transfer` method
- Accepts an amount and another budget category as arguments.
- The method should add a withdrawal with the amount and the description 'Transfer to [Destination Budget Category]'.
- The method should then add a deposit to the other budget category with the amount and the description 'Transfer from [Source Budget Category]'.
- If there are not enough funds, nothing should be added to either ledger.
- This method should return `True` if the transfer took place, and `False` otherwise.

### 5. `check_funds` method
- Accepts an amount as an argument.
- Returns `False` if the amount is greater than the balance of the budget category and returns `True` otherwise.
- This method should be used by both the withdraw method and transfer method.

## Printing the Budget Object

When the budget object is printed, it should display:

- A title line of 30 characters where the name of the category is centered in a line of `*` characters.
- A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right-aligned, contain two decimal places, and display a maximum of 7 characters.
- A line displaying the category total.

### Example Usage

```python
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
```

### Example Output

```
*************Food*************
deposit               1000.00
groceries              -10.15
restaurant and more foo-15.89
Transfer to Clothing   -50.00
Total: 923.96
```

## `create_spend_chart` Function

Besides the `Category` class, create a function (outside of the class) called `create_spend_chart` that takes a list of categories as an argument. It should return a string that is a bar chart.

- The chart should show the percentage spent in each category passed in to the function.
- The percentage spent should be calculated only with withdrawals and not with deposits.
- Down the left side of the chart should be labels 0 - 100.
- The 'bars' in the bar chart should be made out of the 'o' character.
- The height of each bar should be rounded down to the nearest 10.
- The horizontal line below the bars should go two spaces past the final bar.
- Each category name should be written vertically below the bar.
- There should be a title at the top that says 'Percentage spent by category'.

This function will be tested with up to four categories.

### Example Output

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

**Note**: Open the browser console with `F12` to see a more verbose output of the tests.
