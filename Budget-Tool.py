#Kai Francis
#Projected Amounts    
class BudgetApp:
    def __init__(self):
        self.income = 0
        self.expenses = {}
        self.savings_goal = 0
        self.bank_balance = 0
    
    def set_income(self):
        self.income = float(input("Enter your monthly income: $"))

    def add_expense(self):
        while True:
            category = input("Enter expense category (or type 'done' to finish): ").lower()
            if category == 'done':
                break
            try:
                amount = float(input(f"Enter amount for {category}: $"))
                if category in self.expenses:
                    self.expenses[category] += amount
                else:
                    self.expenses[category] = amount
            except ValueError:
                print("Please enter a valid number.")
    
    def set_savings_goal(self):
        try:
            self.savings_goal = float(input("Enter your savings goal: $"))
        except ValueError:
            print("Please enter a vaild number.")
    
    def calculate_projected_amount(self):
        total_expenses = sum(self.expenses.values())
        return self.income - total_expenses
    
    def track_progress(self):
        saved_amount = self.bank_balance - sum(self.expenses.values())
        if self.savings_goal > 0:
            return saved_amount / self.savings_goal * 100
        else:
            return 0        

#Keith Young
#Financial Goals

class Goals:
    def __init__(self, goal, cost, weeks):
        self.goal = goal
        self.cost = cost
        self.weeks = weeks
        print(f"My goal is to buy a {self.goal} in {self.weeks} weeks. It cost ${self.cost}")
    
    def payment(self, money):
        cost = self.cost
        total_left = self.cost - money
        print(total_left)
        

def emergency_fund():
    money = 500
    if money < (BudgetApp.set_income * .10):
        return True
    print(f"You can use this amount{money}")
    BudgetApp.set_income = BudgetApp.set_income + money

#Main
def main():
    app = BudgetApp()

    #set income
    app.set_income()

    #expenses
    app.add_expense()

    #set savings goal
    app.set_savings_goal()

    #display projected financial amount
    projected = app.calculate_projected_amount()
    print(f"\nProjected amount after expenses: ${projected:.2f}")

    #display 50-30-20 rule breakdown

    #expense breakdown

    #bank account-based budgeting


if __name__ == "__main__":
    main()
