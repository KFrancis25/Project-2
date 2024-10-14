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
    
    def calculate_50_30_20_rule(self):
        """Calculate the 50-30-20 rule distribution of the income."""
        needs = 0.5 * self.income
        wants = 0.3 * self.income
        savings = 0.2 * self.income
        return needs, wants, savings
    
    def track_progress(self):
        saved_amount = self.bank_balance - sum(self.expenses.values())
        if self.savings_goal > 0:
            return saved_amount / self.savings_goal * 100
        else:
            return 0   

    def get_expense_breakdown(self, timeframe="monthly"):
        if timeframe == "monthly":
            return {category: amount for category, amount in self.expenses.items()}
        elif timeframe == "weekly":
            return {category: amount/ 4 for category, amount in self.expenses.items()}     

    #tentative 50-30-20 rule (for testing)
    def bank_account_based_budgeting(self):
        needs, wants, savings = self.calculate_50_30_20_rule()
        needs_allocated = self.bank_balance * 0.5
        wants_allocated = self.bank_balance * 0.3
        savings_allocated = self.bank_balance * 0.2
        return needs_allocated, wants_allocated, savings_allocated
#Ryan Yonek
#50-20-30 Rule (try to use the same function name in main)

#Keith Young
#Personal Purchase Goals
# Sets the goal its costs and how many weeks a person has to achieve it
class Goals:
    def __init__(self, goal, cost, weeks):
        self.goal = goal
        self.cost = cost
        self.weeks = weeks
        print(f"My goal is to buy a {self.goal} in {self.weeks} weeks. It cost ${self.cost}")
        
    #Payment towards the goal
    def payment(self, money):
        cost = self.cost
        total_left = cost - money
        print(total_left)
        
#emergency fund creation
def emergency_fund():
    money = 500
    if money < (BudgetApp.set_income * .10):
        return True
    print(f"You can use this amount{money}")
    BudgetApp.set_income = BudgetApp.set_income + money

#Main
def main():
    app = BudgetApp()

    while True:
        #feature selction
        print("\nChoose a feature:")
        print("1. Financial Goals")
        print("2. Projected Amount")
        print("3. Monthly/Weekly Expenses")
        print("4. Income tracking (50-20-30 Rule)")
        print("5. Exit")


        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Please enter a valid choice (1-5).")
            continue

        if choice == 1:
            #set financial goals
            print("\n--- Finacial Goals ---")
            app.set_savings_goal()
            #error: cannot run because set_savings_goal does not exist
            print(f"Savings goals set to ${app.set_savings_goal:.2f}")
            set_goal = input("Do you want to create a personal goal?: Enter y/n ")
            try: 
                print(set_goal)
            except:
                if set_goal != "y" or "n":
                    print ("Enter a y or n for yes or no!")
            if set_goal == "y":
                ask_goal = input("What is your goal? ")
                ask_cost = int(input("What is the cost? ")) 
                ask_weeks = int(input("In how many weeks do you want to accomplish this goal?"))
                personal_goal = Goals(ask_goal, ask_cost, ask_weeks)
            else:
                print("No personal goal!")
    

        elif choice == 2:
            #calculate and display projected amount
            print("\n--- Projected Amount ---")
            app.set_income()
            app.add_expense()
            projected = app.calculate_projected_amount()
            print(f"Projected ampunt after expenses: ${projected:.2f}")

        elif choice == 3:
            #Display monthly/weekly expenses
            print("\n--- Monthly/Weekly Expenses ---")
            app.add_expense()
            timeframe  = input("Do you want a 'monthly' or 'weekly' breakdown? ").lower()
            breakdown = app.get_expense_breakdown(timeframe)
            print(f"Expense breakdown ({timeframe}): {breakdown}")

        elif choice == 4:
            #Income tracking using the 50-20-30 rule
            print("\n--- Income tracking (50-20-30 Rule) ---")
            app.set_income()
            needs, wants, savings = app.calculate_50_30_20_rule()
            print(f"Needs: ${needs:.2f}, Wants: ${wants:.2f}, Savings: ${savings:.2f}")
        
        elif choice == 5:
            #exit the program
            print("Exiting the program Thank you!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")    
        

    #set income
    # app.set_income()

    # #expenses
    # app.add_expense()

    # #set savings goal
    # app.set_savings_goal()

    # #display projected financial amount
    # projected = app.calculate_projected_amount()
    # print(f"\nProjected amount after expenses: ${projected:.2f}")

    #display 50-30-20 rule breakdown

    #expense breakdown

    #bank account-based budgeting


if __name__ == "__main__":
    main()
