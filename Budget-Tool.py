#Kai Francis
#Projected Amounts    
class BudgetApp:
    def __init__(self):
        self.income = 0
        self.expenses = {}
        self.savings_goal = 0
        self.bank_balance = 0

    # Adds income to total income
    def add_income(self):
        self.income = self.income + float(input("Enter income amount to be added: $"))

    # Removes income from total income
    def remove_income(self):
        remove_income = float(input("Enter income amount to be removed: $"))
        if self.income - remove_income < 0:
            print("Error: Not enough income")
            return
        else:
            self.income = self.income - remove_income
            return
    
    # Returns income amount
    def get_income(self):
        return self.income

    # Add an expense by category and amount
    # Stores expense in the expenses dictionary
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
        #Calculate the 50-30-20 rule distribution of the income.
        print("Total income is: $", self.income)
        needs = 0.5 * self.income
        wants = 0.3 * self.income
        savings = 0.2 * self.income
        return needs, wants, savings
    
    # def set_savings_goal(self):
    #     #Set a financial goal for saving."""
    #     try:
    #         # User enters their savings goal
    #         self.savings_goal = float(input("Enter your savings goal: $"))
    #         print(f"Savings goal set to: ${self.set_savings_goal():.2f}")
    #     except ValueError:
    #         print("Invalid input. Please enter a numeric value.")
    
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
    
    #emergency fund creation
    # Need to make a method that takes money from the uses
    def emergency_fund(self, deposit):
        account = 0
        if deposit < (self.income * .10):
            print(f"You are adding ${deposit} to emergency fund and removing from your overall income.")
            self.income = self.income - deposit
            account += deposit
        else:
            print("You are putting too much in your emergency fund!!!")



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
        try:
            cost = self.cost
            total_left = cost - money
            print(total_left)
        except:
            money < BudgetApp.get_income * 0.3
            print("You don't have enough money right now")
        


#Main
def main():
    app = BudgetApp()

    while True:
        #feature selction
        print("\nChoose a feature:")
        print(f"Current income is: ${app.income:.2f}")
        print("1. Financial Goals")
        print("2. Projected Amount")
        print("3. Monthly/Weekly Expenses")
        print("4. Income tracking (50-30-20 Rule)")
        print("5. Income Adjustment")
        print("6. Emergency Fund")
        print("7. Exit")


        try:
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            print("Please enter a valid choice (1-7).")
            continue

        if choice == 1:
            #set financial goals
            print("\n--- Financial Goals ---")
            app.set_savings_goal()
            #error: cannot run because set_savings_goal does not exist
            print(f"Savings goal set to: ${app.savings_goal:.2f}")
            set_goal = input("Do you want to create a personal goal?: Enter y/n ")
            # Ask the user if they want to set personal purchase goal. If answer is yes it will record their goal.
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
                print(personal_goal)
            else:
                print("No personal goal!")
    

        elif choice == 2:
            #calculate and display projected amount
            print("\n--- Projected Amount ---")
            app.add_expense()
            projected = app.calculate_projected_amount()
            print(f"Projected amount after expenses: ${projected:.2f}")

        elif choice == 3:
            #Display monthly/weekly expenses
            print("\n--- Monthly/Weekly Expenses ---")
            app.add_expense()
            timeframe  = input("Do you want a 'monthly' or 'weekly' breakdown? ").lower()
            breakdown = app.get_expense_breakdown(timeframe)
            print(f"Expense breakdown ({timeframe}): {breakdown}")

        elif choice == 4:
            #Income tracking using the 50-30-20 rule
            print("\n--- Income tracking (50-30-20 Rule) ---")
            needs, wants, savings = app.calculate_50_30_20_rule()
            print(f"Needs: ${needs:.2f}, Wants: ${wants:.2f}, Savings: ${savings:.2f}")
            
        elif choice == 5:
            # Adding or removing income, reset to 0, or exit
            print("\n--- Income Adjustment ---")
            print("1. Add to total income")
            print("2. Remove from total income")
            print("3. Check total income")
            print("4. Reset income to 0")
            print("5. Back to main menu.")
            try:
                adjchoice = int(input("Enter your choice (1-5): "))
            except ValueError:
                print("Please enter a valid choice (1-5).")
                continue
            if adjchoice == 1:
                app.add_income()
                print(f"New total income is: ${app.income:.2f}")
            if adjchoice == 2:
                app.remove_income()
                print(f"New total income is: ${app.income:.2f}")
            if adjchoice == 3:
                print(f"Total income is: ${app.income:.2f}")
            if adjchoice == 4:
                app.income = 0
                print(f"New total income is: ${app.income:.2f}")
            if adjchoice == 5:
                print("Exiting back to main budget menu.")
                               

        elif choice == 6:
            emergency_money = int(input("How much would you like to add to your emergency fund? $"))
            app.emergency_fund(emergency_money)

        elif choice == 7:
            #exit the program
            print("Exiting the program.")
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")    

if __name__ == "__main__":
    main()
