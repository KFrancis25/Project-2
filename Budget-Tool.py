#Kai Francis
#Projected Amounts    
class BudgetApp:
    def __init__(self):
        self.income = 0
        self.expenses = {}
        self.savings_goal = 0
        self.bank_balance = 0
        self.account = 0
        
    # Ryan Yonek
    # Adds income to total income
    def add_income(self):
        self.income = self.income + float(input("Enter income amount to be added: $"))

    # Ryan Yonek
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
        self.add_income()
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
    
    #emergency fund creation
    # Keith Young, Ryan Yonek
    def emergency_fund(self, deposit):
        if deposit < (self.get_income() * .10):
            print(f"You want add {deposit} to your emergency fund.")
            self.account += deposit
        else:
            print("You are putting too much in your emergency fund!!!")
    
    # Returns emergency fund amount
    # Ryan Yonek
    def get_emergency_fund(self):
        return self.account



#Keith Young
#Personal Purchase Goals
# Sets the goal its costs and how many weeks a person has to achieve it
class Goals:
    def __init__(self, goal, cost, weeks):
        self.goal = goal
        self.cost = cost
        self.weeks = weeks
    
    def check_goal(self):
        return self.goal, self.cost, self.weeks
        
    #Payment towards the goal
    def payment(self, money):
        try:
            cost = self.cost
            total_left = cost - money
            print(total_left)
        except:
            money < self.get_income() * 0.3
            print("You don't have enough money right now")
        


#Main
def main():
    app = BudgetApp()

    while True:
        #feature selction
        print("\nChoose a feature:")
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
                if set_goal == 'y':
                    ask_goal = input("What are you saving for? ")
                    ask_cost = int(input("What is the cost? $")) 
                    ask_weeks = int(input("In how many weeks do you want to accomplish this goal? "))
                    goals = Goals(ask_goal, ask_cost, ask_weeks)
                    print(f"My goal is to buy a {goals.goal} in {goals.weeks} weeks. It cost ${goals.cost}")
                    add_to_goal = input("Do you want to make a payment to the personal goal?: Enter y/n ")
                    try:
                        if add_to_goal == 'y':
                            money = input("How much would you like to pay towards the goal? $")
                            goals.payment(money)
                            print("Current goal is now: ", goals.check_goal())
                        if add_to_goal == 'n':
                            print("Back to main menu")
                    except:
                        if set_goal != "y" or "n":
                            print("Enter a y or n for yes or no!")
                if set_goal == 'n':
                    print("No savings goal set. Back to main menu")
            except:
                if set_goal != "y" or "n":
                    print ("Enter a y or n for yes or no!")
            else:
                print("No personal goal! Did not enter 'y' or 'n'. Back to main menu.")

    

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
            print("3. Reset income to 0")
            print("4. Back to main menu.")
            try:
                adjchoice = int(input("Enter your choice (1-4): "))
            except ValueError:
                print("Please enter a valid choice (1-4).")
                continue
            if adjchoice == 1:
                app.add_income()
                print(f"New total income is: ${app.income:.2f}")
            if adjchoice == 2:
                app.remove_income()
                print(f"New total income is: ${app.income:.2f}")
            if adjchoice == 3:
                app.income = 0
                print(f"New total income is: ${app.income:.2f}")
            if adjchoice == 4:
                print("Exiting back to main budget menu.")
                               

        elif choice == 6:
            emergency_money = int(input("How much would you like to add to your emergency fund? "))
            app.emergency_fund(emergency_money)
            try:
                check_fund = input("Do you want to see emergency fund? y or n ")
                if check_fund == 'y':
                    print("Emergency fund is: ", app.get_emergency_fund())
                if check_fund == 'n':
                    print("Going back to main menu")
            except:
                if check_fund != 'y' or 'n':
                    print('Answer y or n for yes or no.')
            

        elif choice == 7:
            #exit the program
            print("Exiting the program.")
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")    

if __name__ == "__main__":
    main()
